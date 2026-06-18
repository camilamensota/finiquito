import customtkinter as ctk #as sirve para abreviarlo pq es mucho texto ajja
from tkcalendar import DateEntry
from calculos import calcular_finiquito

#FUNCION PARA TOMAR LOS DATOS REGISTRADOS
def ejecutar_calculo():
    datos = {
        "motivo" : motivo.get(), #para obtener los datos en una funcion, cuando el usuario le de clic en CALCULAR, la funcion ejecutar_calculo leera lo que se escribió
        #la libreria CTK almacena la información metida dentro de los objetos (como ctkEntry) y usamos el método .get() para poder extraer los datos que se ingresaron
        # "motivo" se refiere a la llave o la etiqueta y motivo.get( ) extrae el valor de la variable y todo lo guardamos dentro del diccionario datos
        "ingreso" : ingreso.get(),
        "baja" : baja.get(),
        "dias_aguinaldo" : dias_aguinaldo.get(),
        "prima" : prima.get(),
        "vacaciones" : vacaciones.get(),
        "v_p" :  v_p.get(),
        "salario_diario" :  salario_diario.get(),
        "s_p" : s_p.get()
    }
    resultado= ejecutar_calculo(datos)
    print(resultado)

ctk.set_appearance_mode("System") #Establece que la aplicación se quede con el modo de color que tenga el usuario puesto oscuro/claro
ctk.set_default_color_theme("blue") #Temsa de color, será azul en este caso

#ventanas
root = ctk.CTk() #crea la ventana principal 
root.geometry("1000x980") #Le estamos definiendo un tamaño a la ventana 
#titulo
titulo = ctk.CTkLabel(
    root,
    text="Sistema para el cálculo de finiquitos",
    font=("Arial",30)
)
titulo.pack(
    pady=30
    )

#INGRESO DE DATOS
label_motivo = ctk.CTkLabel(
    root, 
    text="Motivo de la baja", 
    font=("Arial", 12)
)
label_motivo.pack(pady=(10, 0))

#motivo de la baja
motivo=ctk.CTkComboBox(
    root,
    values=["Renuncia","Despido"]
)
motivo.pack(
    pady=10
)

label_ingreso = ctk.CTkLabel(
    root,
    text="Fecha de ingreso",
    font=("Arial", 12)
)
label_ingreso.pack(
    pady=(5, 0)
)
#fecha de ingreso
ingreso = DateEntry(
    root,
    width=15,
    background='#2b2b2b',
    foreground='white',
    headersbackground='#1f1f1f',
    headersforeground='white',
    selectbackground='#1f538d',
    selectforeground='white',
    date_pattern='dd/mm/yyyy'
)
ingreso.pack(pady=(10, 0))

label_baja=ctk.CTkLabel(
    root, 
    text="Fecha de baja",
    font=("Arial", 12)
)
label_baja.pack(
    pady=(5, 0)
)
#fecha de baja
baja = DateEntry(
    root,
    width=15,
    background='#2b2b2b',
    foreground='white',
    headersbackground='#1f1f1f',
    headersforeground='white',
    selectbackground='#1f538d',
    selectforeground='white',
    date_pattern='dd/mm/yyyy'
)
baja.pack(pady=10)

#dias de aguinaldo
dias_aguinaldo=ctk.CTkEntry(
    root,
    placeholder_text="Días de aguinaldo"
)
dias_aguinaldo.pack(
    pady=10
)

#prima vacacional %
prima=ctk.CTkEntry(
    root,
    placeholder_text="Prima Vacacional"
)
prima.pack(
    pady=10
)

#días de vacaciones por año
vacaciones=ctk.CTkEntry(
    root,
    placeholder_text="Días de vacaciones por año"
)
vacaciones.pack(
    pady=10
)

#días de vacaciones pendientes
v_p=ctk.CTkEntry(
    root,
    placeholder_text="Días de vacaciones pendientes"
)
v_p.pack(
    pady=10
)

#salario diario
salario_diario=ctk.CTkEntry(
    root,
    placeholder_text="Salario diario"
)
salario_diario.pack(
    pady=10
)

#Días de salario pendiente
s_p=ctk.CTkEntry(
    root,
    placeholder_text="Días de salario pendiente"
)

#boton
boton = ctk.CTkButton(
    root,
    text="CALCULAR",
    command=ejecutar_calculo
)
boton.pack(pady=20)


root.mainloop()#ejecuta la aplicación