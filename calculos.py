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

        monto_sueldos=dias_salario_pendiente * salario
        monto_vacaciones_pendientes= dias_vacaciones_pendientes * salario
        monto_prima_vacacional=prima_decimal*monto_vacaciones_pendientes

        total_finiquito=monto_sueldos=dias_salario_pendiente + monto_vacaciones_pendientes


