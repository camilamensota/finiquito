from datetime import datetime

def calcular(datos):
        salario = float(datos["salario_diario"])
        dias_vacaciones_pendientes = int(datos["v_p"]) if datos["v_p"] else 0 
        dias_salario_pendiente = int(datos["s_p"]) if datos["s_p"] else 0

        if datos["prima"]:
                valor = float(datos["prima"])
                prima_decimal = valor / 100 if valor >= 1 else valor
        else:
                prima_decimal = 0.25

        dias_aguinaldo_anual = int(datos["dias_aguinaldo"]) if datos["dias_aguinaldo"] else 15
        dias_vacaciones_anual = int(datos["vacaciones"]) if datos["vacaciones"] else 12

        factor_aguinaldo = dias_aguinaldo_anual / 365
        factor_prima_vacacional = (dias_vacaciones_anual * prima_decimal) / 365
        salario_diario_integrado = salario + (salario * factor_aguinaldo) + (salario * factor_prima_vacacional)

        fecha_ingreso = datetime.strptime(datos["ingreso"], "%d/%m/%Y")
        fecha_baja = datetime.strptime(datos["baja"], "%d/%m/%Y")
        
        dias_totales_antiguedad = (fecha_baja - fecha_ingreso).days + 1
        anios_trabajados = dias_totales_antiguedad / 365

        anio_baja = fecha_baja.year
        inicio_anio_baja = datetime(anio_baja, 1, 1)
        if fecha_ingreso > inicio_anio_baja:
                fecha_inicio_calculo = fecha_ingreso
        else:
                fecha_inicio_calculo = inicio_anio_baja
        dias_del_anio = (fecha_baja - fecha_inicio_calculo).days + 1

        monto_sueldos = dias_salario_pendiente * salario
        monto_vacaciones_pendientes = dias_vacaciones_pendientes * salario
        monto_prima_vacacional = prima_decimal * monto_vacaciones_pendientes

        dias_proporcion_aguinaldo = (dias_aguinaldo_anual / 365) * dias_del_anio
        monto_aguinaldo_proporcional = dias_proporcion_aguinaldo * salario

        factor_vacaciones = dias_vacaciones_anual / 365
        vacaciones_proporcionales = factor_vacaciones * dias_del_anio
        monto_vacaciones_proporcionales = vacaciones_proporcionales * salario
        monto_prima_proporcional = monto_vacaciones_proporcionales * prima_decimal
    
        total_finiquito = monto_sueldos + monto_vacaciones_pendientes + monto_prima_vacacional + monto_aguinaldo_proporcional + monto_vacaciones_proporcionales + monto_prima_proporcional

        indemnizacion = 0
        prima_antiguedad = 0

        if datos["motivo"] == "Despido" or (datos["motivo"] == "Renuncia" and anios_trabajados >= 15):
                salario_tope = min(salario, 497.86)
                prima_antiguedad = 12 * salario_tope * anios_trabajados

        if datos["motivo"] == "Despido":
                indemnizacion = 90 * salario_diario_integrado

        total_liquidacion = indemnizacion + prima_antiguedad
        gran_total_a_pagar = total_finiquito + total_liquidacion

        return {
                "sdi": salario_diario_integrado,
                "sueldos_pendientes": monto_sueldos,
                "vacaciones_pendientes": monto_vacaciones_pendientes,
                "prima_vacacional_pendiente": monto_prima_vacacional,
                "aguinaldo_proporcional": monto_aguinaldo_proporcional,
                "vacaciones_proporcionales": monto_vacaciones_proporcionales,
                "prima_proporcional": monto_prima_proporcional,
                "total_finiquito": total_finiquito,
                "indemnizacion": indemnizacion,
                "prima_antiguedad": prima_antiguedad,
                "total_liquidacion": total_liquidacion,
                "gran_total": gran_total_a_pagar
        }