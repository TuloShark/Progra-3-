#================================================IMPORTS================================================#

import tkinter
import random
import pickle
from tkinter import messagebox

#===============================================VARIABLES===============================================#

dificultad = "FACIL"
control_reloj = "Si"
panel = "Derecha"
numero_manejado = 0
botton_num_1 = 0
botton_num_2 = 0
botton_num_3 = 0
botton_num_4 = 0
botton_num_5 = 0
casilla1_1 = 0
casilla2_1 = 0
casilla3_1 = 0
casilla4_1 = 0
casilla5_1 = 0
casilla1_2 = 0
casilla2_2 = 0
casilla3_2 = 0
casilla4_2 = 0
casilla5_2 = 0
casilla1_3 = 0
casilla2_3 = 0
casilla3_3 = 0
casilla4_3 = 0
casilla5_3 = 0
casilla1_4 = 0
casilla2_4 = 0
casilla3_4 = 0
casilla4_4 = 0
casilla5_4 = 0
casilla1_5 = 0
casilla2_5 = 0
casilla3_5 = 0
casilla4_5 = 0
casilla5_5 = 0
iniciar_activado = 0
hora_numero = 0
minuto_numero = 0
segundo_numero = 0
hora_terminado = 0
minuto_terminado = 0
segundo_terminado = 0
suerte = 0
desactivar = 0
ventana_jugar = 0
borrar = False
botton_pri_1 = 0
botton_pri_2 = 0
botton_pri_3 = 0
botton_pri_4 = 0
top_10_facil = []
top_10_medio = []
top_10_dificil = []
entrada_hora = 0
entrada_minuto = 0
entrada_segundo = 0
botton_timer = 0
jugador = 0
hora_si_terminado = 0
minuto_si_terminado = 0
segundo_si_terminado = 0
texto = 0

parada_final = 0

guardar_casilla1_1 = 0
guardar_casilla2_1 = 0
guardar_casilla3_1 = 0
guardar_casilla4_1 = 0
guardar_casilla5_1 = 0
guardar_casilla1_2 = 0
guardar_casilla2_2 = 0
guardar_casilla3_2 = 0
guardar_casilla4_2 = 0
guardar_casilla5_2 = 0
guardar_casilla1_3 = 0
guardar_casilla2_3 = 0
guardar_casilla3_3 = 0
guardar_casilla4_3 = 0
guardar_casilla5_3 = 0
guardar_casilla1_4 = 0
guardar_casilla2_4 = 0
guardar_casilla3_4 = 0
guardar_casilla4_4 = 0
guardar_casilla5_4 = 0
guardar_casilla1_5 = 0
guardar_casilla2_5 = 0
guardar_casilla3_5 = 0
guardar_casilla4_5 = 0
guardar_casilla5_5 = 0

guardar_dificultad = 0
guardar_control_reloj = 0
guardar_panel = 0
guardar_suerte = 0

guardar_hora = 0
guardar_minuto = 0
guardar_segundo = 0

juego_cargado = False

botton_guardar = 0
botton_cargar = 0

desplegar = 0

#================================================JUEGO 1================================================#

#=================================================FACIL=================================================#

def juego_facil_1(ventana_jugar):

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1

    global casilla1_2
    global casilla2_2
    global casilla3_2 
    global casilla4_2
    global casilla5_2

    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3

    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4

    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5

    casilla1_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_1)
    casilla1_1.place(x=127,y=150)
    casilla2_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_1)
    casilla2_1.place(x=197,y=150)
    casilla3_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_1)
    casilla3_1.place(x=267,y=150)
    casilla4_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_1)
    casilla4_1.place(x=337,y=150)
    casilla5_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_1)
    casilla5_1.place(x=407,y=150)

    casilla1_2 = tkinter.Button(ventana_jugar,height=2, width=5, text=1, command=numero_fijo)
    casilla1_2.place(x=127,y=215)
    casilla2_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_2)
    casilla2_2.place(x=197,y=215)
    casilla3_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_2)
    casilla3_2.place(x=267,y=215)
    casilla4_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_2)
    casilla4_2.place(x=337,y=215)
    casilla5_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_2)
    casilla5_2.place(x=407,y=215)

    casilla1_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_3)
    casilla1_3.place(x=127,y=280)
    casilla2_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_3)
    casilla2_3.place(x=197,y=280)
    casilla3_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_3)
    casilla3_3.place(x=267,y=280)
    casilla4_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_3)
    casilla4_3.place(x=337,y=280)
    casilla5_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_3)
    casilla5_3.place(x=407,y=280)

    casilla1_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_4)
    casilla1_4.place(x=127,y=345)
    casilla2_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_4)
    casilla2_4.place(x=197,y=345)
    casilla3_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_4)
    casilla3_4.place(x=267,y=345)
    casilla4_4 = tkinter.Button(ventana_jugar,height=2, width=5, text=4, command=numero_fijo)
    casilla4_4.place(x=337,y=345)
    casilla5_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_4)
    casilla5_4.place(x=407,y=345)

    casilla1_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_5)
    casilla1_5.place(x=127,y=410)
    casilla2_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_5)
    casilla2_5.place(x=197,y=410)
    casilla3_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_5)
    casilla3_5.place(x=267,y=410)
    casilla4_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_5)
    casilla4_5.place(x=337,y=410)
    casilla5_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_5)
    casilla5_5.place(x=407,y=410)
    
    label1 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=178, y=160)
    label2 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=160)
    label3 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=388, y=420)

    global juego_cargado

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5
    
    if juego_cargado == True:

        casilla1_1.config(text=guardar_casilla1_1)
        casilla2_1.config(text=guardar_casilla2_1)
        casilla3_1.config(text=guardar_casilla3_1)
        casilla4_1.config(text=guardar_casilla4_1)
        casilla5_1.config(text=guardar_casilla5_1)
        casilla1_2.config(text=guardar_casilla1_2)
        casilla2_2.config(text=guardar_casilla2_2)
        casilla3_2.config(text=guardar_casilla3_2)
        casilla4_2.config(text=guardar_casilla4_2)
        casilla5_2.config(text=guardar_casilla5_2)
        casilla1_3.config(text=guardar_casilla1_3)
        casilla2_3.config(text=guardar_casilla2_3)
        casilla3_3.config(text=guardar_casilla3_3)
        casilla4_3.config(text=guardar_casilla4_3)
        casilla5_3.config(text=guardar_casilla5_3)
        casilla1_4.config(text=guardar_casilla1_4)
        casilla2_4.config(text=guardar_casilla2_4)
        casilla3_4.config(text=guardar_casilla3_4)
        casilla4_4.config(text=guardar_casilla4_4)
        casilla5_4.config(text=guardar_casilla5_4)
        casilla1_5.config(text=guardar_casilla1_5)
        casilla2_5.config(text=guardar_casilla2_5)
        casilla3_5.config(text=guardar_casilla3_5)
        casilla4_5.config(text=guardar_casilla4_5)
        casilla5_5.config(text=guardar_casilla5_5)

def cambio1_1():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_1.config(text=numero_manejado)        
    texto1 = casilla1_1["text"]   
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla1_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_1)  

def cambio2_1():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_1.config(text=numero_manejado)        
    texto1 = casilla2_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla2_2["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla2_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_1)   
       
def cambio3_1():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_1.config(text=numero_manejado)        
    texto1 = casilla3_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla3_2["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_1)  
        
def cambio4_1():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_1.config(text=numero_manejado)        
    texto1 = casilla4_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla4_2["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]    
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_1)   
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_1)
        
def cambio5_1():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_1.config(text=numero_manejado)        
    texto1 = casilla5_1["text"]   
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla4_1["text"]
    texto6 = casilla5_2["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto5 != "":
        if texto1 > texto5:
            return menor(casilla5_1)           
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_1)
        
def cambio1_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_2.config(text=numero_manejado)        
    texto1 = casilla1_2["text"]   
    texto2 = casilla2_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_2)
        
def cambio2_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_2.config(text=numero_manejado)        
    texto1 = casilla2_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_2)
        
def cambio3_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_2.config(text=numero_manejado)
    texto1 = casilla3_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla2_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_2)
        
def cambio4_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_2.config(text=numero_manejado)
    texto1 = casilla4_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla2_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_2)
        
def cambio5_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_2.config(text=numero_manejado)
    texto1 = casilla5_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla2_2["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_2)
        
def cambio1_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_3.config(text=numero_manejado)
    texto1 = casilla1_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_3)

def cambio2_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_3.config(text=numero_manejado)
    texto1 = casilla2_3["text"]   
    texto2 = casilla1_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_3)
        
def cambio3_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_3.config(text=numero_manejado)
    texto1 = casilla3_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla1_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_3)
        
def cambio4_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_3.config(text=numero_manejado)
    texto1 = casilla4_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla1_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_3)
        
def cambio5_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_3.config(text=numero_manejado)
    texto1 = casilla5_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla1_3["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_3)
        
def cambio1_4():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_4.config(text=numero_manejado)
    texto1 = casilla1_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_4)
        
def cambio2_4():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_4.config(text=numero_manejado)
    texto1 = casilla2_4["text"]   
    texto2 = casilla1_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_4)
        
def cambio3_4():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_4.config(text=numero_manejado)
    texto1 = casilla3_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla1_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_4)
        
def cambio4_4():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_4.config(text=numero_manejado)
    texto1 = casilla4_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla1_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_4)
        
def cambio5_4():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_4.config(text=numero_manejado)
    texto1 = casilla5_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla1_4["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_4)
        
def cambio1_5():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_5.config(text=numero_manejado)
    texto1 = casilla1_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_4["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_5)
        
def cambio2_5():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_5.config(text=numero_manejado)
    texto1 = casilla2_5["text"]   
    texto2 = casilla1_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_4["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_5)
        
def cambio3_5():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_5.config(text=numero_manejado)
    texto1 = casilla3_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla1_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_4["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_5)
        
def cambio4_5():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_5.config(text=numero_manejado)
    texto1 = casilla4_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla1_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_4["text"]
    if texto5 != "":
        if texto1 > texto5:
            return menor(casilla4_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_5)
        
def cambio5_5():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_5.config(text=numero_manejado)
    texto1 = casilla5_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla1_5["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_4["text"]
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla5_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_5)

#================================================JUEGO 2================================================#

#=================================================FACIL=================================================#

def juego_facil_2(ventana_jugar):

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1

    global casilla1_2
    global casilla2_2
    global casilla3_2
    global casilla4_2
    global casilla5_2

    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3

    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4

    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5
    
    casilla1_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_1_2)
    casilla1_1.place(x=127,y=150)
    casilla2_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_1_2)
    casilla2_1.place(x=197,y=150)
    casilla3_1 = tkinter.Button(ventana_jugar,height=2, width=5, text=3, command=numero_fijo)
    casilla3_1.place(x=267,y=150)
    casilla4_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_1_2)
    casilla4_1.place(x=337,y=150)
    casilla5_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_1_2)
    casilla5_1.place(x=407,y=150)

    casilla1_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_2_2)
    casilla1_2.place(x=127,y=215)
    casilla2_2 = tkinter.Button(ventana_jugar,height=2, width=5, text=1, command=numero_fijo)
    casilla2_2.place(x=197,y=215)
    casilla3_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_2_2)
    casilla3_2.place(x=267,y=215)
    casilla4_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_2_2)
    casilla4_2.place(x=337,y=215)
    casilla5_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_2_2)
    casilla5_2.place(x=407,y=215)

    casilla1_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_3_2)
    casilla1_3.place(x=127,y=280)
    casilla2_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_3_2)
    casilla2_3.place(x=197,y=280)
    casilla3_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_3_2)
    casilla3_3.place(x=267,y=280)
    casilla4_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_3_2)
    casilla4_3.place(x=337,y=280)
    casilla5_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_3_2)
    casilla5_3.place(x=407,y=280)

    casilla1_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_4_2)
    casilla1_4.place(x=127,y=345)
    casilla2_4 = tkinter.Button(ventana_jugar,height=2, width=5, text=5, command=numero_fijo)
    casilla2_4.place(x=197,y=345)
    casilla3_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_4_2)
    casilla3_4.place(x=267,y=345)
    casilla4_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_4_2)
    casilla4_4.place(x=337,y=345)
    casilla5_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_4_2)
    casilla5_4.place(x=407,y=345)

    casilla1_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_5_2)
    casilla1_5.place(x=127,y=410)
    casilla2_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_5_2)
    casilla2_5.place(x=197,y=410)
    casilla3_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_5_2)
    casilla3_5.place(x=267,y=410)
    casilla4_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_5_2)
    casilla4_5.place(x=337,y=410)
    casilla5_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_5_2)
    casilla5_5.place(x=407,y=410)
    
    label1 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=178, y=160)
    label2 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=388, y=160)
    label3 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=420)
    label4 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=178, y=420)

    global juego_cargado

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5
    
    if juego_cargado == True:

        casilla1_1.config(text=guardar_casilla1_1)
        casilla2_1.config(text=guardar_casilla2_1)
        casilla3_1.config(text=guardar_casilla3_1)
        casilla4_1.config(text=guardar_casilla4_1)
        casilla5_1.config(text=guardar_casilla5_1)
        casilla1_2.config(text=guardar_casilla1_2)
        casilla2_2.config(text=guardar_casilla2_2)
        casilla3_2.config(text=guardar_casilla3_2)
        casilla4_2.config(text=guardar_casilla4_2)
        casilla5_2.config(text=guardar_casilla5_2)
        casilla1_3.config(text=guardar_casilla1_3)
        casilla2_3.config(text=guardar_casilla2_3)
        casilla3_3.config(text=guardar_casilla3_3)
        casilla4_3.config(text=guardar_casilla4_3)
        casilla5_3.config(text=guardar_casilla5_3)
        casilla1_4.config(text=guardar_casilla1_4)
        casilla2_4.config(text=guardar_casilla2_4)
        casilla3_4.config(text=guardar_casilla3_4)
        casilla4_4.config(text=guardar_casilla4_4)
        casilla5_4.config(text=guardar_casilla5_4)
        casilla1_5.config(text=guardar_casilla1_5)
        casilla2_5.config(text=guardar_casilla2_5)
        casilla3_5.config(text=guardar_casilla3_5)
        casilla4_5.config(text=guardar_casilla4_5)
        casilla5_5.config(text=guardar_casilla5_5)
    
def cambio1_1_2():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_1.config(text=numero_manejado)        
    texto1 = casilla1_1["text"]   
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla1_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_1)   

def cambio2_1_2():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_1.config(text=numero_manejado)        
    texto1 = casilla2_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla2_2["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla2_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_1)    
       
def cambio3_1_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_1.config(text=numero_manejado)        
    texto1 = casilla3_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla3_2["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_1)   
        
def cambio4_1_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_1.config(text=numero_manejado)        
    texto1 = casilla4_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla4_2["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]    
    if texto5 != "":
        if texto1 > texto5:
            return menor(casilla4_1)   
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_1)
        
def cambio5_1_2():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_1.config(text=numero_manejado)        
    texto1 = casilla5_1["text"]   
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla4_1["text"]
    texto6 = casilla5_2["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla5_1)           
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_1)
        
def cambio1_2_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_2.config(text=numero_manejado)        
    texto1 = casilla1_2["text"]   
    texto2 = casilla2_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_2)
        
def cambio2_2_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_2.config(text=numero_manejado)        
    texto1 = casilla2_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_2)
        
def cambio3_2_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_2.config(text=numero_manejado)
    texto1 = casilla3_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla2_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_2)
        
def cambio4_2_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_2.config(text=numero_manejado)
    texto1 = casilla4_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla2_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_2)
        
def cambio5_2_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_2.config(text=numero_manejado)
    texto1 = casilla5_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla2_2["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_2)
        
def cambio1_3_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_3.config(text=numero_manejado)
    texto1 = casilla1_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_3)
        
