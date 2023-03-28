from tkinter import*
from tkinter import messagebox as MessageBox
import time
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from tkinter import colorchooser as ColorChooser

pygame.init()

root = Tk()
root.title("ALARMA") #Titulo de la raiz
root.resizable(0,0)

#Menu
miMenu = Menu(root)
root.config(menu = miMenu)

#Metodo
def clock():
    horas = time.strftime("%H")
    minutos = time.strftime("%M")
    segundos = time.strftime("%S")

    horaLocal = horas + " : " + minutos + " : " + segundos

    miEtiqueta2.config(text=horaLocal)
    miEtiqueta2.after(1000, clock)

    global horaDefinida
    horaDefinida = tiempoA.get() + " : " + tiempoB.get() + " : " + "00"

    if horaLocal == horaDefinida:
        Song()
        color1()
        mostrarInfo1()
        tiempoA.set("00")
        tiempoB.set("00")

def mostrarInfo1():
    MessageBox.showinfo("Informacion", "Es hora")
    miEtiqueta1.config(text="00 : 00 : 00")

def mostrarInfo2():
    miEtiqueta1.config(text=horaDefinida)
    MessageBox.showinfo("Informacion", "Alarma establecida correctamente")
    
def Song():
    print(cancion)
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(-1)

def Song1():
    global cancion
    cancion = "Morning Flower  Tono de Alarma Samsung.mp3"
    MessageBox.showinfo("Informacion", "Tono establecido correctamente: Morning Flower")
    pygame.mixer.music.load(cancion)

def Song2():
    global cancion
    cancion = "Oxygen  Tono de Alarma Motorola.mp3"
    MessageBox.showinfo("Informacion", "Tono establecido correctamente: Oxygen")
    pygame.mixer.music.load(cancion)

def Song3():
    global cancion
    cancion = "Canto del gallo.mp3"
    MessageBox.showinfo("Informacion", "Tono establecido correctamente: Canto de gallo")
    pygame.mixer.music.load(cancion)

def Song4():
    global cancion
    cancion = "iPhone.mp3"
    MessageBox.showinfo("Informacion", "Tono establecido correctamente: iPhone")
    pygame.mixer.music.load(cancion)

def Song5():
    global cancion
    cancion = "Bom bom.mp3"
    MessageBox.showinfo("Informacion", "Tono establecido correctamente: Bom bom")
    pygame.mixer.music.load(cancion)

def changeColor():
    otroColor = ColorChooser.askcolor(title="Selecciona un color")
    ventana.config(bg=otroColor[1])
    ventana.config(bg=otroColor[1])
    titulo1.config(bg=otroColor[1])
    titulo2.config(bg=otroColor[1])
    horasx.config(bg=otroColor[1])
    minutosx.config(bg=otroColor[1])
    titulo3.config(bg=otroColor[1])
    titulo4.config(bg=otroColor[1])
    titulo5.config(bg=otroColor[1])
    MessageBox.showinfo("Informacion", "Color establecido correctamente")

def stopAlarma():
    pygame.mixer.music.stop()
    MessageBox.showinfo("Informacion", "Alarma detenida correctamente")
    ventana.config(bg=otroColor[1])
    titulo1.config(bg=otroColor[1])
    titulo2.config(bg=otroColor[1])
    horasx.config(bg=otroColor[1])
    minutosx.config(bg=otroColor[1])
    titulo3.config(bg=otroColor[1])
    titulo4.config(bg=otroColor[1])
    titulo5.config(bg=otroColor[1])

def color1():
    ventana.config(bg="#F39C12")
    titulo1.config(bg="#F39C12")
    titulo2.config(bg="#F39C12")
    horasx.config(bg="#F39C12")
    minutosx.config(bg="#F39C12")
    titulo3.config(bg="#F39C12")
    titulo4.config(bg="#F39C12")
    titulo5.config(bg="#F39C12")
    ventana.after(700,color2)


def color2():
    ventana.config(bg="#3498DB")
    titulo1.config(bg="#3498DB")
    titulo2.config(bg="#3498DB")
    horasx.config(bg="#3498DB")
    minutosx.config(bg="#3498DB")
    titulo3.config(bg="#3498DB")
    titulo4.config(bg="#3498DB")
    titulo5.config(bg="#3498DB")
    ventana.after(700,color3)

def color3():
    ventana.config(bg="#F39C12")
    titulo1.config(bg="#F39C12")
    titulo2.config(bg="#F39C12")
    horasx.config(bg="#F39C12")
    minutosx.config(bg="#F39C12")
    titulo3.config(bg="#F39C12")
    titulo4.config(bg="#F39C12")
    titulo5.config(bg="#F39C12")
    ventana.after(700,color4)

def color4():
    ventana.config(bg="#3498DB")
    titulo1.config(bg="#3498DB")
    titulo2.config(bg="#3498DB")
    horasx.config(bg="#3498DB")
    minutosx.config(bg="#3498DB")
    titulo3.config(bg="#3498DB")
    titulo4.config(bg="#3498DB")
    titulo5.config(bg="#3498DB")
    ventana.after(700,color5)

def color5():
    ventana.config(bg="#F39C12")
    titulo1.config(bg="#F39C12")
    titulo2.config(bg="#F39C12")
    horasx.config(bg="#F39C12")
    minutosx.config(bg="#F39C12")
    titulo3.config(bg="#F39C12")
    titulo4.config(bg="#F39C12")
    titulo5.config(bg="#F39C12")
    ventana.after(700,color6)

def color6():
    ventana.config(bg="#3498DB")
    titulo1.config(bg="#3498DB")
    titulo2.config(bg="#3498DB")
    horasx.config(bg="#3498DB")
    minutosx.config(bg="#3498DB")
    titulo3.config(bg="#3498DB")
    titulo4.config(bg="#3498DB")
    titulo5.config(bg="#3498DB")
    ventana.after(700,color7)

