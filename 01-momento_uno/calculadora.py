# Tkinter: programa para diseñar interfaces graficas.
from cgitb import text
from tkinter import *
from math import *

# Se crea una instancia de la clase Tk() llamada ventana.
ventana = Tk()
# Se le asigna un titulo a la ventana.
ventana.title("Calculadora.")
# Geometria, 400*600.
ventana.geometry("400x600")
# No se podran modificar las dimensiones.
ventana.resizable(False, False)
# Color de fondo.
ventana.configure(background="gray")
# Creacion de pantalla.
# Se define la variable de operador
operador = ""
texto_pantalla = StringVar()
def clear():
    global operador
    operador = ""
    texto_pantalla.set("0")

def click(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)
def resultado():
    global operador
    try: 
        r = str(eval(operador))
    except:
        r = "ERROR"
    texto_pantalla.set(r)



Pantalla = Entry(ventana, font = (" arial ", 20, " bold "), width = 22, borderwidth = 10, background = "light grey")
Pantalla.grid( row = 0, column = 0, columnspan = 4, padx = 20, pady = 20 )


# Creacion de botones.
color_boton = "gray"
ancho_boton = 10
alto_boton = 3

# Botones primera fila.
Boton0 = Button(ventana, text = " 0 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 1, column = 0, pady = 10 )
Boton1 = Button(ventana, text = " 1 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 1, column = 1, pady = 10 )
Boton2 = Button(ventana, text = " 2 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 1, column = 2, pady = 10 )
Boton3 = Button(ventana, text = " 3 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 1, column = 3, pady = 10 )

# Botones segunda fila.
Boton4 = Button(ventana, text = " 4 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 2, column = 0, pady = 10 )
Boton5 = Button(ventana, text = " 5 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 2, column = 1, pady = 10 )
Boton6 = Button(ventana, text = " 6 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 2, column = 2, pady = 10 )
Boton7 = Button(ventana, text = " 7 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 2, column = 3, pady = 10 )

# Botones tercera fila.
Boton8 = Button(ventana, text = " 8 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 3, column = 0, pady = 10 )
Boton9 = Button(ventana, text = " 9 ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 3, column = 1, pady = 10 )
BotonPi = Button(ventana, text = " π ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 3, column = 2, pady = 10 )
BotonPunto = Button(ventana, text = " . ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 3, column = 3, pady = 10 )

# Botones cuarta fila.
BotonSuma = Button(ventana, text = " + ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 4, column = 0, pady = 10 )
BotonResta = Button(ventana, text = " - ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 4, column = 1, pady = 10 )
BotonMultiplicacion = Button(ventana, text = " * ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 4, column = 2, pady = 10 )
BotonDivision = Button(ventana, text = " / ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 4, column = 3, pady = 10 )

# Botones quinta fila.
BotonRaiz = Button(ventana, text = " √ ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 5, column = 0, pady = 10 )
BotonClear = Button(ventana, text = " C ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 5, column = 1, pady = 10 )
BotonExponencial = Button(ventana, text = " EXP ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 5, column = 2, pady = 10 )
BotonIgual = Button(ventana, text = " = ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 5, column = 3, pady = 10 )

# Botones sexta fila.
BotonPizq = Button(ventana, text = " (", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 6, column = 0, pady = 10 )
BotonPder = Button(ventana, text = " ) ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 6, column = 1, pady = 10 )
BotonMod = Button(ventana, text = " % ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 6, column = 2, pady = 10 )
BotonLN = Button(ventana, text = " LN ", background = color_boton, width = ancho_boton, height = alto_boton).grid(row = 6, column = 3, pady = 10 )






# Metodo el cual debe ser siempre llamado cuando se crean interfaces graficas.
ventana.mainloop()