def cambio2_3_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_3.config(text=numero_manejado)
    texto1 = casilla2_3["text"]   
    texto2 = casilla1_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_3)
        
def cambio3_3_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_3.config(text=numero_manejado)
    texto1 = casilla3_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla1_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_3)
        
def cambio4_3_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_3.config(text=numero_manejado)
    texto1 = casilla4_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla1_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_3)
        
def cambio5_3_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_3.config(text=numero_manejado)
    texto1 = casilla5_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla1_3["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_3)
        
def cambio1_4_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_4.config(text=numero_manejado)
    texto1 = casilla1_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_4)
        
def cambio2_4_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_4.config(text=numero_manejado)
    texto1 = casilla2_4["text"]   
    texto2 = casilla1_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_4)
        
def cambio3_4_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_4.config(text=numero_manejado)
    texto1 = casilla3_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla1_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_4)
        
def cambio4_4_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_4.config(text=numero_manejado)
    texto1 = casilla4_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla1_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_4)
        
def cambio5_4_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_4.config(text=numero_manejado)
    texto1 = casilla5_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla1_4["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_4)
        
def cambio1_5_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_5.config(text=numero_manejado)
    texto1 = casilla1_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla1_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_5)
        
def cambio2_5_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_5.config(text=numero_manejado)
    texto1 = casilla2_5["text"]   
    texto2 = casilla1_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_4["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla2_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_5)
        
def cambio3_5_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_5.config(text=numero_manejado)
    texto1 = casilla3_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla1_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_4["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_5)
        
def cambio4_5_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_5.config(text=numero_manejado)
    texto1 = casilla4_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla1_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_4["text"]
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_5)
        
def cambio5_5_2():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_5.config(text=numero_manejado)
    texto1 = casilla5_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla1_5["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_4["text"]
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla5_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_5)

#================================================JUEGO 3================================================#

#=================================================FACIL=================================================#

def juego_facil_3(ventana_jugar):

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1

    global casilla1_2
    global casilla2_2
    global casilla3_2
    global casilla4_2
    global casilla5_2

    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3

    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4

    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5
    
    casilla1_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_1_3)
    casilla1_1.place(x=127,y=150)
    casilla2_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_1_3)
    casilla2_1.place(x=197,y=150)
    casilla3_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_1_3)
    casilla3_1.place(x=267,y=150)
    casilla4_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_1_3)
    casilla4_1.place(x=337,y=150)
    casilla5_1 = tkinter.Button(ventana_jugar,height=2, width=5, text=2, command=numero_fijo)
    casilla5_1.place(x=407,y=150)

    casilla1_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_2_3)
    casilla1_2.place(x=127,y=215)
    casilla2_2 = tkinter.Button(ventana_jugar,height=2, width=5, text=2, command=numero_fijo)
    casilla2_2.place(x=197,y=215)
    casilla3_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_2_3)
    casilla3_2.place(x=267,y=215)
    casilla4_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_2_3)
    casilla4_2.place(x=337,y=215)
    casilla5_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_2_3)
    casilla5_2.place(x=407,y=215)

    casilla1_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_3_3)
    casilla1_3.place(x=127,y=280)
    casilla2_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_3_3)
    casilla2_3.place(x=197,y=280)
    casilla3_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_3_3)
    casilla3_3.place(x=267,y=280)
    casilla4_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_3_3)
    casilla4_3.place(x=337,y=280)
    casilla5_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_3_3)
    casilla5_3.place(x=407,y=280)

    casilla1_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_4_3)
    casilla1_4.place(x=127,y=345)
    casilla2_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_4_3)
    casilla2_4.place(x=197,y=345)
    casilla3_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_4_3)
    casilla3_4.place(x=267,y=345)
    casilla4_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_4_3)
    casilla4_4.place(x=337,y=345)
    casilla5_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_4_3)
    casilla5_4.place(x=407,y=345)

    casilla1_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_5_3)
    casilla1_5.place(x=127,y=410)
    casilla2_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_5_3)
    casilla2_5.place(x=197,y=410)
    casilla3_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_5_3)
    casilla3_5.place(x=267,y=410)
    casilla4_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_5_3)
    casilla4_5.place(x=337,y=410)
    casilla5_5 = tkinter.Button(ventana_jugar,height=2, width=5, text=4, command=numero_fijo)
    casilla5_5.place(x=407,y=410)
    
    label1 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=178, y=290)
    label2 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=247, y=290)
    label3 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=290)
    label4 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=290)

    global juego_cargado

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5
    
    if juego_cargado == True:

        casilla1_1.config(text=guardar_casilla1_1)
        casilla2_1.config(text=guardar_casilla2_1)
        casilla3_1.config(text=guardar_casilla3_1)
        casilla4_1.config(text=guardar_casilla4_1)
        casilla5_1.config(text=guardar_casilla5_1)
        casilla1_2.config(text=guardar_casilla1_2)
        casilla2_2.config(text=guardar_casilla2_2)
        casilla3_2.config(text=guardar_casilla3_2)
        casilla4_2.config(text=guardar_casilla4_2)
        casilla5_2.config(text=guardar_casilla5_2)
        casilla1_3.config(text=guardar_casilla1_3)
        casilla2_3.config(text=guardar_casilla2_3)
        casilla3_3.config(text=guardar_casilla3_3)
        casilla4_3.config(text=guardar_casilla4_3)
        casilla5_3.config(text=guardar_casilla5_3)
        casilla1_4.config(text=guardar_casilla1_4)
        casilla2_4.config(text=guardar_casilla2_4)
        casilla3_4.config(text=guardar_casilla3_4)
        casilla4_4.config(text=guardar_casilla4_4)
        casilla5_4.config(text=guardar_casilla5_4)
        casilla1_5.config(text=guardar_casilla1_5)
        casilla2_5.config(text=guardar_casilla2_5)
        casilla3_5.config(text=guardar_casilla3_5)
        casilla4_5.config(text=guardar_casilla4_5)
        casilla5_5.config(text=guardar_casilla5_5)
    
def cambio1_1_3():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_1.config(text=numero_manejado)        
    texto1 = casilla1_1["text"]   
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_1)

def cambio2_1_3():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_1.config(text=numero_manejado)        
    texto1 = casilla2_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla2_2["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_1)    
       
def cambio3_1_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_1.config(text=numero_manejado)        
    texto1 = casilla3_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla3_2["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_1)  
        
def cambio4_1_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_1.config(text=numero_manejado)        
    texto1 = casilla4_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla4_2["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]     
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_1)
        
def cambio5_1_3():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_1.config(text=numero_manejado)        
    texto1 = casilla5_1["text"]   
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla4_1["text"]
    texto6 = casilla5_2["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]         
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_1)
        
def cambio1_2_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_2.config(text=numero_manejado)        
    texto1 = casilla1_2["text"]   
    texto2 = casilla2_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_2)
        
def cambio2_2_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_2.config(text=numero_manejado)        
    texto1 = casilla2_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_2)
        
def cambio3_2_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_2.config(text=numero_manejado)
    texto1 = casilla3_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla2_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_2)
        
def cambio4_2_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_2.config(text=numero_manejado)
    texto1 = casilla4_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla2_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_2)
        
def cambio5_2_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_2.config(text=numero_manejado)
    texto1 = casilla5_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla2_2["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_2)
        
def cambio1_3_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_3.config(text=numero_manejado)
    texto1 = casilla1_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla1_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_3)

def cambio2_3_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_3.config(text=numero_manejado)
    texto1 = casilla2_3["text"]   
    texto2 = casilla1_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla2_3)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla2_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_3)
        
def cambio3_3_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_3.config(text=numero_manejado)
    texto1 = casilla3_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla1_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla3_3)
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_3)
        
def cambio4_3_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_3.config(text=numero_manejado)
    texto1 = casilla4_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla1_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_3)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla4_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_3)
        
def cambio5_3_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_3.config(text=numero_manejado)
    texto1 = casilla5_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla1_3["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla5_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_3)
        
def cambio1_4_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_4.config(text=numero_manejado)
    texto1 = casilla1_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_4)
        
def cambio2_4_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_4.config(text=numero_manejado)
    texto1 = casilla2_4["text"]   
    texto2 = casilla1_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_4)
        
def cambio3_4_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_4.config(text=numero_manejado)
    texto1 = casilla3_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla1_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_4)
        
def cambio4_4_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_4.config(text=numero_manejado)
    texto1 = casilla4_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla1_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_4)
        
def cambio5_4_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_4.config(text=numero_manejado)
    texto1 = casilla5_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla1_4["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_4)
        
def cambio1_5_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_5.config(text=numero_manejado)
    texto1 = casilla1_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_5)
        
def cambio2_5_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_5.config(text=numero_manejado)
    texto1 = casilla2_5["text"]   
    texto2 = casilla1_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_5)
        
def cambio3_5_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_5.config(text=numero_manejado)
    texto1 = casilla3_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla1_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_4["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_5)
        
def cambio4_5_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_5.config(text=numero_manejado)
    texto1 = casilla4_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla1_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_5)
        
def cambio5_5_3():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_5.config(text=numero_manejado)
    texto1 = casilla5_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla1_5["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_5)

#================================================JUEGO 1================================================#
        
#==============================================INTERMEDIO===============================================#

def juego_intermedio_1(ventana_jugar):

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1

    global casilla1_2
    global casilla2_2
    global casilla3_2
    global casilla4_2
    global casilla5_2

    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3

    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4

    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5
    
    casilla1_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_1_1_intermedio)
    casilla1_1.place(x=127,y=150)
    casilla2_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_1_1_intermedio)
    casilla2_1.place(x=197,y=150)
    casilla3_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_1_1_intermedio)
    casilla3_1.place(x=267,y=150)
    casilla4_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_1_1_intermedio)
    casilla4_1.place(x=337,y=150)
    casilla5_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_1_1_intermedio)
    casilla5_1.place(x=407,y=150)

    casilla1_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_2_1_intermedio)
    casilla1_2.place(x=127,y=215)
    casilla2_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_2_1_intermedio)
    casilla2_2.place(x=197,y=215)
    casilla3_2 = tkinter.Button(ventana_jugar,height=2, width=5, text=4, command=numero_fijo)
    casilla3_2.place(x=267,y=215)
    casilla4_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_2_1_intermedio)
    casilla4_2.place(x=337,y=215)
    casilla5_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_2_1_intermedio)
    casilla5_2.place(x=407,y=215)

    casilla1_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_3_1_intermedio)
    casilla1_3.place(x=127,y=280)
    casilla2_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_3_1_intermedio)
    casilla2_3.place(x=197,y=280)
    casilla3_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_3_1_intermedio)
    casilla3_3.place(x=267,y=280)
    casilla4_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_3_1_intermedio)
    casilla4_3.place(x=337,y=280)
    casilla5_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_3_1_intermedio)
    casilla5_3.place(x=407,y=280)

    casilla1_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_4_1_intermedio)
    casilla1_4.place(x=127,y=345)
    casilla2_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_4_1_intermedio)
    casilla2_4.place(x=197,y=345)
    casilla3_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_4_1_intermedio)
    casilla3_4.place(x=267,y=345)
    casilla4_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_4_1_intermedio)
    casilla4_4.place(x=337,y=345)
    casilla5_4 = tkinter.Button(ventana_jugar,height=2, width=5, text=3, command=numero_fijo)
    casilla5_4.place(x=407,y=345)

    casilla1_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_5_1_intermedio)
    casilla1_5.place(x=127,y=410)
    casilla2_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_5_1_intermedio)
    casilla2_5.place(x=197,y=410)
    casilla3_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_5_1_intermedio)
    casilla3_5.place(x=267,y=410)
    casilla4_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_5_1_intermedio)
    casilla4_5.place(x=337,y=410)
    casilla5_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_5_1_intermedio)
    casilla5_5.place(x=407,y=410)
    
    label1 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=178, y=290)
    label2 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=247, y=290)
    label3 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=290)
    label4 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=290)
    label5 = tkinter.Label(ventana_jugar, text="v",bg="#FFECEC").place(x=353, y=258)
    label6 = tkinter.Label(ventana_jugar, text="ʌ",bg="#FFECEC").place(x=353, y=324)
    label1 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=178, y=420)

    global juego_cargado

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5
    
    if juego_cargado == True:

        casilla1_1.config(text=guardar_casilla1_1)
        casilla2_1.config(text=guardar_casilla2_1)
        casilla3_1.config(text=guardar_casilla3_1)
        casilla4_1.config(text=guardar_casilla4_1)
        casilla5_1.config(text=guardar_casilla5_1)
        casilla1_2.config(text=guardar_casilla1_2)
        casilla2_2.config(text=guardar_casilla2_2)
        casilla3_2.config(text=guardar_casilla3_2)
        casilla4_2.config(text=guardar_casilla4_2)
        casilla5_2.config(text=guardar_casilla5_2)
        casilla1_3.config(text=guardar_casilla1_3)
        casilla2_3.config(text=guardar_casilla2_3)
        casilla3_3.config(text=guardar_casilla3_3)
        casilla4_3.config(text=guardar_casilla4_3)
        casilla5_3.config(text=guardar_casilla5_3)
        casilla1_4.config(text=guardar_casilla1_4)
        casilla2_4.config(text=guardar_casilla2_4)
        casilla3_4.config(text=guardar_casilla3_4)
        casilla4_4.config(text=guardar_casilla4_4)
        casilla5_4.config(text=guardar_casilla5_4)
        casilla1_5.config(text=guardar_casilla1_5)
        casilla2_5.config(text=guardar_casilla2_5)
        casilla3_5.config(text=guardar_casilla3_5)
        casilla4_5.config(text=guardar_casilla4_5)
        casilla5_5.config(text=guardar_casilla5_5)
    
def cambio1_1_1_intermedio():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_1.config(text=numero_manejado)        
    texto1 = casilla1_1["text"]   
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_1)   

def cambio2_1_1_intermedio():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_1.config(text=numero_manejado)        
    texto1 = casilla2_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla2_2["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_1)  
       
def cambio3_1_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_1.config(text=numero_manejado)        
    texto1 = casilla3_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla3_2["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_1)
        
def cambio4_1_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_1.config(text=numero_manejado)        
    texto1 = casilla4_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla4_2["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]     
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_1)
        
def cambio5_1_1_intermedio():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_1.config(text=numero_manejado)        
    texto1 = casilla5_1["text"]   
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla4_1["text"]
    texto6 = casilla5_2["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]         
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_1)
        
def cambio1_2_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_2.config(text=numero_manejado)        
    texto1 = casilla1_2["text"]   
    texto2 = casilla2_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_2)
        
def cambio2_2_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_2.config(text=numero_manejado)        
    texto1 = casilla2_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_2)
        
def cambio3_2_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_2.config(text=numero_manejado)
    texto1 = casilla3_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla2_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_2)
        
def cambio4_2_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_2.config(text=numero_manejado)
    texto1 = casilla4_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla2_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto7 != "":
        if texto1 < texto7:
            return mayor(casilla4_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_2)
        
def cambio5_2_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_2.config(text=numero_manejado)
    texto1 = casilla5_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla2_2["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_2)
        
def cambio1_3_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_3.config(text=numero_manejado)
    texto1 = casilla1_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla1_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_3)

def cambio2_3_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_3.config(text=numero_manejado)
    texto1 = casilla2_3["text"]   
    texto2 = casilla1_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla2_3)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla2_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_3)
        
def cambio3_3_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_3.config(text=numero_manejado)
    texto1 = casilla3_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla1_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla3_3)
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_3)
        
def cambio4_3_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_3.config(text=numero_manejado)
    texto1 = casilla4_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla1_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_3)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla4_3)
    if texto8 != "":
        if texto1 > texto8:
            return menor(casilla4_3)
    if texto7 != "":
        if texto1 > texto7:
            return menor(casilla4_3) 
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_3)
        