def color7():
    ventana.config(bg="#F39C12")
    titulo1.config(bg="#F39C12")
    titulo2.config(bg="#F39C12")
    horasx.config(bg="#F39C12")
    minutosx.config(bg="#F39C12")
    titulo3.config(bg="#F39C12")
    titulo4.config(bg="#F39C12")
    titulo5.config(bg="#F39C12")
    ventana.after(700,color8)

def color8():
    ventana.config(bg="#3498DB")
    titulo1.config(bg="#3498DB")
    titulo2.config(bg="#3498DB")
    horasx.config(bg="#3498DB")
    minutosx.config(bg="#3498DB")
    titulo3.config(bg="#3498DB")
    titulo4.config(bg="#3498DB")
    titulo5.config(bg="#3498DB")
    ventana.after(700,color9)

def color9():
    ventana.config(bg="#F39C12")
    titulo1.config(bg="#F39C12")
    titulo2.config(bg="#F39C12")
    horasx.config(bg="#F39C12")
    minutosx.config(bg="#F39C12")
    titulo3.config(bg="#F39C12")
    titulo4.config(bg="#F39C12")
    titulo5.config(bg="#F39C12")
    ventana.after(700,color10)

def color10():
    ventana.config(bg="#3498DB")
    titulo1.config(bg="#3498DB")
    titulo2.config(bg="#3498DB")
    horasx.config(bg="#3498DB")
    minutosx.config(bg="#3498DB")
    titulo3.config(bg="#3498DB")
    titulo4.config(bg="#3498DB")
    titulo5.config(bg="#3498DB")
    ventana.after(700, color11)

def color11():
    ventana.config(bg=otroColor[1])
    titulo1.config(bg=otroColor[1])
    titulo2.config(bg=otroColor[1])
    horasx.config(bg=otroColor[1])
    minutosx.config(bg=otroColor[1])
    titulo3.config(bg=otroColor[1])
    titulo4.config(bg=otroColor[1])
    titulo5.config(bg=otroColor[1])

#variables
tiempoA = StringVar()
tiempoB = StringVar()

tiempoA.set("00")
tiempoB.set("00")

otroColor = ["0","#F4D03F"]

cancion = "Morning Flower  Tono de Alarma Samsung.mp3"

ventana = Frame(root, bg=otroColor[1])
ventana.pack(fill="both", expand=1)

#Titulo de la ventana
titulo1 = Label(ventana, text="Alarma", font=("Roboto",30,"bold"), bg=otroColor[1])
titulo1.grid(row=1, column=1, columnspan=2, padx=20, pady=15)

titulo2 = Label(ventana, text="Agregar alarma", font=("Roboto",15,"bold"), bg=otroColor[1])
titulo2.grid(row=2, column=1, columnspan=2, padx=20, pady=10)

#Etiqueta 1
horasx = Label(ventana, text="H", font=("Roboto",15,"bold"), bg=otroColor[1])
horasx.grid(row=3, column=1, padx=10, pady=5)
textoHoras = Entry(ventana, font=("Roboto",15), textvariable=tiempoA).grid(row=3, column=2, padx=10, pady=5)

#Etiqueta 2
minutosx = Label(ventana, text="M", font=("Roboto",15,"bold"), bg=otroColor[1])
minutosx.grid(row=4, column=1)
textoMinutos = Entry(ventana, font=("Roboto",15), textvariable=tiempoB).grid(row=4, column=2, padx=10, pady=5)

miEtiqueta1 = Label(ventana, text="00 : 00 : 00", font=("Roboto", 20))
miEtiqueta1.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

#Salto 1
titulo3 = Label(ventana, text="-------------------------------------------------------", font=("Roboto",10,"bold"), bg=otroColor[1])
titulo3.grid(row=6, column=1, columnspan=2)

#Subtitulo de la ventana
titulo4 = Label(ventana, text="Reloj", font=("Roboto",15,"bold"), bg=otroColor[1])
titulo4.grid(row=7, column=1, columnspan=2, padx=20, pady=10)

miEtiqueta2 = Label(ventana, text="", font=("Roboto", 20))
miEtiqueta2.grid(row=8, column=1, columnspan=2)

clock()

#Salto 2
titulo5 = Label(ventana, text="-------------------------------------------------------", font=("Roboto",10,"bold"), bg=otroColor[1])
titulo5.grid(row=9, column=1, columnspan=2)

#Boton Set alarma
boton = Button(ventana, text="Set alarma", font=("Roboto",15), command=mostrarInfo2).grid(row=10, column=1, columnspan=2, padx=20, pady=5)

#Boton Parar alarma
boton = Button(ventana, text="Detener alarma", font=("Roboto",15), command=stopAlarma).grid(row=11, column=1, columnspan=2, padx=20, pady=10)

#Menu configuraciones
#Crear los submenus
configMenu1 = Menu(miMenu, tearoff=0)
configMenu2 = Menu(miMenu, tearoff=0)

#mostrar los submenus
miMenu.add_cascade(label="Colores", menu=configMenu1)
miMenu.add_cascade(label="Tonos", menu=configMenu2)

#agregar las opciones a los submenus
#herramientas archivo
configMenu1.add_command(label="Cambiar Color Fondo", command=changeColor)
configMenu2.add_command(label="Morning Flower", command=Song1)
configMenu2.add_command(label="Oxygen", command=Song2)
configMenu2.add_command(label="Canto de gallo", command=Song3)
configMenu2.add_command(label="iPhone", command=Song4)
configMenu2.add_command(label="Bom bom", command=Song5)


root.mainloop()