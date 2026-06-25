import customtkinter as ctk 
from tkinter import ttk 
from tkcalendar import DateEntry
from calculos import calcular

def ejecutar_calculo():
    datos = {
        "motivo" : motivo.get(), 
        "ingreso" : ingreso.get(),
        "baja" : baja.get(),
        "dias_aguinaldo" : dias_aguinaldo.get(),
        "prima" : prima.get(),
        "vacaciones" : vacaciones.get(),
        "v_p" :  v_p.get(),
        "salario_diario" :  salario_diario.get(),
        "s_p" : s_p.get()
    }
    
    res = calcular(datos) 
    
    texto_resultado = (
        f"--- DESGLOSE DE CONCEPTOS ---\n\n"
        f"Salario Diario Integrado (SDI): ${res['sdi']:.2f}\n"
        f"Aguinaldo Proporcional: ${res['aguinaldo_proporcional']:.2f}\n"
        f"Vacaciones Proporcionales: ${res['vacaciones_proporcionales']:.2f}\n"
        f"Prima Vacacional Proporcional: ${res['prima_proporcional']:.2f}\n"
        f"Pendientes (Sueldos/Vacaciones): ${res['sueldos_pendientes'] + res['vacaciones_pendientes'] + res['prima_vacacional_pendiente']:.2f}\n\n"
        f"TOTAL FINIQUITO: ${res['total_finiquito']:.2f}\n"
        f"----------------------------------------\n"
        f"Indemnización (90 días): ${res['indemnizacion']:.2f}\n"
        f"Prima de Antigüedad: ${res['prima_antiguedad']:.2f}\n\n"
        f"TOTAL LIQUIDACIÓN: ${res['total_liquidacion']:.2f}\n"
        f"========================\n"
        f"GRAN TOTAL A RECIBIR: ${res['gran_total']:.2f}"
    )
    label_resultado.configure(text=texto_resultado)

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue") 

root = ctk.CTk() 
root.geometry("1100x700") 

titulo = ctk.CTkLabel(root, text="Sistema para el cálculo de finiquitos", font=("Arial", 30, "bold"))
titulo.pack(pady=15)

contenedor_principal = ctk.CTkFrame(root, fg_color="transparent")
contenedor_principal.pack(fill="both", expand=True, padx=20, pady=5)

contenedor_principal.columnconfigure(0, weight=1)
contenedor_principal.columnconfigure(1, weight=1)
contenedor_principal.rowconfigure(0, weight=1)

frame_izquierdo = ctk.CTkFrame(contenedor_principal)
frame_izquierdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame_derecho = ctk.CTkFrame(contenedor_principal)
frame_derecho.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

label_motivo = ctk.CTkLabel(frame_izquierdo, text="Motivo de la baja", font=("Arial", 12))
label_motivo.pack(pady=(10, 0))

motivo = ctk.CTkComboBox(frame_izquierdo, values=["Renuncia", "Despido"], width=250)
motivo.pack(pady=5)

label_ingreso = ctk.CTkLabel(frame_izquierdo, text="Fecha de ingreso", font=("Arial", 12))
label_ingreso.pack(pady=(5, 0))

ingreso = DateEntry(
    frame_izquierdo, width=15, background='#2b2b2b', foreground='white',
    headersbackground='#1f1f1f', headersforeground='white',
    selectbackground='#1f538d', selectforeground='white', date_pattern='dd/mm/yyyy'
)
ingreso.pack(pady=5)

label_baja = ctk.CTkLabel(frame_izquierdo, text="Fecha de baja", font=("Arial", 12))
label_baja.pack(pady=(5, 0))

baja = DateEntry(
    frame_izquierdo, width=15, background='#2b2b2b', foreground='white',
    headersbackground='#1f1f1f', headersforeground='white',
    selectbackground='#1f538d', selectforeground='white', date_pattern='dd/mm/yyyy'
)
baja.pack(pady=5)

dias_aguinaldo = ctk.CTkEntry(frame_izquierdo, placeholder_text="Días de aguinaldo", width=250)
dias_aguinaldo.pack(pady=5)

prima = ctk.CTkEntry(frame_izquierdo, placeholder_text="Prima Vacacional", width=250)
prima.pack(pady=5)

vacaciones = ctk.CTkEntry(frame_izquierdo, placeholder_text="Días de vacaciones por año", width=250)
vacaciones.pack(pady=5)

v_p = ctk.CTkEntry(frame_izquierdo, placeholder_text="Días de vacaciones pendientes", width=250)
v_p.pack(pady=5)

salario_diario = ctk.CTkEntry(frame_izquierdo, placeholder_text="Salario diario", width=250)
salario_diario.pack(pady=5)

s_p = ctk.CTkEntry(frame_izquierdo, placeholder_text="Días de salario pendiente", width=250)
s_p.pack(pady=5)

boton = ctk.CTkButton(frame_izquierdo, text="CALCULAR", command=ejecutar_calculo, width=250)
boton.pack(pady=15)

titulo_resultados = ctk.CTkLabel(frame_derecho, text="Resultados del Cálculo", font=("Arial", 18, "bold"))
titulo_resultados.pack(pady=20)

label_resultado = ctk.CTkLabel(frame_derecho, text="Total Finiquito: $0.00\nTotal Liquidación: $0.00", font=("Arial", 14), justify="left")
label_resultado.pack(pady=20, padx=20)

root.mainloop()