def cambio5_3_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_3.config(text=numero_manejado)
    texto1 = casilla5_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla1_3["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla5_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_3)
        
def cambio1_4_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_4.config(text=numero_manejado)
    texto1 = casilla1_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_4)
        
def cambio2_4_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_4.config(text=numero_manejado)
    texto1 = casilla2_4["text"]   
    texto2 = casilla1_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_4)
        
def cambio3_4_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_4.config(text=numero_manejado)
    texto1 = casilla3_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla1_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_4)
        
def cambio4_4_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_4.config(text=numero_manejado)
    texto1 = casilla4_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla1_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_5["text"]
    if texto8 != "":
        if texto1 < texto8:
            return mayor(casilla4_4)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_4)
        
def cambio5_4_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_4.config(text=numero_manejado)
    texto1 = casilla5_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla1_4["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_4)
        
def cambio1_5_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_5.config(text=numero_manejado)
    texto1 = casilla1_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla1_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_5)
        
def cambio2_5_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_5.config(text=numero_manejado)
    texto1 = casilla2_5["text"]   
    texto2 = casilla1_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_4["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla2_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_5)
        
def cambio3_5_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_5.config(text=numero_manejado)
    texto1 = casilla3_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla1_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_4["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_5)
        
def cambio4_5_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_5.config(text=numero_manejado)
    texto1 = casilla4_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla1_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_5)
        
def cambio5_5_1_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_5.config(text=numero_manejado)
    texto1 = casilla5_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla1_5["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_5)

#================================================JUEGO 2================================================#
        
#==============================================INTERMEDIO===============================================#

def juego_intermedio_2(ventana_jugar):

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1

    global casilla1_2
    global casilla2_2
    global casilla3_2
    global casilla4_2
    global casilla5_2

    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3

    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4

    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5
    
    casilla1_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_1_2_intermedio)
    casilla1_1.place(x=127,y=150)
    casilla2_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_1_2_intermedio)
    casilla2_1.place(x=197,y=150)
    casilla3_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_1_2_intermedio)
    casilla3_1.place(x=267,y=150)
    casilla4_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_1_2_intermedio)
    casilla4_1.place(x=337,y=150)
    casilla5_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_1_2_intermedio)
    casilla5_1.place(x=407,y=150)

    casilla1_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_2_2_intermedio)
    casilla1_2.place(x=127,y=215)
    casilla2_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_2_2_intermedio)
    casilla2_2.place(x=197,y=215)
    casilla3_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_2_2_intermedio)
    casilla3_2.place(x=267,y=215)
    casilla4_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_2_2_intermedio)
    casilla4_2.place(x=337,y=215)
    casilla5_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_2_2_intermedio)
    casilla5_2.place(x=407,y=215)

    casilla1_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_3_2_intermedio)
    casilla1_3.place(x=127,y=280)
    casilla2_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_3_2_intermedio)
    casilla2_3.place(x=197,y=280)
    casilla3_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_3_2_intermedio)
    casilla3_3.place(x=267,y=280)
    casilla4_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_3_2_intermedio)
    casilla4_3.place(x=337,y=280)
    casilla5_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_3_2_intermedio)
    casilla5_3.place(x=407,y=280)

    casilla1_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_4_2_intermedio)
    casilla1_4.place(x=127,y=345)
    casilla2_4 = tkinter.Button(ventana_jugar,height=2, width=5, text=3, command=numero_fijo)
    casilla2_4.place(x=197,y=345)
    casilla3_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_4_2_intermedio)
    casilla3_4.place(x=267,y=345)
    casilla4_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_4_2_intermedio)
    casilla4_4.place(x=337,y=345)
    casilla5_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_4_2_intermedio)
    casilla5_4.place(x=407,y=345)

    casilla1_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_5_2_intermedio)
    casilla1_5.place(x=127,y=410)
    casilla2_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_5_2_intermedio)
    casilla2_5.place(x=197,y=410)
    casilla3_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_5_2_intermedio)
    casilla3_5.place(x=267,y=410)
    casilla4_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_5_2_intermedio)
    casilla4_5.place(x=337,y=410)
    casilla5_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_5_2_intermedio)
    casilla5_5.place(x=407,y=410)
    
    label1 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=178, y=290)
    label2 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=290)
    label3 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=290)
    label4 = tkinter.Label(ventana_jugar, text="v",bg="#FFECEC").place(x=282, y=258)
    label5 = tkinter.Label(ventana_jugar, text="ʌ",bg="#FFECEC").place(x=282, y=324)
    label6 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=178, y=420)
    label7 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=247, y=420)

    global juego_cargado

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5
    
    if juego_cargado == True:

        casilla1_1.config(text=guardar_casilla1_1)
        casilla2_1.config(text=guardar_casilla2_1)
        casilla3_1.config(text=guardar_casilla3_1)
        casilla4_1.config(text=guardar_casilla4_1)
        casilla5_1.config(text=guardar_casilla5_1)
        casilla1_2.config(text=guardar_casilla1_2)
        casilla2_2.config(text=guardar_casilla2_2)
        casilla3_2.config(text=guardar_casilla3_2)
        casilla4_2.config(text=guardar_casilla4_2)
        casilla5_2.config(text=guardar_casilla5_2)
        casilla1_3.config(text=guardar_casilla1_3)
        casilla2_3.config(text=guardar_casilla2_3)
        casilla3_3.config(text=guardar_casilla3_3)
        casilla4_3.config(text=guardar_casilla4_3)
        casilla5_3.config(text=guardar_casilla5_3)
        casilla1_4.config(text=guardar_casilla1_4)
        casilla2_4.config(text=guardar_casilla2_4)
        casilla3_4.config(text=guardar_casilla3_4)
        casilla4_4.config(text=guardar_casilla4_4)
        casilla5_4.config(text=guardar_casilla5_4)
        casilla1_5.config(text=guardar_casilla1_5)
        casilla2_5.config(text=guardar_casilla2_5)
        casilla3_5.config(text=guardar_casilla3_5)
        casilla4_5.config(text=guardar_casilla4_5)
        casilla5_5.config(text=guardar_casilla5_5)
    
def cambio1_1_2_intermedio():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_1.config(text=numero_manejado)        
    texto1 = casilla1_1["text"]   
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_1)  

def cambio2_1_2_intermedio():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_1.config(text=numero_manejado)        
    texto1 = casilla2_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla2_2["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_1)  
       
def cambio3_1_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_1.config(text=numero_manejado)        
    texto1 = casilla3_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla3_2["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_1)
        
def cambio4_1_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_1.config(text=numero_manejado)        
    texto1 = casilla4_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla4_2["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]     
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_1)
        
def cambio5_1_2_intermedio():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_1.config(text=numero_manejado)        
    texto1 = casilla5_1["text"]   
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla4_1["text"]
    texto6 = casilla5_2["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]         
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_1)
        
def cambio1_2_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_2.config(text=numero_manejado)        
    texto1 = casilla1_2["text"]   
    texto2 = casilla2_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_2)
        
def cambio2_2_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_2.config(text=numero_manejado)        
    texto1 = casilla2_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_2)
        
def cambio3_2_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_2.config(text=numero_manejado)
    texto1 = casilla3_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla2_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto7 != "":
        if texto1 < texto7:
            return mayor(casilla3_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_2)
        
def cambio4_2_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_2.config(text=numero_manejado)
    texto1 = casilla4_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla2_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_2)
        
def cambio5_2_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_2.config(text=numero_manejado)
    texto1 = casilla5_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla2_2["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_2)
        
def cambio1_3_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_3.config(text=numero_manejado)
    texto1 = casilla1_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla1_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_3)

def cambio2_3_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_3.config(text=numero_manejado)
    texto1 = casilla2_3["text"]   
    texto2 = casilla1_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla2_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_3)
        
def cambio3_3_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_3.config(text=numero_manejado)
    texto1 = casilla3_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla1_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_3)
    if texto8 != "":
        if texto1 > texto8:
            return menor(casilla3_3)
    if texto7 != "":
        if texto1 > texto7:
            return menor(casilla3_3) 
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_3)
        
def cambio4_3_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_3.config(text=numero_manejado)
    texto1 = casilla4_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla1_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_3)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla4_3) 
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_3)
        
def cambio5_3_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_3.config(text=numero_manejado)
    texto1 = casilla5_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla1_3["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla5_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_3)
        
def cambio1_4_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_4.config(text=numero_manejado)
    texto1 = casilla1_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        fila(casilla1_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        columna(casilla1_4)
        
def cambio2_4_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_4.config(text=numero_manejado)
    texto1 = casilla2_4["text"]   
    texto2 = casilla1_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_4)
        
def cambio3_4_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_4.config(text=numero_manejado)
    texto1 = casilla3_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla1_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_5["text"]
    if texto8 != "":
        if texto1 < texto8:
            return mayor(casilla3_4)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_4)
        
def cambio4_4_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_4.config(text=numero_manejado)
    texto1 = casilla4_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla1_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_4)
        
def cambio5_4_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_4.config(text=numero_manejado)
    texto1 = casilla5_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla1_4["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_4)
        
def cambio1_5_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_5.config(text=numero_manejado)
    texto1 = casilla1_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla1_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_5)
        
def cambio2_5_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_5.config(text=numero_manejado)
    texto1 = casilla2_5["text"]   
    texto2 = casilla1_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_4["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla2_5)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla2_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_5)
        
def cambio3_5_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_5.config(text=numero_manejado)
    texto1 = casilla3_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla1_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla3_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_5)
        
def cambio4_5_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_5.config(text=numero_manejado)
    texto1 = casilla4_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla1_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_5)
        
def cambio5_5_2_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_5.config(text=numero_manejado)
    texto1 = casilla5_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla1_5["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_5)

#================================================JUEGO 3================================================#
        
#==============================================INTERMEDIO===============================================#

def juego_intermedio_3(ventana_jugar):

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1

    global casilla1_2
    global casilla2_2
    global casilla3_2
    global casilla4_2
    global casilla5_2

    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3

    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4

    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5
    
    casilla1_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_1_3_intermedio)
    casilla1_1.place(x=127,y=150)
    casilla2_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_1_3_intermedio)
    casilla2_1.place(x=197,y=150)
    casilla3_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_1_3_intermedio)
    casilla3_1.place(x=267,y=150)
    casilla4_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_1_3_intermedio)
    casilla4_1.place(x=337,y=150)
    casilla5_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_1_3_intermedio)
    casilla5_1.place(x=407,y=150)

    casilla1_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_2_3_intermedio)
    casilla1_2.place(x=127,y=215)
    casilla2_2 = tkinter.Button(ventana_jugar,height=2, width=5, text=2, command=numero_fijo)
    casilla2_2.place(x=197,y=215)
    casilla3_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_2_3_intermedio)
    casilla3_2.place(x=267,y=215)
    casilla4_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_2_3_intermedio)
    casilla4_2.place(x=337,y=215)
    casilla5_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_2_3_intermedio)
    casilla5_2.place(x=407,y=215)

    casilla1_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_3_3_intermedio)
    casilla1_3.place(x=127,y=280)
    casilla2_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_3_3_intermedio)
    casilla2_3.place(x=197,y=280)
    casilla3_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_3_3_intermedio)
    casilla3_3.place(x=267,y=280)
    casilla4_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_3_3_intermedio)
    casilla4_3.place(x=337,y=280)
    casilla5_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_3_3_intermedio)
    casilla5_3.place(x=407,y=280)

    casilla1_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_4_3_intermedio)
    casilla1_4.place(x=127,y=345)
    casilla2_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_4_3_intermedio)
    casilla2_4.place(x=197,y=345)
    casilla3_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_4_3_intermedio)
    casilla3_4.place(x=267,y=345)
    casilla4_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_4_3_intermedio)
    casilla4_4.place(x=337,y=345)
    casilla5_4 = tkinter.Button(ventana_jugar,height=2, width=5, text=1, command=numero_fijo)
    casilla5_4.place(x=407,y=345)

    casilla1_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_5_3_intermedio)
    casilla1_5.place(x=127,y=410)
    casilla2_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_5_3_intermedio)
    casilla2_5.place(x=197,y=410)
    casilla3_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_5_3_intermedio)
    casilla3_5.place(x=267,y=410)
    casilla4_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_5_3_intermedio)
    casilla4_5.place(x=337,y=410)
    casilla5_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_5_3_intermedio)
    casilla5_5.place(x=407,y=410)
    
    label1 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=178, y=290)
    label2 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=160)
    label3 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=160)
    label4 = tkinter.Label(ventana_jugar, text="v",bg="#FFECEC").place(x=282, y=258)
    label5 = tkinter.Label(ventana_jugar, text="ʌ",bg="#FFECEC").place(x=282, y=324)
    label6 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=178, y=420)
    label7 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=247, y=420)

    global juego_cargado

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5
    
    if juego_cargado == True:

        casilla1_1.config(text=guardar_casilla1_1)
        casilla2_1.config(text=guardar_casilla2_1)
        casilla3_1.config(text=guardar_casilla3_1)
        casilla4_1.config(text=guardar_casilla4_1)
        casilla5_1.config(text=guardar_casilla5_1)
        casilla1_2.config(text=guardar_casilla1_2)
        casilla2_2.config(text=guardar_casilla2_2)
        casilla3_2.config(text=guardar_casilla3_2)
        casilla4_2.config(text=guardar_casilla4_2)
        casilla5_2.config(text=guardar_casilla5_2)
        casilla1_3.config(text=guardar_casilla1_3)
        casilla2_3.config(text=guardar_casilla2_3)
        casilla3_3.config(text=guardar_casilla3_3)
        casilla4_3.config(text=guardar_casilla4_3)
        casilla5_3.config(text=guardar_casilla5_3)
        casilla1_4.config(text=guardar_casilla1_4)
        casilla2_4.config(text=guardar_casilla2_4)
        casilla3_4.config(text=guardar_casilla3_4)
        casilla4_4.config(text=guardar_casilla4_4)
        casilla5_4.config(text=guardar_casilla5_4)
        casilla1_5.config(text=guardar_casilla1_5)
        casilla2_5.config(text=guardar_casilla2_5)
        casilla3_5.config(text=guardar_casilla3_5)
        casilla4_5.config(text=guardar_casilla4_5)
        casilla5_5.config(text=guardar_casilla5_5)
    
def cambio1_1_3_intermedio():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_1.config(text=numero_manejado)        
    texto1 = casilla1_1["text"]   
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_1)  

def cambio2_1_3_intermedio():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_1.config(text=numero_manejado)        
    texto1 = casilla2_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla2_2["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_1)     
       
def cambio3_1_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_1.config(text=numero_manejado)        
    texto1 = casilla3_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla3_2["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_1)  
        
def cambio4_1_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_1.config(text=numero_manejado)        
    texto1 = casilla4_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla4_2["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_1)
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla4_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_1)
        
def cambio5_1_3_intermedio():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_1.config(text=numero_manejado)        
    texto1 = casilla5_1["text"]   
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla4_1["text"]
    texto6 = casilla5_2["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto5 != "":
        if texto1 > texto5:
            return menor(casilla5_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_1)
        
def cambio1_2_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_2.config(text=numero_manejado)        
    texto1 = casilla1_2["text"]   
    texto2 = casilla2_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_2)
        
def cambio2_2_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_2.config(text=numero_manejado)        
    texto1 = casilla2_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_2)
        
def cambio3_2_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_2.config(text=numero_manejado)
    texto1 = casilla3_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla2_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto7 != "":
        if texto1 < texto7:
            return mayor(casilla3_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_2)
        
def cambio4_2_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_2.config(text=numero_manejado)
    texto1 = casilla4_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla2_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_2)
        
def cambio5_2_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_2.config(text=numero_manejado)
    texto1 = casilla5_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla2_2["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_2)
        
def cambio1_3_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_3.config(text=numero_manejado)
    texto1 = casilla1_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla1_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_3)

def cambio2_3_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_3.config(text=numero_manejado)
    texto1 = casilla2_3["text"]   
    texto2 = casilla1_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla2_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_3)
        
