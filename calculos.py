from datetime import datetime

def calcular(datos):
        salario=float(datos["salario_diario"])
        dias_vacaciones_pendientes= int(datos["v_p"]) if datos ["v_p"] else 0 #operador ternario, es un if-else en una sola linea, si los datos(descritos como enteros) existen, 
        #entoces se usan, pero si no solo manda un 0 en caso de no ser válido o simplemente no poner nada
        dias_salario_pendiente= int(datos["s_p"]) if datos ["s_p"] else 0

        #para la prima dice que si sus datos los pone en flotante, que esta bien asi se deje, pero si son mayores a 1, o en entero que se divida entre 100, para asi tener el porcentaje
        #solo para multiplicarlo
        if datos["prima"]:
                valor = float(datos["prima"])
                prima_decimal= valor / 100 if valor >= 1 else valor
        else:
                prima_decimal= 0.25

        #calcula lo pendiente
        monto_sueldos=dias_salario_pendiente * salario
        monto_vacaciones_pendientes= dias_vacaciones_pendientes * salario
        monto_prima_vacacional=prima_decimal*monto_vacaciones_pendientes

        #calcula lo proporcional al año
        fecha_ingreso=datetime.strptime(datos["ingreso"], "%d/%m/%Y")
        fecha_baja=datetime.strptime(datos["baja"], "%d/%m/%Y")
        anio_baja=fecha_baja.year
        inicio_anio_baja=datetime(anio_baja, 1, 1)

        if fecha_ingreso > inicio_anio_baja:
                fecha_inicio_calculo = fecha_ingreso
        else:
                fecha_inicio_calculo = inicio_anio_baja
        
        dias_del_anio = (fecha_baja - fecha_inicio_calculo).days + 1

        dias_aguinaldo_anual = int(datos["dias_aguinaldo"]) if datos["dias_aguinaldo"] else 15
        dias_proporcion_aguinaldo = (dias_aguinaldo_anual / 365) * dias_del_anio
        monto_aguinaldo_proporcional = dias_proporcion_aguinaldo * salario

        dias_vacaciones_anual = int(datos["vacaciones"]) if datos["vacaciones"] else 12
        factor_vacaciones = dias_vacaciones_anual / 365
        vacaciones_proporcionales = factor_vacaciones * dias_del_anio
        monto_vacaciones_proporcionales = vacaciones_proporcionales * salario
        monto_prima_proporcional = monto_vacaciones_proporcionales * prima_decimal
    
        total_liquidacion += monto_aguinaldo_proporcional + monto_vacaciones_proporcionales + monto_prima_proporcional
        total_finiquito = monto_sueldos + monto_vacaciones_pendientes + monto_prima_vacacional

        vacaciones_proporcionales = factor_vacaciones * dias_del_anio

        return total_finiquito, total_liquidacion

