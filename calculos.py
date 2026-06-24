from datetime import datetime

# Salarios mínimos 2026 — actualiza cada año
SALARIO_MINIMO_GENERAL  = 278.80   # Zona general
SALARIO_MINIMO_FRONTERA = 419.88   # Zona libre frontera norte


def calcular(datos, zona_frontera=False):
    salario                   = float(datos["salario_diario"])
    dias_vacaciones_pendientes = int(datos["v_p"]) if datos["v_p"] else 0
    dias_salario_pendiente     = int(datos["s_p"]) if datos["s_p"] else 0

    # Prima vacacional: acepta 25 o 0.25
    if datos["prima"]:
        valor         = float(datos["prima"])
        prima_decimal = valor / 100 if valor >= 1 else valor
    else:
        prima_decimal = 0.25

    dias_aguinaldo_anual  = int(datos["dias_aguinaldo"]) if datos["dias_aguinaldo"] else 15
    dias_vacaciones_anual = int(datos["vacaciones"])     if datos["vacaciones"]     else 12

    fecha_ingreso = datetime.strptime(datos["ingreso"], "%d/%m/%Y")
    fecha_baja    = datetime.strptime(datos["baja"],    "%d/%m/%Y")

    # ── ANTIGÜEDAD ──────────────────────────────────────────────────────────
    dias_totales   = (fecha_baja - fecha_ingreso).days   # sin +1, igual que FiscoClic
    anios_trabajados = dias_totales / 365
    anios_completos  = int(anios_trabajados)

    # ── SDI (Salario Diario Integrado) ───────────────────────────────────────
    factor_integracion = (
        1
        + (dias_aguinaldo_anual / 365)
        + (dias_vacaciones_anual * prima_decimal / 365)
    )
    sdi = salario * factor_integracion

    # ────────────────────────────────────────────────────────────────────────
    # 1. MONTOS PENDIENTES
    # ────────────────────────────────────────────────────────────────────────
    monto_sueldos              = dias_salario_pendiente     * salario
    monto_vacaciones_pendientes = dias_vacaciones_pendientes * salario
    monto_prima_pendiente       = monto_vacaciones_pendientes * prima_decimal

    # ────────────────────────────────────────────────────────────────────────
    # 2. AGUINALDO PROPORCIONAL
    #    Mismo criterio que FiscoClic: días trabajados en el año CALENDARIO
    #    de la baja (1 ene → fecha baja), incluyendo el día de baja.
    # ────────────────────────────────────────────────────────────────────────
    inicio_anio_calendario  = datetime(fecha_baja.year, 1, 1)
    fecha_inicio_aguinaldo  = max(fecha_ingreso, inicio_anio_calendario)
    dias_aguinaldo_periodo  = (fecha_baja - fecha_inicio_aguinaldo).days + 1  # incluye día de baja

    aguinaldo_proporcional  = (dias_aguinaldo_anual / 365) * dias_aguinaldo_periodo * salario

    # ────────────────────────────────────────────────────────────────────────
    # 3. VACACIONES PROPORCIONALES
    #    Solo la fracción del año incompleto TRAS el último aniversario.
    #    Si no hay fracción (exactamente N años), el monto es 0.
    # ────────────────────────────────────────────────────────────────────────
    if anios_completos > 0:
        try:
            ultimo_aniversario = datetime(
                fecha_ingreso.year + anios_completos,
                fecha_ingreso.month,
                fecha_ingreso.day,
            )
        except ValueError:
            # Fecha bisiesta (ej. 29 feb) → usar 28 feb
            ultimo_aniversario = datetime(
                fecha_ingreso.year + anios_completos,
                fecha_ingreso.month,
                28,
            )
        dias_fraccion = (fecha_baja - ultimo_aniversario).days
    else:
        dias_fraccion = dias_totales

    vacaciones_proporcionales = (dias_vacaciones_anual / 365) * dias_fraccion * salario
    prima_proporcional        = vacaciones_proporcionales * prima_decimal

    # ────────────────────────────────────────────────────────────────────────
    # 4. TOTAL FINIQUITO
    # ────────────────────────────────────────────────────────────────────────
    total_finiquito = (
        monto_sueldos
        + monto_vacaciones_pendientes
        + monto_prima_pendiente
        + aguinaldo_proporcional
        + vacaciones_proporcionales
        + prima_proporcional
    )

    # ────────────────────────────────────────────────────────────────────────
    # 5. INDEMNIZACIÓN Y PRIMA DE ANTIGÜEDAD
    # ────────────────────────────────────────────────────────────────────────
    salario_minimo = SALARIO_MINIMO_FRONTERA if zona_frontera else SALARIO_MINIMO_GENERAL
    tope_prima     = salario_minimo * 2
    salario_tope   = min(salario, tope_prima)

    indemnizacion_90 = 0.0
    indemnizacion_20 = 0.0
    prima_antiguedad = 0.0

    if datos["motivo"] == "Despido":
        indemnizacion_90 = 90 * sdi
        indemnizacion_20 = 20 * sdi * anios_trabajados          # Art. 50 LFT
        prima_antiguedad = 12 * salario_tope * anios_trabajados  # Art. 162 LFT

    elif datos["motivo"] == "Renuncia" and anios_trabajados >= 15:
        # Prima de antigüedad aplica también en renuncia con 15+ años (Art. 162)
        prima_antiguedad = 12 * salario_tope * anios_trabajados

    total_liquidacion = indemnizacion_90 + indemnizacion_20 + prima_antiguedad
    gran_total        = total_finiquito + total_liquidacion

    return {
        "sdi":                        sdi,
        "sueldos_pendientes":         monto_sueldos,
        "vacaciones_pendientes":      monto_vacaciones_pendientes,
        "prima_vacacional_pendiente": monto_prima_pendiente,
        "aguinaldo_proporcional":     aguinaldo_proporcional,
        "vacaciones_proporcionales":  vacaciones_proporcionales,
        "prima_proporcional":         prima_proporcional,
        "total_finiquito":            total_finiquito,
        "indemnizacion_90":           indemnizacion_90,
        "indemnizacion_20":           indemnizacion_20,
        "prima_antiguedad":           prima_antiguedad,
        "total_liquidacion":          total_liquidacion,
        "gran_total":                 gran_total,
    }