def cambio3_3_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_3.config(text=numero_manejado)
    texto1 = casilla3_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla1_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto8 != "":
        if texto1 > texto8:
            return menor(casilla3_3)
    if texto7 != "":
        if texto1 > texto7:
            return menor(casilla3_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_3)
        
def cambio4_3_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_3.config(text=numero_manejado)
    texto1 = casilla4_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla1_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_3)
        
def cambio5_3_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_3.config(text=numero_manejado)
    texto1 = casilla5_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla1_3["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_3)
        
def cambio1_4_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_4.config(text=numero_manejado)
    texto1 = casilla1_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_4)
        
def cambio2_4_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_4.config(text=numero_manejado)
    texto1 = casilla2_4["text"]   
    texto2 = casilla1_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_4)
        
def cambio3_4_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_4.config(text=numero_manejado)
    texto1 = casilla3_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla1_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_5["text"]
    if texto8 != "":
        if texto1 < texto8:
            return mayor(casilla3_4)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_4)
        
def cambio4_4_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_4.config(text=numero_manejado)
    texto1 = casilla4_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla1_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_4)
        
def cambio5_4_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_4.config(text=numero_manejado)
    texto1 = casilla5_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla1_4["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_4)
        
def cambio1_5_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_5.config(text=numero_manejado)
    texto1 = casilla1_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla1_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_5)
        
def cambio2_5_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_5.config(text=numero_manejado)
    texto1 = casilla2_5["text"]   
    texto2 = casilla1_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_4["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla2_5)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla2_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_5)
        
def cambio3_5_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_5.config(text=numero_manejado)
    texto1 = casilla3_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla1_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla3_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_5)
        
def cambio4_5_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_5.config(text=numero_manejado)
    texto1 = casilla4_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla1_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_5)
        
def cambio5_5_3_intermedio():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_5.config(text=numero_manejado)
    texto1 = casilla5_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla1_5["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_5)

#================================================JUEGO 1================================================#
        
#================================================DIFICIL================================================#

def juego_dificil_1(ventana_jugar):

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1

    global casilla1_2
    global casilla2_2
    global casilla3_2
    global casilla4_2
    global casilla5_2

    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3

    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4

    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5
    
    casilla1_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_1_1_dificil)
    casilla1_1.place(x=127,y=150)
    casilla2_1 = tkinter.Button(ventana_jugar,height=2, width=5, text=1, command=numero_fijo)
    casilla2_1.place(x=197,y=150)
    casilla3_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_1_1_dificil)
    casilla3_1.place(x=267,y=150)
    casilla4_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_1_1_dificil)
    casilla4_1.place(x=337,y=150)
    casilla5_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_1_1_dificil)
    casilla5_1.place(x=407,y=150)

    casilla1_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_2_1_dificil)
    casilla1_2.place(x=127,y=215)
    casilla2_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_2_1_dificil)
    casilla2_2.place(x=197,y=215)
    casilla3_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_2_1_dificil)
    casilla3_2.place(x=267,y=215)
    casilla4_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_2_1_dificil)
    casilla4_2.place(x=337,y=215)
    casilla5_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_2_1_dificil)
    casilla5_2.place(x=407,y=215)

    casilla1_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_3_1_dificil)
    casilla1_3.place(x=127,y=280)
    casilla2_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_3_1_dificil)
    casilla2_3.place(x=197,y=280)
    casilla3_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_3_1_dificil)
    casilla3_3.place(x=267,y=280)
    casilla4_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_3_1_dificil)
    casilla4_3.place(x=337,y=280)
    casilla5_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_3_1_dificil)
    casilla5_3.place(x=407,y=280)

    casilla1_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_4_1_dificil)
    casilla1_4.place(x=127,y=345)
    casilla2_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_4_1_dificil)
    casilla2_4.place(x=197,y=345)
    casilla3_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_4_1_dificil)
    casilla3_4.place(x=267,y=345)
    casilla4_4 = tkinter.Button(ventana_jugar,height=2, width=5, text=4, command=numero_fijo)
    casilla4_4.place(x=337,y=345)
    casilla5_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_4_1_dificil)
    casilla5_4.place(x=407,y=345)

    casilla1_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_5_1_dificil)
    casilla1_5.place(x=127,y=410)
    casilla2_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_5_1_dificil)
    casilla2_5.place(x=197,y=410)
    casilla3_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_5_1_dificil)
    casilla3_5.place(x=267,y=410)
    casilla4_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_5_1_dificil)
    casilla4_5.place(x=337,y=410)
    casilla5_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_5_1_dificil)
    casilla5_5.place(x=407,y=410)
    
    label1 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=178, y=290)
    label2 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=160)
    label3 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=160)
    label4 = tkinter.Label(ventana_jugar, text="v",bg="#FFECEC").place(x=282, y=258)
    label5 = tkinter.Label(ventana_jugar, text="ʌ",bg="#FFECEC").place(x=282, y=324)
    label6 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=178, y=420)
    label7 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=247, y=420)

    label8 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=420)
    label9 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=420)
    label10 = tkinter.Label(ventana_jugar, text="ʌ",bg="#FFECEC").place(x=423, y=324)
    label1 = tkinter.Label(ventana_jugar, text="v",bg="#FFECEC").place(x=143, y=192)

    global juego_cargado

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5
    
    if juego_cargado == True:

        casilla1_1.config(text=guardar_casilla1_1)
        casilla2_1.config(text=guardar_casilla2_1)
        casilla3_1.config(text=guardar_casilla3_1)
        casilla4_1.config(text=guardar_casilla4_1)
        casilla5_1.config(text=guardar_casilla5_1)
        casilla1_2.config(text=guardar_casilla1_2)
        casilla2_2.config(text=guardar_casilla2_2)
        casilla3_2.config(text=guardar_casilla3_2)
        casilla4_2.config(text=guardar_casilla4_2)
        casilla5_2.config(text=guardar_casilla5_2)
        casilla1_3.config(text=guardar_casilla1_3)
        casilla2_3.config(text=guardar_casilla2_3)
        casilla3_3.config(text=guardar_casilla3_3)
        casilla4_3.config(text=guardar_casilla4_3)
        casilla5_3.config(text=guardar_casilla5_3)
        casilla1_4.config(text=guardar_casilla1_4)
        casilla2_4.config(text=guardar_casilla2_4)
        casilla3_4.config(text=guardar_casilla3_4)
        casilla4_4.config(text=guardar_casilla4_4)
        casilla5_4.config(text=guardar_casilla5_4)
        casilla1_5.config(text=guardar_casilla1_5)
        casilla2_5.config(text=guardar_casilla2_5)
        casilla3_5.config(text=guardar_casilla3_5)
        casilla4_5.config(text=guardar_casilla4_5)
        casilla5_5.config(text=guardar_casilla5_5)
    
def cambio1_1_1_dificil():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_1.config(text=numero_manejado)        
    texto1 = casilla1_1["text"]   
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto6 != "":
        if texto1 < texto6:
            return mayor(casilla1_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_1)   

def cambio2_1_1_dificil():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_1.config(text=numero_manejado)        
    texto1 = casilla2_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla2_2["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_1)    
       
def cambio3_1_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_1.config(text=numero_manejado)        
    texto1 = casilla3_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla3_2["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_1)  
        
def cambio4_1_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_1.config(text=numero_manejado)        
    texto1 = casilla4_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla4_2["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_1)
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla4_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return colunma(casilla4_1)
        
def cambio5_1_1_dificil():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_1.config(text=numero_manejado)        
    texto1 = casilla5_1["text"]   
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla4_1["text"]
    texto6 = casilla5_2["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto5 != "":
        if texto1 > texto5:
            return menor(casilla5_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
       return columna(casilla5_1)
        
def cambio1_2_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_2.config(text=numero_manejado)        
    texto1 = casilla1_2["text"]   
    texto2 = casilla2_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto6 != "":
        if texto1 > texto6:
            return menor(casilla1_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_2)
        
def cambio2_2_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_2.config(text=numero_manejado)        
    texto1 = casilla2_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_2)
        
def cambio3_2_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_2.config(text=numero_manejado)
    texto1 = casilla3_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla2_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto7 != "":
        if texto1 < texto7:
            return mayor(casilla3_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_2)
        
def cambio4_2_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_2.config(text=numero_manejado)
    texto1 = casilla4_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla2_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_2)
        
def cambio5_2_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_2.config(text=numero_manejado)
    texto1 = casilla5_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla2_2["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_2)
        
def cambio1_3_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_3.config(text=numero_manejado)
    texto1 = casilla1_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla1_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_3)

def cambio2_3_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_3.config(text=numero_manejado)
    texto1 = casilla2_3["text"]   
    texto2 = casilla1_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla2_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_3)
        
def cambio3_3_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_3.config(text=numero_manejado)
    texto1 = casilla3_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla1_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto8 != "":
        if texto1 > texto8:
            return menor(casilla3_3)
    if texto7 != "":
        if texto1 > texto7:
            return menor(casilla3_3) 
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_3)
        
def cambio4_3_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_3.config(text=numero_manejado)
    texto1 = casilla4_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla1_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_3)
        
def cambio5_3_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_3.config(text=numero_manejado)
    texto1 = casilla5_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla1_3["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto8 != "":
        if texto1 > texto8:
            return menor(casilla5_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_3)
        
def cambio1_4_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_4.config(text=numero_manejado)
    texto1 = casilla1_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_4)
        
def cambio2_4_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_4.config(text=numero_manejado)
    texto1 = casilla2_4["text"]   
    texto2 = casilla1_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_4)
        
def cambio3_4_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_4.config(text=numero_manejado)
    texto1 = casilla3_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla1_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_5["text"]
    if texto8 != "":
        if texto1 < texto8:
            return mayor(casilla3_4)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_4)
        
def cambio4_4_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_4.config(text=numero_manejado)
    texto1 = casilla4_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla1_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_4)
        
def cambio5_4_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_4.config(text=numero_manejado)
    texto1 = casilla5_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla1_4["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_5["text"]
    if texto8 != "":
        if texto1 < texto8:
            return mayor(casilla5_4)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_4)
        
def cambio1_5_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_5.config(text=numero_manejado)
    texto1 = casilla1_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla1_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_5)
        
def cambio2_5_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_5.config(text=numero_manejado)
    texto1 = casilla2_5["text"]   
    texto2 = casilla1_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_4["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla2_5)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla2_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_5)
        
def cambio3_5_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_5.config(text=numero_manejado)
    texto1 = casilla3_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla1_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla3_5)
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_5)
        
def cambio4_5_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_5.config(text=numero_manejado)
    texto1 = casilla4_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla1_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_4["text"]
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla4_5)
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_5)
        
def cambio5_5_1_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_5.config(text=numero_manejado)
    texto1 = casilla5_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla1_5["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_4["text"]
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla5_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_5)

#================================================JUEGO 2================================================#
        
#================================================DIFICIL================================================#

def juego_dificil_2(ventana_jugar):

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1

    global casilla1_2
    global casilla2_2
    global casilla3_2
    global casilla4_2
    global casilla5_2

    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3

    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4

    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5
    
    casilla1_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_1_2_dificil)
    casilla1_1.place(x=127,y=150)
    casilla2_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_1_2_dificil)
    casilla2_1.place(x=197,y=150)
    casilla3_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_1_2_dificil)
    casilla3_1.place(x=267,y=150)
    casilla4_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_1_2_dificil)
    casilla4_1.place(x=337,y=150)
    casilla5_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_1_2_dificil)
    casilla5_1.place(x=407,y=150)

    casilla1_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_2_2_dificil)
    casilla1_2.place(x=127,y=215)
    casilla2_2 = tkinter.Button(ventana_jugar,height=2, width=5, text=2, command=numero_fijo)
    casilla2_2.place(x=197,y=215)
    casilla3_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_2_2_dificil)
    casilla3_2.place(x=267,y=215)
    casilla4_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_2_2_dificil)
    casilla4_2.place(x=337,y=215)
    casilla5_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_2_2_dificil)
    casilla5_2.place(x=407,y=215)

    casilla1_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_3_2_dificil)
    casilla1_3.place(x=127,y=280)
    casilla2_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_3_2_dificil)
    casilla2_3.place(x=197,y=280)
    casilla3_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_3_2_dificil)
    casilla3_3.place(x=267,y=280)
    casilla4_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_3_2_dificil)
    casilla4_3.place(x=337,y=280)
    casilla5_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_3_2_dificil)
    casilla5_3.place(x=407,y=280)

    casilla1_4 = tkinter.Button(ventana_jugar,height=2, width=5, text=2, command=numero_fijo)
    casilla1_4.place(x=127,y=345)
    casilla2_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_4_2_dificil)
    casilla2_4.place(x=197,y=345)
    casilla3_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_4_2_dificil)
    casilla3_4.place(x=267,y=345)
    casilla4_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_4_2_dificil)
    casilla4_4.place(x=337,y=345)
    casilla5_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_4_2_dificil)
    casilla5_4.place(x=407,y=345)

    casilla1_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_5_2_dificil)
    casilla1_5.place(x=127,y=410)
    casilla2_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_5_2_dificil)
    casilla2_5.place(x=197,y=410)
    casilla3_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_5_2_dificil)
    casilla3_5.place(x=267,y=410)
    casilla4_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_5_2_dificil)
    casilla4_5.place(x=337,y=410)
    casilla5_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_5_2_dificil)
    casilla5_5.place(x=407,y=410)
    
    label1 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=178, y=290)
    label2 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=160)
    label3 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=160)
    label4 = tkinter.Label(ventana_jugar, text="v",bg="#FFECEC").place(x=282, y=258)
    label5 = tkinter.Label(ventana_jugar, text="ʌ",bg="#FFECEC").place(x=282, y=324)
    label6 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=178, y=420)
    label7 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=247, y=420)

    label8 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=225)
    label9 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=225)
    label10 = tkinter.Label(ventana_jugar, text="ʌ",bg="#FFECEC").place(x=423, y=324)
    label1 = tkinter.Label(ventana_jugar, text="v",bg="#FFECEC").place(x=143, y=192)

    global juego_cargado

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5
    
    if juego_cargado == True:

        casilla1_1.config(text=guardar_casilla1_1)
        casilla2_1.config(text=guardar_casilla2_1)
        casilla3_1.config(text=guardar_casilla3_1)
        casilla4_1.config(text=guardar_casilla4_1)
        casilla5_1.config(text=guardar_casilla5_1)
        casilla1_2.config(text=guardar_casilla1_2)
        casilla2_2.config(text=guardar_casilla2_2)
        casilla3_2.config(text=guardar_casilla3_2)
        casilla4_2.config(text=guardar_casilla4_2)
        casilla5_2.config(text=guardar_casilla5_2)
        casilla1_3.config(text=guardar_casilla1_3)
        casilla2_3.config(text=guardar_casilla2_3)
        casilla3_3.config(text=guardar_casilla3_3)
        casilla4_3.config(text=guardar_casilla4_3)
        casilla5_3.config(text=guardar_casilla5_3)
        casilla1_4.config(text=guardar_casilla1_4)
        casilla2_4.config(text=guardar_casilla2_4)
        casilla3_4.config(text=guardar_casilla3_4)
        casilla4_4.config(text=guardar_casilla4_4)
        casilla5_4.config(text=guardar_casilla5_4)
        casilla1_5.config(text=guardar_casilla1_5)
        casilla2_5.config(text=guardar_casilla2_5)
        casilla3_5.config(text=guardar_casilla3_5)
        casilla4_5.config(text=guardar_casilla4_5)
        casilla5_5.config(text=guardar_casilla5_5)
    
def cambio1_1_2_dificil():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_1.config(text=numero_manejado)        
    texto1 = casilla1_1["text"]   
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto6 != "":
        if texto1 < texto6:
            return mayor(casilla1_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_1)  

