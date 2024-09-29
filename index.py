import tkinter as tk
from tkinter import messagebox, scrolledtext
import matplotlib.pyplot as plt
from ascenso_colimas import ejecutar_asencso
from a_stocástico import ejecutar_ascenso_est
from temple_simulado import ejecutar_temple
from acenso_colimas_reinicio import ejecutar_reinicio_aleatorio_colinas
# Configuración de la interfaz gráfica
BG_COLOR = "#000000"  
FG_COLOR = "#FFFFFF" 
BUTTON_COLOR = "#333333"  
BUTTON_TEXT_COLOR = "#FFFFFF"  
FONT_TITLE = ("Helvetica", 18, "bold")
FONT_TEXT = ("Helvetica", 14)
FONT_BUTTON = ("Helvetica", 14, "bold")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Menú de Algoritmos de Búsqueda - 8 Reinas")
ventana.configure(bg=BG_COLOR)
ventana.geometry("1200x700")

# Etiqueta principal
etiqueta = tk.Label(ventana, text="Seleccione un algoritmo para resolver el problema de las 8 reinas:", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TITLE)
etiqueta.grid(row=0, column=0, columnspan=4, pady=20)

# Output de texto con scroll
output_text = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=FONT_TEXT, bg=BG_COLOR, fg=FG_COLOR, bd=0)
output_text.grid(row=1, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
output_text.tag_configure("center", justify="center")

# Redirigir la consola al widget de texto
class RedirigirConsola:
    def __init__(self, widget):
        self.widget = widget

    def write(self, texto):
        self.widget.insert(tk.END, texto)
        self.widget.tag_add("center", "1.0", "end")
        self.widget.see(tk.END)

    def flush(self):
        pass

import sys
sys.stdout = RedirigirConsola(output_text)

# Funciones de ejecución para cada algoritmo
def ejecutar_ascenso_estocastico():
    output_text.delete(1.0, tk.END)
    ejecutar_ascenso_est()  # El algoritmo se encarga de graficar internamente
def ejecutar_ascenso_colinas():
    output_text.delete(1.0, tk.END)
    ejecutar_asencso()  # El algoritmo se encarga de graficar internamente

def ejecutar_temple_simulado():
    output_text.delete(1.0, tk.END)
    ejecutar_temple()  # El algoritmo se encarga de graficar internamente

def ejecutar_reinicio_aleatorio():
    ejecutar_reinicio_aleatorio_colinas()  # El algoritmo se encarga de graficar internamente

def ejecutar_reinicio_aleatorio_es():
    messagebox.showinfo("Reinicio Aleatorio", "¡Funcionalidad en desarrollo!")
# Crear botones para cada algoritmo
def crear_boton_moderno(texto, comando):
    return tk.Button(ventana, text=texto, command=comando, font=FONT_BUTTON, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, bd=0, height=2, activebackground="#555555", activeforeground=BUTTON_TEXT_COLOR)

# Pasar la referencia de la función sin paréntesis
boton_ascenso_estocastico = crear_boton_moderno("Ascenso Estocástico", ejecutar_ascenso_estocastico)
boton_ascenso_estocastico.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

boton_ascenso_colinas = crear_boton_moderno("Ascenso de Colinas", ejecutar_ascenso_colinas)
boton_ascenso_colinas.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

boton_temple_simulado = crear_boton_moderno("Temple Simulado", ejecutar_temple_simulado)
boton_temple_simulado.grid(row=2, column=2, padx=20, pady=10, sticky="ew")

boton_reinicio_aleatorio = crear_boton_moderno("Reinicio Aleatorio ascenso colinas", ejecutar_reinicio_aleatorio)
boton_reinicio_aleatorio.grid(row=3, column=0, padx=20, pady=10, sticky="ew")  # Ubicación en la fila 3

boton_reinicio_aleatorio = crear_boton_moderno("Reinicio Aleatorio ascenso colinas estocastico", ejecutar_reinicio_aleatorio_es)
boton_reinicio_aleatorio.grid(row=3, column=2, padx=20, pady=10, sticky="ew")  # Ubicación en la fila 3
# Configurar el tamaño de la cuadrícula y ejecutar la ventana
ventana.grid_rowconfigure(1, weight=1) 
ventana.grid_columnconfigure((0, 1, 2, 3), weight=1)  
ventana.state("zoomed")
ventana.mainloop()