def cambio2_1_2_dificil():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_1.config(text=numero_manejado)        
    texto1 = casilla2_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla2_2["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_1)     
       
def cambio3_1_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_1.config(text=numero_manejado)        
    texto1 = casilla3_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla3_2["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_1)  
        
def cambio4_1_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_1.config(text=numero_manejado)        
    texto1 = casilla4_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla4_2["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_1)
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla4_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_1)
        
def cambio5_1_2_dificil():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_1.config(text=numero_manejado)        
    texto1 = casilla5_1["text"]   
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla4_1["text"]
    texto6 = casilla5_2["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto5 != "":
        if texto1 > texto5:
            return menor(casilla5_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_1)
        
def cambio1_2_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_2.config(text=numero_manejado)        
    texto1 = casilla1_2["text"]   
    texto2 = casilla2_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto6 != "":
        if texto1 > texto6:
            return menor(casilla1_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_2)
        
def cambio2_2_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_2.config(text=numero_manejado)        
    texto1 = casilla2_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_2)
        
def cambio3_2_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_2.config(text=numero_manejado)
    texto1 = casilla3_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla2_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto7 != "":
        if texto1 < texto7:
            return mayor(casilla3_2)
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_2)
        
def cambio4_2_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_2.config(text=numero_manejado)
    texto1 = casilla4_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla2_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla4_2)
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_2)
        
def cambio5_2_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_2.config(text=numero_manejado)
    texto1 = casilla5_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla2_2["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla5_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_2)
        
def cambio1_3_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_3.config(text=numero_manejado)
    texto1 = casilla1_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla1_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_3)

def cambio2_3_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_3.config(text=numero_manejado)
    texto1 = casilla2_3["text"]   
    texto2 = casilla1_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla2_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_3)
        
def cambio3_3_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_3.config(text=numero_manejado)
    texto1 = casilla3_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla1_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto8 != "":
        if texto1 > texto8:
            return menor(casilla3_3)
    if texto7 != "":
        if texto1 > texto7:
            return menor(casilla3_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_3)
        
def cambio4_3_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_3.config(text=numero_manejado)
    texto1 = casilla4_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla1_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_3)
        
def cambio5_3_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_3.config(text=numero_manejado)
    texto1 = casilla5_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla1_3["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto8 != "":
        if texto1 > texto8:
            return menor(casilla5_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_3)
        
def cambio1_4_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_4.config(text=numero_manejado)
    texto1 = casilla1_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_4)
        
def cambio2_4_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_4.config(text=numero_manejado)
    texto1 = casilla2_4["text"]   
    texto2 = casilla1_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_4)
        
def cambio3_4_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_4.config(text=numero_manejado)
    texto1 = casilla3_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla1_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_5["text"]
    if texto8 != "":
        if texto1 < texto8:
            return mayor(casilla3_4)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_4)
        
def cambio4_4_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_4.config(text=numero_manejado)
    texto1 = casilla4_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla1_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_4)
        
def cambio5_4_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_4.config(text=numero_manejado)
    texto1 = casilla5_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla1_4["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_5["text"]
    if texto8 != "":
        if texto1 < texto8:
            return mayor(casilla5_4)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_4)
        
def cambio1_5_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_5.config(text=numero_manejado)
    texto1 = casilla1_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla1_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_5)
        
def cambio2_5_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_5.config(text=numero_manejado)
    texto1 = casilla2_5["text"]   
    texto2 = casilla1_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_4["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla2_5)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla2_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_5)
        
def cambio3_5_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_5.config(text=numero_manejado)
    texto1 = casilla3_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla1_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_4["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla3_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_5)
        
def cambio4_5_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_5.config(text=numero_manejado)
    texto1 = casilla4_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla1_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_5)
        
def cambio5_5_2_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_5.config(text=numero_manejado)
    texto1 = casilla5_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla1_5["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_5)

#================================================JUEGO 3================================================#
        
#================================================DIFICIL================================================#

def juego_dificil_3(ventana_jugar):

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1

    global casilla1_2
    global casilla2_2
    global casilla3_2
    global casilla4_2
    global casilla5_2

    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3

    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4

    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5
    
    casilla1_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_1_3_dificil)
    casilla1_1.place(x=127,y=150)
    casilla2_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_1_3_dificil)
    casilla2_1.place(x=197,y=150)
    casilla3_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_1_3_dificil)
    casilla3_1.place(x=267,y=150)
    casilla4_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_1_3_dificil)
    casilla4_1.place(x=337,y=150)
    casilla5_1 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_1_3_dificil)
    casilla5_1.place(x=407,y=150)

    casilla1_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_2_3_dificil)
    casilla1_2.place(x=127,y=215)
    casilla2_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_2_3_dificil)
    casilla2_2.place(x=197,y=215)
    casilla3_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_2_3_dificil)
    casilla3_2.place(x=267,y=215)
    casilla4_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_2_3_dificil)
    casilla4_2.place(x=337,y=215)
    casilla5_2 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_2_3_dificil)
    casilla5_2.place(x=407,y=215)

    casilla1_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_3_3_dificil)
    casilla1_3.place(x=127,y=280)
    casilla2_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_3_3_dificil)
    casilla2_3.place(x=197,y=280)
    casilla3_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_3_3_dificil)
    casilla3_3.place(x=267,y=280)
    casilla4_3 = tkinter.Button(ventana_jugar,height=2, width=5, text=4, command=numero_fijo)
    casilla4_3.place(x=337,y=280)
    casilla5_3 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_3_3_dificil)
    casilla5_3.place(x=407,y=280)

    casilla1_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio1_4_3_dificil)
    casilla1_4.place(x=127,y=345)
    casilla2_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_4_3_dificil)
    casilla2_4.place(x=197,y=345)
    casilla3_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_4_3_dificil)
    casilla3_4.place(x=267,y=345)
    casilla4_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_4_3_dificil)
    casilla4_4.place(x=337,y=345)
    casilla5_4 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_4_3_dificil)
    casilla5_4.place(x=407,y=345)

    casilla1_5 = tkinter.Button(ventana_jugar,height=2, width=5, text=5, command=numero_fijo)
    casilla1_5.place(x=127,y=410)
    casilla2_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio2_5_3_dificil)
    casilla2_5.place(x=197,y=410)
    casilla3_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio3_5_3_dificil)
    casilla3_5.place(x=267,y=410)
    casilla4_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio4_5_3_dificil)
    casilla4_5.place(x=337,y=410)
    casilla5_5 = tkinter.Button(ventana_jugar,height=2, width=5, command=cambio5_5_3_dificil)
    casilla5_5.place(x=407,y=410)
    
    label1 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=178, y=290)
    label2 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=160)
    label3 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=160)
    label4 = tkinter.Label(ventana_jugar, text="v",bg="#FFECEC").place(x=282, y=258)
    label5 = tkinter.Label(ventana_jugar, text="ʌ",bg="#FFECEC").place(x=282, y=324)
    label6 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=420)
    label7 = tkinter.Label(ventana_jugar, text="<",bg="#FFECEC").place(x=388, y=420)

    label8 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=318, y=225)
    label9 = tkinter.Label(ventana_jugar, text=">",bg="#FFECEC").place(x=388, y=225)
    label10 = tkinter.Label(ventana_jugar, text="ʌ",bg="#FFECEC").place(x=423, y=324)
    label1 = tkinter.Label(ventana_jugar, text="v",bg="#FFECEC").place(x=143, y=192)

    global juego_cargado

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5
    
    if juego_cargado == True:

        casilla1_1.config(text=guardar_casilla1_1)
        casilla2_1.config(text=guardar_casilla2_1)
        casilla3_1.config(text=guardar_casilla3_1)
        casilla4_1.config(text=guardar_casilla4_1)
        casilla5_1.config(text=guardar_casilla5_1)
        casilla1_2.config(text=guardar_casilla1_2)
        casilla2_2.config(text=guardar_casilla2_2)
        casilla3_2.config(text=guardar_casilla3_2)
        casilla4_2.config(text=guardar_casilla4_2)
        casilla5_2.config(text=guardar_casilla5_2)
        casilla1_3.config(text=guardar_casilla1_3)
        casilla2_3.config(text=guardar_casilla2_3)
        casilla3_3.config(text=guardar_casilla3_3)
        casilla4_3.config(text=guardar_casilla4_3)
        casilla5_3.config(text=guardar_casilla5_3)
        casilla1_4.config(text=guardar_casilla1_4)
        casilla2_4.config(text=guardar_casilla2_4)
        casilla3_4.config(text=guardar_casilla3_4)
        casilla4_4.config(text=guardar_casilla4_4)
        casilla5_4.config(text=guardar_casilla5_4)
        casilla1_5.config(text=guardar_casilla1_5)
        casilla2_5.config(text=guardar_casilla2_5)
        casilla3_5.config(text=guardar_casilla3_5)
        casilla4_5.config(text=guardar_casilla4_5)
        casilla5_5.config(text=guardar_casilla5_5)
    
def cambio1_1_3_dificil():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_1.config(text=numero_manejado)        
    texto1 = casilla1_1["text"]   
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto6 != "":
        if texto1 < texto6:
            return mayor(casilla1_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_1)   

def cambio2_1_3_dificil():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_1.config(text=numero_manejado)        
    texto1 = casilla2_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla2_2["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_1)   
       
def cambio3_1_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_1.config(text=numero_manejado)        
    texto1 = casilla3_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla3_2["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_1)   
        
def cambio4_1_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_1.config(text=numero_manejado)        
    texto1 = casilla4_1["text"]    
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla4_2["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_1)
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla4_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_1)
        
def cambio5_1_3_dificil():    
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_1.config(text=numero_manejado)        
    texto1 = casilla5_1["text"]   
    texto2 = casilla1_1["text"]
    texto3 = casilla2_1["text"]
    texto4 = casilla3_1["text"]
    texto5 = casilla4_1["text"]
    texto6 = casilla5_2["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto5 != "":
        if texto1 > texto5:
            return menor(casilla5_1)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_1)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_1)
        
def cambio1_2_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_2.config(text=numero_manejado)        
    texto1 = casilla1_2["text"]   
    texto2 = casilla2_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_3["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto6 != "":
        if texto1 > texto6:
            return menor(casilla1_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_2)
        
def cambio2_2_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_2.config(text=numero_manejado)        
    texto1 = casilla2_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_3["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_2)
        
def cambio3_2_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_2.config(text=numero_manejado)
    texto1 = casilla3_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla2_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_3["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto7 != "":
        if texto1 < texto7:
            return mayor(casilla3_2)
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_2)
        
def cambio4_2_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_2.config(text=numero_manejado)
    texto1 = casilla4_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla2_2["text"]
    texto5 = casilla5_2["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_3["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla4_2)
    if texto5 != "":
        if texto1 < texto5:
            return mayor(casilla4_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_2)
        
def cambio5_2_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_2.config(text=numero_manejado)
    texto1 = casilla5_2["text"]   
    texto2 = casilla1_2["text"]
    texto3 = casilla3_2["text"]
    texto4 = casilla4_2["text"]
    texto5 = casilla2_2["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_3["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto4 != "":
        if texto1 > texto4:
            return menor(casilla5_2)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_2)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_2)
        
def cambio1_3_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_3.config(text=numero_manejado)
    texto1 = casilla1_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_4["text"]
    texto9 = casilla1_5["text"]
    if texto2 != "":
        if texto1 > texto2:
            return menor(casilla1_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_3)

def cambio2_3_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_3.config(text=numero_manejado)
    texto1 = casilla2_3["text"]   
    texto2 = casilla1_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_4["text"]
    texto9 = casilla2_5["text"]
    if texto2 != "":
        if texto1 < texto2:
            return mayor(casilla2_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_3)
        
def cambio3_3_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_3.config(text=numero_manejado)
    texto1 = casilla3_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla1_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_4["text"]
    texto9 = casilla3_5["text"]
    if texto8 != "":
        if texto1 > texto8:
            return menor(casilla3_3)
    if texto7 != "":
        if texto1 > texto7:
            return menor(casilla3_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_3)
        
def cambio4_3_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_3.config(text=numero_manejado)
    texto1 = casilla4_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla1_3["text"]
    texto5 = casilla5_3["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_4["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_3)
        
def cambio5_3_3_dificil():
    global numero_manejado
    if numero_manejado != 0:
        casilla5_3.config(text=numero_manejado)
    texto1 = casilla5_3["text"]   
    texto2 = casilla2_3["text"]
    texto3 = casilla3_3["text"]
    texto4 = casilla4_3["text"]
    texto5 = casilla1_3["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_4["text"]
    texto9 = casilla5_5["text"]
    if texto8 != "":
        if texto1 > texto8:
            return menor(casilla5_3)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_3)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_3)
        
def cambio1_4_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_4.config(text=numero_manejado)
    texto1 = casilla1_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_4)
        
def cambio2_4_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_4.config(text=numero_manejado)
    texto1 = casilla2_4["text"]   
    texto2 = casilla1_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_5["text"]    
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_4)
        
def cambio3_4_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_4.config(text=numero_manejado)
    texto1 = casilla3_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla1_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_5["text"]
    if texto8 != "":
        if texto1 < texto8:
            return mayor(casilla3_4)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_4)
        
def cambio4_4_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_4.config(text=numero_manejado)
    texto1 = casilla4_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla1_4["text"]
    texto5 = casilla5_4["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_5["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_4)
        
def cambio5_4_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_4.config(text=numero_manejado)
    texto1 = casilla5_4["text"]   
    texto2 = casilla2_4["text"]
    texto3 = casilla3_4["text"]
    texto4 = casilla4_4["text"]
    texto5 = casilla1_4["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_5["text"]
    if texto8 != "":
        if texto1 < texto8:
            return mayor(casilla5_4)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_4)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_4)
        
def cambio1_5_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla1_5.config(text=numero_manejado)
    texto1 = casilla1_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla1_1["text"]
    texto7 = casilla1_2["text"]
    texto8 = casilla1_3["text"]
    texto9 = casilla1_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla1_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla1_5)
        
def cambio2_5_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla2_5.config(text=numero_manejado)
    texto1 = casilla2_5["text"]   
    texto2 = casilla1_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla2_1["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla2_3["text"]
    texto9 = casilla2_4["text"]
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla2_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla2_5)
        
def cambio3_5_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla3_5.config(text=numero_manejado)
    texto1 = casilla3_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla1_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla3_1["text"]
    texto7 = casilla3_2["text"]
    texto8 = casilla3_3["text"]
    texto9 = casilla3_4["text"]
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla3_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla3_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla3_5)
        
def cambio4_5_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla4_5.config(text=numero_manejado)
    texto1 = casilla4_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla1_5["text"]
    texto5 = casilla5_5["text"]
    texto6 = casilla4_1["text"]
    texto7 = casilla4_2["text"]
    texto8 = casilla4_3["text"]
    texto9 = casilla4_4["text"]
    if texto5 != "":
        if texto1 > texto5:
            return menor(casilla4_5)
    if texto3 != "":
        if texto1 > texto3:
            return menor(casilla4_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla4_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla4_5)
        
def cambio5_5_3_dificil():
    global numero_manejado
    if numero_manejado == 0:
        return messagebox.showinfo(message="DEBE SELECCIONAR UN DIGITO PRIMERO")
    if numero_manejado != 0:
        casilla5_5.config(text=numero_manejado)
    texto1 = casilla5_5["text"]   
    texto2 = casilla2_5["text"]
    texto3 = casilla3_5["text"]
    texto4 = casilla4_5["text"]
    texto5 = casilla1_5["text"]
    texto6 = casilla5_1["text"]
    texto7 = casilla5_2["text"]
    texto8 = casilla5_3["text"]
    texto9 = casilla5_4["text"]
    if texto4 != "":
        if texto1 < texto4:
            return mayor(casilla5_5)
    if texto1==texto2 or texto1==texto3 or texto1==texto4 or texto1==texto5:
        return fila(casilla5_5)
    if texto1==texto6 or texto1==texto7 or texto1==texto8 or texto1==texto9:
        return columna(casilla5_5)
                
#=======================================================================================================#

def numero_fijo():
    mensaje = messagebox.showinfo(message="ERROR, ES UN NUMERO FIJO")

def menor(x):
    x.config(bg="red")
    x.config(text="")
    mensaje = messagebox.showinfo(message="ERROR, EL NUMERO DEBE DE SER MENOR")
    if mensaje == "ok":
        quitar_color(x)
        
def mayor(x):
    x.config(bg="red")
    x.config(text="")
    mensaje = messagebox.showinfo(message="ERROR, EL NUMERO DEBE DE SER MAYOR")
    if mensaje == "ok":
        quitar_color(x)

def fila(x):
    x.config(bg="red")
    x.config(text="")
    mensaje = messagebox.showinfo(message="ERROR, EL NUMERO YA ESTA EN LA FILA")
    if mensaje == "ok":
        quitar_color(x)

def columna(x):
    x.config(bg="red")
    x.config(text="")
    mensaje = messagebox.showinfo(message="ERROR, EL NUMERO YA ESTA EN LA COLUMNA")
    if mensaje == "ok":
        quitar_color(x)
        
def quitar_color(x):
    x.config(bg="SystemButtonFace")

#=======================================================================================================#
        
def activado_1():
    global botton_num_1
    global botton_num_2
    global botton_num_3
    global botton_num_4
    global botton_num_5
    global numero_manejado
    global iniciar_activado

    if iniciar_activado != True:
        return messagebox.showinfo(message="DEBE INICIAR JUEGO PRIMERO PARA COMENZAR")
    botton_num_1.config(bg="#66FF45")
    botton_num_2.config(bg="SystemButtonFace")
    botton_num_3.config(bg="SystemButtonFace")
    botton_num_4.config(bg="SystemButtonFace")
    botton_num_5.config(bg="SystemButtonFace")
    numero_manejado = 1
    
def activado_2():
    global botton_num_1
    global botton_num_2
    global botton_num_3
    global botton_num_4
    global botton_num_5
    global numero_manejado
    global iniciar_activado

    if iniciar_activado != True:
        return messagebox.showinfo(message="DEBE INICIAR JUEGO PRIMERO PARA COMENZAR")
    botton_num_1.config(bg="SystemButtonFace")
    botton_num_2.config(bg="#66FF45")
    botton_num_3.config(bg="SystemButtonFace")
    botton_num_4.config(bg="SystemButtonFace")
    botton_num_5.config(bg="SystemButtonFace")
    numero_manejado = 2

def activado_3():
    global botton_num_1
    global botton_num_2
    global botton_num_3
    global botton_num_4
    global botton_num_5
    global numero_manejado
    global iniciar_activado

    if iniciar_activado != True:
        return messagebox.showinfo(message="DEBE INICIAR JUEGO PRIMERO PARA COMENZAR")
    botton_num_1.config(bg="SystemButtonFace")
    botton_num_2.config(bg="SystemButtonFace")
    botton_num_3.config(bg="#66FF45")
    botton_num_4.config(bg="SystemButtonFace")
    botton_num_5.config(bg="SystemButtonFace")
    numero_manejado = 3

def activado_4():
    global botton_num_1
    global botton_num_2
    global botton_num_3
    global botton_num_4
    global botton_num_5
    global numero_manejado
    global iniciar_activado

    if iniciar_activado != True:
        return messagebox.showinfo(message="DEBE INICIAR JUEGO PRIMERO PARA COMENZAR")
    botton_num_1.config(bg="SystemButtonFace")
    botton_num_2.config(bg="SystemButtonFace")
    botton_num_3.config(bg="SystemButtonFace")
    botton_num_4.config(bg="#66FF45")
    botton_num_5.config(bg="SystemButtonFace")
    numero_manejado = 4
    
def activado_5():
    global botton_num_1
    global botton_num_2
    global botton_num_3
    global botton_num_4
    global botton_num_5
    global numero_manejado
    global iniciar_activado

    if iniciar_activado != True:
        return messagebox.showinfo(message="DEBE INICIAR JUEGO PRIMERO PARA COMENZAR")
    botton_num_1.config(bg="SystemButtonFace")
    botton_num_2.config(bg="SystemButtonFace")
    botton_num_3.config(bg="SystemButtonFace")
    botton_num_4.config(bg="SystemButtonFace")
    botton_num_5.config(bg="#66FF45")
    numero_manejado = 5

#=======================================================================================================#

def inicio():
    
    global iniciar_activado
    global desactivar
    global botton_pri_1
    global botton_pri_2
    global botton_pri_3
    global botton_pri_4
    global jugador
    global control_reloj
    global botton_timer
    global top_10_facil
    global top_10_medio
    global top_10_dificil
    global texto
    global botton_guardar
    global botton_cargar
    
    if control_reloj == "Timer":
        if botton_timer["state"] != "disabled":
            return messagebox.showinfo(message="DEBE CONFIGURAR EL TIMER PRIMERO")
    
    texto = str(jugador.get())
    
    if texto == "":
        return messagebox.showinfo(message="DEBE DIGITAR UN NOMBRE PRIMERO")
    if len(texto) > 20:
        return messagebox.showinfo(message="EL NOMBRE DEBE DE ESTAR ENRTE 1 Y 20 CARACTERES")

    for elemento in top_10_facil:
        if elemento[0] == texto:
            return messagebox.showinfo(message="EL NOMBRE YA SE ENCUENTRA EN EL TOP")

    for elemento in top_10_medio:
        if elemento[0] == texto:
            return messagebox.showinfo(message="EL NOMBRE YA SE ENCUENTRA EN EL TOP")

    for elemento in top_10_dificil:
        if elemento[0] == texto:
            return messagebox.showinfo(message="EL NOMBRE YA SE ENCUENTRA EN EL TOP")
    
    iniciar_activado = True

    botton_cargar["state"] = "disabled"
    botton_guardar["state"] = "normal"
    
    botton_pri_2["state"] = "normal"
    botton_pri_3["state"] = "normal"
    botton_pri_4["state"] = "normal"
    botton_pri_1["state"] = "disabled"
 
    tiempo()
    

def tiempo():

    global hora_numero
    global minuto_numero
    global segundo_numero
    global desactivar
    global iniciar_activado
    global control_reloj
    global hora_si_terminado
    global minuto_si_terminado
    global segundo_si_terminado
    global parada_final
    global juego_cargado

    if iniciar_activado == True:
        if control_reloj == "No":
            return messagebox.showinfo(message="NO ESTA PARTICIPANDO PARA EL TOP 10")
        segundo = segundo_numero["text"]   
        minuto = minuto_numero["text"]
        hora = hora_numero["text"]
        
        if control_reloj == "Si":
            if segundo == 59:
                minuto_numero.config(text=minuto+1)
                segundo = -1       
                if minuto == 59:
                    hora_numero.config(text=hora+1)
                    minuto = -1
                    minuto_numero.config(text=minuto+1)
            segundo_numero.config(text=segundo+1)

            if parada_final != True:           
                actualizar = tkinter.Label()
                actualizar.after(1000,tiempo)

        if control_reloj == "Timer":
            if segundo == 0 and minuto == 0 and hora == 0:
                mensaje = messagebox.askquestion(message="SE HA ACABADO EL TIEMPO, ¿DESEA CONTINUAR?")
                if mensaje == "no":
                    ventana_jugar.destroy()
                    return jugar()
                if mensaje == "yes":
                    control_reloj = "Si"
                    minuto_numero.config(text=minuto_si_terminado)
                    segundo_numero.config(text=segundo_si_terminado)
                    hora_numero.config(text=hora_si_terminado) 
                    return tiempo()
            if segundo == 0:
                minuto_numero.config(text=minuto-1)
                segundo = 60       
                if minuto == 0:
                    hora_numero.config(text=hora-1)
                    minuto = 60
                    minuto_numero.config(text=minuto-1)
            segundo_numero.config(text=segundo-1)

            if parada_final != True:
                actualizar = tkinter.Label()
                actualizar.after(1000,tiempo)

    if juego_cargado == False:
        if iniciar_activado == False:
            minuto_numero.config(text=0)
            segundo_numero.config(text=0)
            hora_numero.config(text=0)
        
    juego_cargado = False

def borrar_el_juego(ventana_jugar):

    global borrar
    global iniciar_activado

    borrar = True

    if iniciar_activado == True:
        mensaje = messagebox.askquestion(message="¿ESTÁ SEGURO DE BORRAR EL JUEGO?")
        if mensaje == "yes":
            ventana_jugar.destroy()        
            return jugar()

def terminar_juego(ventana_jugar):
    global iniciar_activado
    if iniciar_activado == True:
        mensaje = messagebox.askquestion(message="¿ESTÁ SEGURO DE TERMINAR EL JUEGO?")
        if mensaje == "yes":
            ventana_jugar.destroy()        
            return jugar()

def regreso(x,y):
    
    global juego_cargado
    juego_cargado = False

    x.destroy()
    y.deiconify()

def confirmar():
    global entrada_hora
    global entrada_minuto
    global entrada_segundo
    global hora_numero
    global minuto_numero
    global segundo_numero
    global botton_timer
    global hora_si_terminado
    global minuto_si_terminado
    global segundo_si_terminado

    hora = entrada_hora.get()
    minuto = entrada_minuto.get()
    segundo = entrada_segundo.get()

    if hora == "":
        hora = 0
    if minuto == "":
        minuto = 0
    if segundo == "":
        segundo = 0

    if hora == 0 and minuto == 0 and segundo == 0:
        return messagebox.showinfo(message="DEBE DIGITAR UN TIEMPO VALIDO")

    hora = int(hora)
    minuto = int(minuto)
    segundo = int(segundo)
    
    if hora < 0 or hora > 2:
        return messagebox.showinfo(message="LAS HORAS DEBEN ESTAR ENTRE 0 Y 2")
    if minuto < 0 or minuto > 59:
        return messagebox.showinfo(message="LOS MINUTOS DEBEN DE ESTAR ENTRE 0 Y 59")
    if segundo < 0 or segundo > 59:
        return messagebox.showinfo(message="LOS SEGUNDOS DEBEN DE ESTAR ENTRE 0 Y 59")

    hora_numero.config(text=hora)
    minuto_numero.config(text=minuto)
    segundo_numero.config(text=segundo)

    hora_si_terminado = hora
    minuto_si_terminado = minuto
    segundo_si_terminado = segundo
    
    botton_timer["state"] = "disabled"

#=======================================================================================================#

def salir_top(x):

    global parada_final

    parada_final = False
    x.destroy()

    tiempo()
    
def top_10_todos():

    global top_10_facil
    global top_10_medio
    global top_10_dificil
    global parada_final
    global archiv_top

    ventana_top = tkinter.Tk()
    ventana_top.title("LOS MEJORES")
    ventana_top.geometry("604x300")
    ventana_top.config(bg="#E8FFF0")

    borde2 = tkinter.Canvas(ventana_top,bg="#B3DDFF",height=300,width=150)
    borde2.place(x=0,y=30)

    borde3 = tkinter.Canvas(ventana_top,bg="#BEF7FF",height=300,width=150)
    borde3.place(x=150,y=30)

    borde3 = tkinter.Canvas(ventana_top,bg="#BEFFDC",height=300,width=150)
    borde3.place(x=300,y=30)

    borde4 = tkinter.Canvas(ventana_top,bg="#BEFFC9",height=300,width=150)
    borde4.place(x=450,y=30)

    borde1 = tkinter.Canvas(ventana_top,bg="#E5E5E5",height=24,width=700)
    borde1.place(x=-10,y=6)

    borde0 = tkinter.Canvas(ventana_top,bg="#E5E5E5",height=223,width=700)
    borde0.place(x=-10,y=40)

    parada_final = True

    salida = tkinter.Button(ventana_top,bg="#CDE8FF",text="Regresar",command=lambda: salir_top(ventana_top))
    salida.place(x=5,y=270)

    y_todos = 40
    nivel_facil = tkinter.Label(ventana_top,text="NIVEL FACIL:",bg="#E5E5E5")
    nivel_facil.place(x=10,y=10)
    
    for ind, elemento in enumerate(top_10_facil,start=1):
        clock = ""
        for x in elemento[1:]:
            clock = clock+str(x)
    
        top_facil = tkinter.Label(ventana_top,text=str(ind)+" - "+elemento[0]+" - "+clock,bg="#E5E5E5")
        top_facil.place(x=40,y=y_todos)
        y_todos+=20

    y_todos = 40
    nivel_medio = tkinter.Label(ventana_top,text="NIVEL MEDIO:",bg="#E5E5E5")
    nivel_medio.place(x=240,y=10)
    
    for ind, elemento in enumerate(top_10_medio,start=1):
        clock = ""
        for x in elemento[1:]:
            clock = clock+str(x)
            
        top_medio = tkinter.Label(ventana_top,text=str(ind)+" - "+elemento[0]+" - "+clock,bg="#E5E5E5")
        top_medio.place(x=270,y=y_todos)
        y_todos+=20

    y_todos = 40
    nivel_dificil = tkinter.Label(ventana_top,text="NIVEL DIFICIL:",bg="#E5E5E5")
    nivel_dificil.place(x=470,y=10)
    
    for ind, elemento in enumerate(top_10_dificil,start=1):
        clock = ""
        for x in elemento[1:]:
            clock = clock+str(x)
            
        top_medio = tkinter.Label(ventana_top,text=str(ind)+" - "+elemento[0]+" - "+clock,bg="#E5E5E5")
        top_medio.place(x=500,y=y_todos)
        y_todos+=20

    archiv_top =open("futoshiki2021top10.dat","w")

    archiv_top.write("\nFacil: " + str(top_10_facil))
    archiv_top.write("\nMedio: " + str(top_10_medio))
    archiv_top.write("\nDificl: " + str(top_10_dificil))
    archiv_top.close()
    

#=======================================================================================================#
def guardar_game():

    global casilla1_1
    global casilla2_1
    global casilla3_1
    global casilla4_1
    global casilla5_1
    global casilla1_2
    global casilla2_2
    global casilla3_2
    global casilla4_2
    global casilla5_2
    global casilla1_3
    global casilla2_3
    global casilla3_3
    global casilla4_3
    global casilla5_3
    global casilla1_4
    global casilla2_4
    global casilla3_4
    global casilla4_4
    global casilla5_4
    global casilla1_5
    global casilla2_5
    global casilla3_5
    global casilla4_5
    global casilla5_5

    global guardar_casilla1_1
    global guardar_casilla2_1
    global guardar_casilla3_1
    global guardar_casilla4_1
    global guardar_casilla5_1
    global guardar_casilla1_2
    global guardar_casilla2_2
    global guardar_casilla3_2
    global guardar_casilla4_2
    global guardar_casilla5_2
    global guardar_casilla1_3
    global guardar_casilla2_3
    global guardar_casilla3_3
    global guardar_casilla4_3
    global guardar_casilla5_3
    global guardar_casilla1_4
    global guardar_casilla2_4
    global guardar_casilla3_4
    global guardar_casilla4_4
    global guardar_casilla5_4
    global guardar_casilla1_5
    global guardar_casilla2_5
    global guardar_casilla3_5
    global guardar_casilla4_5
    global guardar_casilla5_5

    global guardar_dificultad
    global guardar_control_reloj
    global guardar_panel
    global guardar_suerte
    
    global dificultad
    global control_reloj
    global panel
    global suerte

    global hora_numero
    global minuto_numero
    global segundo_numero

    global guardar_hora
    global guardar_minuto
    global guardar_segundo

    global desplegar

    guardar_casilla1_1 = casilla1_1["text"]
    guardar_casilla1_2 = casilla1_2["text"]
    guardar_casilla1_3 = casilla1_3["text"]
    guardar_casilla1_4 = casilla1_4["text"]
    guardar_casilla1_5 = casilla1_5["text"]
    guardar_casilla2_1 = casilla2_1["text"]
    guardar_casilla2_2 = casilla2_2["text"]
    guardar_casilla2_3 = casilla2_3["text"]
    guardar_casilla2_4 = casilla2_4["text"]
    guardar_casilla2_5 = casilla2_5["text"]
    guardar_casilla3_1 = casilla3_1["text"]
    guardar_casilla3_2 = casilla3_2["text"]
    guardar_casilla3_3 = casilla3_3["text"]
    guardar_casilla3_4 = casilla3_4["text"]
    guardar_casilla3_5 = casilla3_5["text"]
    guardar_casilla4_1 = casilla4_1["text"]
    guardar_casilla4_2 = casilla4_2["text"]
    guardar_casilla4_3 = casilla4_3["text"]
    guardar_casilla4_4 = casilla4_4["text"]
    guardar_casilla4_5 = casilla4_5["text"]
    guardar_casilla5_1 = casilla5_1["text"]
    guardar_casilla5_2 = casilla5_2["text"]
    guardar_casilla5_3 = casilla5_3["text"]
    guardar_casilla5_4 = casilla5_4["text"]
    guardar_casilla5_5 = casilla5_5["text"]

    guardar_dificultad = dificultad
    guardar_control_reloj = control_reloj
    guardar_panel = panel
    guardar_suerte = suerte

    guardar_hora = hora_numero["text"]
    guardar_minuto = minuto_numero["text"]
    guardar_segundo = segundo_numero["text"]

    archiv_juego =open("futoshiki2021juegoactual.dat","w")

    archiv_juego.write("\nCasilla1_1: " + str(guardar_casilla1_1))
    archiv_juego.write("\nCasilla1_2: " + str(guardar_casilla1_2))
    archiv_juego.write("\nCasilla1_3: " + str(guardar_casilla1_3))
    archiv_juego.write("\nCasilla1_4: " + str(guardar_casilla1_4))
    archiv_juego.write("\nCasilla1_5: " + str(guardar_casilla1_5))
    archiv_juego.write("\nCasilla2_1: " + str(guardar_casilla2_1))
    archiv_juego.write("\nCasilla2_2: " + str(guardar_casilla2_2))
    archiv_juego.write("\nCasilla2_3: " + str(guardar_casilla2_3))
    archiv_juego.write("\nCasilla2_4: " + str(guardar_casilla2_4))
    archiv_juego.write("\nCasilla2_5: " + str(guardar_casilla2_5))
    archiv_juego.write("\nCasilla3_1: " + str(guardar_casilla3_1))
    archiv_juego.write("\nCasilla3_2: " + str(guardar_casilla3_2))
    archiv_juego.write("\nCasilla3_3: " + str(guardar_casilla3_3))
    archiv_juego.write("\nCasilla3_4: " + str(guardar_casilla3_4))
    archiv_juego.write("\nCasilla3_5: " + str(guardar_casilla3_5))
    archiv_juego.write("\nCasilla4_1: " + str(guardar_casilla4_1))
    archiv_juego.write("\nCasilla4_2: " + str(guardar_casilla4_2))
    archiv_juego.write("\nCasilla4_3: " + str(guardar_casilla4_3))
    archiv_juego.write("\nCasilla4_4: " + str(guardar_casilla4_4))
    archiv_juego.write("\nCasilla4_5: " + str(guardar_casilla4_5))
    archiv_juego.write("\nCasilla5_1: " + str(guardar_casilla5_1))
    archiv_juego.write("\nCasilla5_2: " + str(guardar_casilla5_2))
    archiv_juego.write("\nCasilla5_3: " + str(guardar_casilla5_3))
    archiv_juego.write("\nCasilla5_4: " + str(guardar_casilla5_4))
    archiv_juego.write("\nCasilla5_5: " + str(guardar_casilla5_5))
    
    archiv_juego.write("\nReloj: " + guardar_control_reloj)
    archiv_juego.write("\nPanel: " + guardar_panel)
    archiv_juego.write("\nSuerte: " + str(guardar_suerte))

    archiv_juego.close()

    desplegar += 1

def cargar_game(x):
    
    global guardar_dificultad
    global guardar_control_reloj
    global guardar_panel
    global guardar_suerte
    
    global dificultad
    global control_reloj
    global panel
    global suerte

    global hora_numero
    global minuto_numero
    global segundo_numero

    global guardar_hora
    global guardar_minuto
    global guardar_segundo 

    global juego_cargado

    if desplegar == 0:
        return messagebox.showinfo(message="NADA PARA DESPLEGAR")

    juego_cargado = True

    dificultad = guardar_dificultad
    control_reloj = guardar_control_reloj
    panel = guardar_panel
    suerte = guardar_suerte
    hora_numero = guardar_hora
    minuto_numero = guardar_minuto
    segundo_numero = guardar_segundo

    x.destroy()
    jugar()

def jugar():
    
    global dificultad
    global ventana
    global botton_num_1
    global botton_num_2
    global botton_num_3
    global botton_num_4
    global botton_num_5
    global panel
    global control_reloj
    global hora_numero
    global minuto_numero
    global segundo_numero
    global suerte
    global desactivar
    global iniciar_activado
    global ventana_jugar
    global numero_manejado
    global borrar
    global botton_pri_1
    global botton_pri_2
    global botton_pri_3
    global botton_pri_4
    global jugador
    global entrada_hora
    global entrada_minuto
    global entrada_segundo
    global botton_timer
    global parada_final
    global guardar_suerte
    global juego_cargado
    global guardar_hora
    global guardar_minuto
    global guardar_segundo
    global botton_guardar
    global botton_cargar
    
    ventana.state(newstate="withdraw")
    ventana_jugar = tkinter.Tk()
    ventana_jugar.title("JUGAR")
    ventana_jugar.geometry("578x700")
    ventana_jugar.config(bg="#FFECEC")

    iniciar_activado = False
    parada_final = False
    desactivar = 0
    numero_manejado = 0

    borde1 = tkinter.Canvas(ventana_jugar, bg="#FFEA82", height=43, width=181).place(x=195,y=30)    
    borde2 = tkinter.Canvas(ventana_jugar, bg="#B9FFDE", height=20, width=193).place(x=0,y=40)
    borde3 = tkinter.Canvas(ventana_jugar, bg="#FFB9FE", height=20, width=193).place(x=381,y=40)

    futoshiki = tkinter.Label(ventana_jugar, text="FUTOSHIKI", font=("Times", "24", "bold italic"), fg="white")
    futoshiki.config(bg="#AAAAAA")
    futoshiki.place(x=200,y=30)

    jugador = tkinter.Entry(ventana_jugar, width=30)
    jugador.place(x=198, y=120)    

    enunciado1 = tkinter.Label(ventana_jugar, text="Nombre del jugador:",bg="#FFECEC").place(x=70,y=120)
    enunciado2 = tkinter.Label(ventana_jugar, text="NIVEL "+ dificultad,bg="#FFECEC").place(x=255, y=95)

    if panel == "Derecha":
        botton_num_1 = tkinter.Button(ventana_jugar, text="1", height=2, width=5, command=activado_1)
        botton_num_1.place(x=487,y=200)
        botton_num_2 = tkinter.Button(ventana_jugar, text="2", height=2, width=5, command=activado_2)
        botton_num_2.place(x=487,y=240)
        botton_num_3 = tkinter.Button(ventana_jugar, text="3", height=2, width=5, command=activado_3)
        botton_num_3.place(x=487,y=280)
        botton_num_4 = tkinter.Button(ventana_jugar, text="4", height=2, width=5, command=activado_4)
        botton_num_4.place(x=487,y=320)  
        botton_num_5 = tkinter.Button(ventana_jugar, text="5", height=2, width=5, command=activado_5)
        botton_num_5.place(x=487,y=360)
    if panel == "Izquierda":
        botton_num_1 = tkinter.Button(ventana_jugar, text="1", height=2, width=5, command=activado_1)
        botton_num_1.place(x=50,y=200)
        botton_num_2 = tkinter.Button(ventana_jugar, text="2", height=2, width=5, command=activado_2)
        botton_num_2.place(x=50,y=240)
        botton_num_3 = tkinter.Button(ventana_jugar, text="3", height=2, width=5, command=activado_3)
        botton_num_3.place(x=50,y=280)
        botton_num_4 = tkinter.Button(ventana_jugar, text="4", height=2, width=5, command=activado_4)
        botton_num_4.place(x=50,y=320)  
        botton_num_5 = tkinter.Button(ventana_jugar, text="5", height=2, width=5, command=activado_5)
        botton_num_5.place(x=50,y=360)

    if control_reloj == "Si" or control_reloj == "Timer":
        fondo = tkinter.Canvas(ventana_jugar,bg="#FFEA82", height=70, width=182)
        fondo.place(x=30,y=560)
        horas_reloj = tkinter.Label(ventana_jugar, text="Horas",bg="#99FFA6",width=8)
        horas_reloj.place(x=32,y=550)
        minutos_reloj = tkinter.Label(ventana_jugar, text="Minutos",bg="#B9FFDE",width=8)
        minutos_reloj.place(x=92,y=550)
        segundos_reloj = tkinter.Label(ventana_jugar, text="Segundos",bg="#FFB9FE",width=8)
        segundos_reloj.place(x=152,y=550)

        hora_numero = tkinter.Label(ventana_jugar, text=0,bg="#FFEA82")
        hora_numero.place(x=58,y=590)
        minuto_numero = tkinter.Label(ventana_jugar, text=0,bg="#FFEA82")
        minuto_numero.place(x=118,y=590)
        segundo_numero = tkinter.Label(ventana_jugar, text=0,bg="#FFEA82")
        segundo_numero.place(x=178,y=590)

    if control_reloj == "Timer":
        entrada_hora = tkinter.Entry(ventana_jugar,width=10)
        entrada_hora.place(x=33,y=650)
        entrada_minuto = tkinter.Entry(ventana_jugar,width=10)
        entrada_minuto.place(x=90,y=650)
        entrada_segundo = tkinter.Entry(ventana_jugar,width=10)
        entrada_segundo.place(x=153,y=650)
        botton_timer = tkinter.Button(ventana_jugar,text="Timer",bg="#FFEA82",command=confirmar)
        botton_timer.place(x=220,y=647)

    botton_guardar = tkinter.Button(ventana_jugar,text="Guardar Juego",bg="#AAAAAA",width=20,fg="white",command=guardar_game)
    botton_guardar.place(x=325,y=560)
    botton_guardar["state"] = "disabled"

    botton_cargar = tkinter.Button(ventana_jugar,text="Cargar Juego",bg="#AAAAAA",width=20,fg="white",command=lambda: cargar_game(ventana_jugar))
    botton_cargar.place(x=325,y=600)

    botton_pri_1 = tkinter.Button(ventana_jugar, text="INICIAR JUEGO", height=2, width=13, bg="#99FFA6", command=inicio)
    botton_pri_1.place(x=20, y=480)
    botton_pri_2 = tkinter.Button(ventana_jugar, text="BORRAR JUGADA", height=2, width=13, bg="#FFB9FE")
    botton_pri_2.place(x=130, y=480)
    botton_pri_2["state"] = "disabled"
    botton_pri_3 = tkinter.Button(ventana_jugar, text="TERMINAR JUEGO", height=2, width=13, bg="#B9FFDE", command=lambda: terminar_juego(ventana_jugar))
    botton_pri_3.place(x=240, y=480)
    botton_pri_3["state"] = "disabled"
    botton_pri_4 = tkinter.Button(ventana_jugar, text="BORRAR JUEGO", height=2, width=13, bg="#FFB9FE",command=lambda: borrar_el_juego(ventana_jugar))
    botton_pri_4.place(x=350, y=480)
    botton_pri_4["state"] = "disabled"
    botton_pri_5 = tkinter.Button(ventana_jugar, text="TOP 10", height=2, width=13, bg="#99FFA6", command=top_10_todos)
    botton_pri_5.place(x=460, y=480)

    botton_regreso = tkinter.Button(ventana_jugar,text="X",command=lambda: regreso(ventana_jugar,ventana))
    botton_regreso.place(x=558,y=65)

    if borrar == False:
        suerte = random.randint(1,3)

    if juego_cargado == True:
        suerte = guardar_suerte
        hora_numero.config(text=int(guardar_hora))
        minuto_numero.config(text=int(guardar_minuto))
        segundo_numero.config(text=int(guardar_segundo))
        if control_reloj == "Timer":
            botton_timer["state"] = "disabled"
        
    if borrar == True:
        borrar = False

    if dificultad == "FACIL":
        if suerte == 1:
            juego_facil_1(ventana_jugar)
        elif suerte == 2:
            juego_facil_2(ventana_jugar)
        elif suerte == 3:
            juego_facil_3(ventana_jugar)
    if dificultad == "MEDIO":
        if suerte == 1:
            juego_intermedio_1(ventana_jugar)
        if suerte == 2:
            juego_intermedio_2(ventana_jugar)
        if suerte == 3:
            juego_intermedio_3(ventana_jugar)
    if dificultad == "DIFICIL":
        if suerte == 1:
            juego_dificil_1(ventana_jugar)
        if suerte == 2:
            juego_dificil_2(ventana_jugar)
        if suerte == 3:
            juego_dificil_3(ventana_jugar)

    return ganador()
        
#==============================================CONFIGURACION============================================#

def config():

    global ventana
    global dificultad
    global control_reloj
    global panel

    archiv_config =open("futoshiki2021configuración.dat","w")

    archiv_config.write("\nNivel: " + dificultad)
    archiv_config.write("\nReloj: " + control_reloj)
    archiv_config.write("\nPanel: " + panel)

    archiv_config.close()
      
    ventana.state(newstate="withdraw")
    ventana_config = tkinter.Tk()
    ventana_config.title("REALIZAR CONFIGURACIONES")
    ventana_config.geometry("300x350")
    ventana_config.config(bg="#FFFFD8")

    borde8 = tkinter.Canvas(ventana_config,bg="#8E8E8E",height=25,width=400)
    borde8.place(x=-10,y=10)
    
    menu = tkinter.Label(ventana_config,text="CONFIGURACION",font=15,bg="#8E8E8E",fg="white")
    menu.place(x=20,y=13)

    borde6 = tkinter.Canvas(ventana_config,bg="#AA94FF",height=200,width=90)
    borde6.place(x=37,y=280)

    borde5 = tkinter.Canvas(ventana_config,bg="#C8B9FF",height=22,width=400)
    borde5.place(x=-10,y=258)

    borde4 = tkinter.Canvas(ventana_config,bg="#C6FD80",height=80,width=90)
    borde4.place(x=37,y=175)

    borde3 = tkinter.Canvas(ventana_config,bg="#E0FFB9",height=22,width=400)
    borde3.place(x=-10,y=153)

    borde7 = tkinter.Canvas(ventana_config,bg="#E0FFB9",height=22,width=300)
    borde7.place(x=120,y=206)

    anuncio = tkinter.Label(ventana_config,text="No participa en el Top 10",bg="#E0FFB9")
    anuncio.place(x=130,y=209)

    borde2 = tkinter.Canvas(ventana_config,bg="#FD8080",height=80,width=90)
    borde2.place(x=37,y=70)

    borde1 = tkinter.Canvas(ventana_config,bg="#FFB1B1",height=22,width=400)
    borde1.place(x=-10,y=47)

    botton_regreso = tkinter.Button(ventana_config,text="x",command=lambda: regreso(ventana_config,ventana))
    botton_regreso.config(bg="#FD8080",width=2,height=1)
    botton_regreso.place(x=276,y=47)

    nivel = tkinter.Label(ventana_config, text="Nivel:",bg="#FFB1B1").place(x=50,y=50)
    reloj = tkinter.Label(ventana_config, text="Reloj:",bg="#E0FFB9").place(x=50,y=155)
    digitos = tkinter.Label(ventana_config, text="Panel de Digitos:",bg="#C8B9FF").place(x=50,y=260)

    facil = tkinter.Checkbutton(ventana_config,bg="#FD8080", text="Facil",command=lambda: actualizar_difi_1(facil,medio,dificil))
    facil.place(x=50,y=75)
    medio = tkinter.Checkbutton(ventana_config,bg="#FD8080", text="Medio",command=lambda: actualizar_difi_2(medio,facil,dificil))
    medio.place(x=50,y=100)
    dificil = tkinter.Checkbutton(ventana_config,bg="#FD8080", text="Dificil",command=lambda: actualizar_difi_3(dificil,facil,medio))
    dificil.place(x=50,y=125)

    reloj_si = tkinter.Checkbutton(ventana_config,bg="#C6FD80", text="Si",command=lambda: actualizar_reloj_1(reloj_si,reloj_no,timer))
    reloj_si.place(x=50,y=180)
    reloj_no = tkinter.Checkbutton(ventana_config,bg="#C6FD80", text="No",command=lambda: actualizar_reloj_2(reloj_no,reloj_si,timer))
    reloj_no.place(x=50,y=205)
    timer = tkinter.Checkbutton(ventana_config,bg="#C6FD80", text="Timer",command=lambda: actualizar_reloj_3(timer,reloj_no,reloj_si))
    timer.place(x=50,y=230)

    panel_de = tkinter.Checkbutton(ventana_config,bg="#AA94FF", text="Derecha",command=lambda: actualizar_panel_1(panel_de,panel_iz))
    panel_de.place(x=50,y=285)
    panel_iz = tkinter.Checkbutton(ventana_config,bg="#AA94FF", text="Izquierda",command=lambda: actualizar_panel_2(panel_iz,panel_de))
    panel_iz.place(x=50,y=310)

    if dificultad == "FACIL":
        facil.select()
    if dificultad == "MEDIO":
        medio.select()
    if dificultad == "DIFICIL":
        dificil.select()

    if control_reloj == "Si":
        reloj_si.select()
    if control_reloj == "No":
        reloj_no.select()
    if control_reloj == "Timer":
        timer.select()

    if panel == "Derecha":
        panel_de.select()
    if panel == "Izquierda":
        panel_iz.select()

def actualizar_difi_1(x,y,z):

    global dificultad
    
    x.select()
    y.deselect()
    z.deselect()

    dificultad = "FACIL"

def actualizar_difi_2(x,y,z):

    global dificultad
    
    x.select()
    y.deselect()
    z.deselect()

    dificultad = "MEDIO"        
    
def actualizar_difi_3(x,y,z):

    global dificultad
    
    x.select()
    y.deselect()
    z.deselect()

    dificultad = "DIFICIL"

def actualizar_reloj_1(x,y,z):

    global control_reloj
    
    x.select()
    y.deselect()
    z.deselect()

    control_reloj = "Si"
    
def actualizar_reloj_2(x,y,z):

    global control_reloj
    
    x.select()
    y.deselect()
    z.deselect()

    control_reloj = "No"

def actualizar_reloj_3(x,y,z):

    global control_reloj
    
    x.select()
    y.deselect()
    z.deselect()

    control_reloj = "Timer"

def actualizar_panel_1(x,y):

    global panel
    
    x.select()
    y.deselect()

    panel = "Derecha"

def actualizar_panel_2(x,y):

    global panel
    
    x.select()
    y.deselect()

    panel = "Izquierda"
    
#=======================================================================================================#

def ganador():

    global hora_numero
    global minuto_numero
    global segundo_numero
    global ventana
    global ventana_jugar
    global numero_manejado
    global control_reloj
    global dificultad
    global top_10_facil
    global top_10_medio
    global top_10_dificil
    global texto
    global hora_si_terminado
    global minuto_si_terminado
    global segundo_si_terminado
    global parada_final

    texto1 = casilla1_1["text"]    
    texto2 = casilla2_1["text"]
    texto3 = casilla3_1["text"]
    texto4 = casilla4_1["text"]
    texto5 = casilla5_1["text"]
    texto6 = casilla1_2["text"]
    texto7 = casilla2_2["text"]
    texto8 = casilla3_2["text"]
    texto9 = casilla4_2["text"]
    texto10 = casilla5_2["text"]    
    texto11 = casilla1_3["text"]
    texto12 = casilla2_3["text"]
    texto13 = casilla3_3["text"]
    texto14 = casilla4_3["text"]
    texto15 = casilla5_3["text"]
    texto16 = casilla1_4["text"]
    texto17 = casilla2_4["text"]
    texto18 = casilla3_4["text"]
    texto19 = casilla4_4["text"]    
    texto20 = casilla5_4["text"]
    texto21 = casilla1_5["text"]
    texto22 = casilla2_5["text"]
    texto23 = casilla3_5["text"]
    texto24 = casilla4_5["text"]
    texto25 = casilla5_5["text"]

    terminado = tkinter.Label()
    if texto1 != "" and texto2 != "" and texto3 != "" and texto4 != "" and texto5 != "" and texto6 != "" and texto7 != "" \
    and texto8 != "" and texto9 != "" and texto10 != "" and texto11 != "" and texto12 != "" and texto13 != "" and texto14 != "" \
    and texto15 != "" and texto16 != "" and texto17 != "" and texto18 != "" and texto19 != "" and texto20 != "" and texto21 != "" \
    and texto22 != "" and texto23 != "" and texto24 != "" and texto25 != "":

        parada_final = True
        
        if segundo_numero != 0 and minuto_numero != 0 and hora_numero != 0:
            if control_reloj == "Si":
                segundo = segundo_numero["text"]   
                minuto = minuto_numero["text"]
                hora = hora_numero["text"]
                numero_manejado = 0
                tiempo_durado = str(hora)+" "+"HORAS CON"+" "+str(minuto)+" "+"MINUTOS Y"+" "+str(segundo)+" "+"SEGUNDOS"
                mensaje = messagebox.showinfo(message="¡EXCELENTE! JUEGO TERMINADO CON ÉXITO, HA TARDADO: "+tiempo_durado)
            if control_reloj == "Timer":
                segundo = int(segundo_numero["text"])
                minuto = int(minuto_numero["text"])*60
                hora = int(hora_numero["text"])*3600
                numero_manejado = 0
                hora_si_terminado = int(hora_si_terminado)*3600
                minuto_si_terminado = int(minuto_si_terminado)*60
                segundo_si_terminado = int(segundo_si_terminado)
                hora_si_terminado = hora_si_terminado-hora
                minuto_si_terminado = minuto_si_terminado-minuto
                segundo_si_terminado = segundo_si_terminado-segundo
                sumatoria = hora_si_terminado+minuto_si_terminado+segundo_si_terminado
                hora = 0
                minuto = 0
                segundo = 0
                while True:
                    if sumatoria - 3600 >= 0:
                        hora += 1
                        sumatoria -= 3600
                    else:
                        break
                while True:
                    if sumatoria - 60 >= 0:
                        minuto += 1
                        sumatoria -= 60
                    else:
                        break
                segundo = sumatoria 
                tiempo_durado = str(hora)+" "+"HORAS CON"+" "+str(minuto)+" "+"MINUTOS Y"+" "+str(segundo)+" "+"SEGUNDOS"
                mensaje = messagebox.showinfo(message="¡EXCELENTE! JUEGO TERMINADO CON ÉXITO, HA TARDADO: "+tiempo_durado)

            tiempo_mostrado = texto,hora,":",minuto,":",segundo
            
            if dificultad == "FACIL":
                if len(top_10_facil) < 10:
                    top_10_facil.append(tiempo_mostrado)
                    top_10_facil = sorted(top_10_facil, key=lambda x: x[1:])
                else:
                    lista_prueba = [top_10_facil[9],tiempo_mostrado]
                    lista_prueba = sorted(lista_prueba, key=lambda x: x[1:])
                    top_10_facil[9] = lista_prueba[0]
                    top_10_facil = sorted(top_10_facil, key=lambda x: x[1:])
     
            if dificultad == "MEDIO":
                if len(top_10_medio) < 10:
                    top_10_medio.append(tiempo_mostrado)
                    top_10_medio = sorted(top_10_medio, key=lambda x: x[1:])
                else:
                    lista_prueba = [top_10_medio[9],tiempo_mostrado]
                    lista_prueba = sorted(lista_prueba, key=lambda x: x[1:])
                    top_10_medio[9] = lista_prueba[0]
                    top_10_medio = sorted(top_10_medio, key=lambda x: x[1:])
                    
            if dificultad == "DIFICIL":
                if len(top_10_dificil) < 10:
                    top_10_dificil.append(tiempo_mostrado)
                    top_10_dificil = sorted(top_10_dificil, key=lambda x: x[1:])
                else:
                    lista_prueba = [top_10_dificil[9],tiempo_mostrado]
                    lista_prueba = sorted(lista_prueba, key=lambda x: x[1:])
                    top_10_dificil[9] = lista_prueba[0]
                    top_10_dificil = sorted(top_10_dificil, key=lambda x: x[1:])
                    
        if control_reloj == "No":
            mensaje = messagebox.showinfo(message="¡EXCELENTE! JUEGO TERMINADO CON ÉXITO")
    
        if mensaje == "ok":
            return regreso(ventana_jugar,ventana)
    
    terminado.after(1000,ganador)
    
#===============================================PRINCIPAL===============================================#

archiv_partida =open("futoshiki2021partidas.dat","wb")

faciles = [((0,0,">"),(0,1),(0,2),(0,3,">"),(0,4),
  (1,0,"1"),(1,1),(1,2),(1,3),(1,4),
  (2,0),(2,1),(2,2),(2,3),(2,4),
  (3,0),(3,1),(3,2),(3,3,"4"),(3,4),
  (4,0),(4,1),(4,2),(4,3),(4,4,">")),
           ((0,0),(0,1),(0,2),(0,3),(0,4,"2"),
  (1,0),(1,1,"2"),(1,2),(1,3),(1,4),
  (2,0),(2,1,"<"),(2,2,"<", ">"),(2,3,">"),(2,4),
  (3,0),(3,1),(3,2),(3,3),(3,4),
  (4,0),(4,1),(4,2),(4,3),(4,4,"4")),
           ((0,0,"<"),(0,1),(0,2,"3"),(0,3,"<"),(0,4),
  (1,0),(1,1,"1"),(1,2),(1,3),(1,4),
  (2,0),(2,1),(2,2),(2,3),(2,4),
  (3,0),(3,1,"5"),(3,2),(3,3),(3,4),
  (4,0,">"),(4,1),(4,2),(4,3),(4,4,">"))]

medianas = [((0,0),(0,1),(0,2),(0,3),(0,4),
  (1,0),(1,1),(1,2),(1,3,">"),(1,4),
  (2,0),(2,1),(2,2),(2,3),(2,4),
  (3,0,"<"),(3,1),(3,2),(3,3,">","<"),(3,4,">"),
  (4,0),(4,1),(4,2),(4,3,">"),(4,4,">")),
           ((0,0),(0,1),(0,2),(0,3),(0,4),
  (1,0),(1,1),(1,2,"4"),(1,3,"<"),(1,4),
  (2,0),(2,1),(2,2),(2,3),(2,4),
  (3,0,"<"),(3,1),(3,2),(3,3,"<",">"),(3,4,">"),
  (4,0),(4,1),(4,2),(4,3,">"),(4,4,">")),
           ((0,0),(0,1,"2"),(0,2,">"),(0,3),(0,4),
  (1,0,"<"),(1,1),(1,2),(1,3),(1,4),
  (2,0),(2,1),(2,2),(2,3,">","<"),(2,4),
  (3,0),(3,1),(3,2),(3,3,"4"),(3,4,"1"),
  (4,0,">"),(4,1),(4,2,"<"),(4,3),(4,4))]

dificiles = [((0,0),(0,1,"1"),(0,2),(0,3,">"),(0,4,">"),
  (1,0,"<"),(1,1),(1,2),(1,3),(1,4),
  (2,0),(2,1),(2,2),(2,3,">"),(2,4),
  (3,0,"<"),(3,1),(3,2,">","<"),(3,3),(3,4,"<"),
  (4,0,"<"),(4,1,"<"),(4,2),(4,3,">"),(4,4,">")),
           ((0,0,">"),(0,1),(0,2),(0,3,">"),(0,4),
  (1,0,">"),(1,1),(1,2),(1,3,">"),(1,4,">"),
  (2,0),(2,1,"2"),(2,2),(2,3,">"),(2,4,">"),
  (3,0,"2"),(3,1),(3,2),(3,3),(3,4,"<"),
  (4,0,">"),(4,1,"<"),(4,2),(4,3),(4,4)),
           ((0,0,">"),(0,1),(0,2),(0,3,">"),(0,4),
  (1,0,">"),(1,1),(1,2),(1,3,">"),(1,4,">"),
  (2,0),(2,1,"2"),(2,2),(2,3,">"),(2,4,">"),
  (3,0),(3,1),(3,2),(3,3,"4"),(3,4,"<"),
  (4,0,"5"),(4,1),(4,2),(4,3,">"),(4,4,"<"))]


pickle.dump(faciles,archiv_partida)
pickle.dump("\n",archiv_partida)
pickle.dump(medianas,archiv_partida)
pickle.dump("\n",archiv_partida)
pickle.dump(dificiles,archiv_partida)

archiv_partida.close()

archiv_config =open("futoshiki2021configuración.dat","wb")
archiv_juego =open("futoshiki2021juegoactual.dat","wb")
archiv_top =open("futoshiki2021top10.dat","wb")

ventana = tkinter.Tk()
ventana.title("VENTANA PRINCIPAL")
ventana.geometry("300x200")
ventana.config(bg="#ECFFFF")

futoshiki = tkinter.Label(ventana, text="FUTOSHIKI", font=("Times", "24", "bold italic"))
futoshiki.config(bg="#B9FFDE")
futoshiki.place(x=60,y=50)

borde1 = tkinter.Canvas(ventana, bg="#FFB9FE", height=10, width=10).place(x=50,y=46)
borde2 = tkinter.Canvas(ventana, bg="#99FFA6", height=10, width=10).place(x=35,y=28)
borde3 = tkinter.Canvas(ventana, bg="#99FFA6", height=10, width=10).place(x=70,y=35)
borde4 = tkinter.Canvas(ventana, bg="#FFB9FE", height=10, width=10).place(x=28,y=58)

borde1 = tkinter.Canvas(ventana, bg="#FFB9FE", height=10, width=10).place(x=234,y=41)
borde2 = tkinter.Canvas(ventana, bg="#B9FFDE", height=10, width=10).place(x=210,y=26)
borde3 = tkinter.Canvas(ventana, bg="#99FFA6", height=10, width=10).place(x=260,y=25)
borde4 = tkinter.Canvas(ventana, bg="#B9FFDE", height=10, width=10).place(x=243,y=65)

button1 = tkinter.Button(ventana, text="Jugar", bg="#AAAAAA", fg="white", command=jugar).place(x=60,y=130)
button2 = tkinter.Button(ventana, text="Configuracion", bg="#AAAAAA", fg="white",command=config).place(x=105,y=130)
button3 = tkinter.Button(ventana, text="Ayuda", bg="#AAAAAA", fg="white").place(x=197,y=130)

borde1 = tkinter.Canvas(ventana, bg="#FFB9FE", height=10, width=10).place(x=58,y=115)
borde2 = tkinter.Canvas(ventana, bg="#99FFA6", height=10, width=10).place(x=44,y=128)
borde3 = tkinter.Canvas(ventana, bg="#B9FFDE", height=10, width=10).place(x=230,y=158)
borde4 = tkinter.Canvas(ventana, bg="#B9FFDE", height=10, width=10).place(x=245,y=144)

ventana.mainloop()
