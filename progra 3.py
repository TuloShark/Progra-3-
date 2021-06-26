import tkinter
import random
from tkinter import messagebox

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

jugador = 0

#=======================================================================================================#

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
    
    ventana.state(newstate="withdraw")
    ventana_jugar = tkinter.Tk()
    ventana_jugar.title("VENTANA PRINCIPAL")
    ventana_jugar.geometry("578x700")
    ventana_jugar.config(bg="#FFECEC")

    iniciar_activado = False
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
    botton_pri_5 = tkinter.Button(ventana_jugar, text="TOP 10", height=2, width=13, bg="#99FFA6")
    botton_pri_5.place(x=460, y=480)

    botton_regreso = tkinter.Button(ventana_jugar,text="X",command=lambda: regreso(ventana_jugar,ventana))
    botton_regreso.place(x=558,y=65)

    if borrar == False:                  
        suerte = random.randint(1,3)
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
    
    texto = str(jugador.get())
    if texto == "":
        return messagebox.showinfo(message="DEBE DIGITAR UN NOMBRE PRIMERO")
    if len(texto) > 20:
        return messagebox.showinfo(message="EL NOMBRE DEBE DE ESTAR ENRTE 1 Y 20 CARACTERES")

    iniciar_activado = True
    
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

    if iniciar_activado == True:
        segundo = segundo_numero["text"]   
        minuto = minuto_numero["text"]
        hora = hora_numero["text"]
        if segundo == 59:
            minuto_numero.config(text=minuto+1)
            segundo = -1       
            if minuto == 59:
                hora_numero.config(text=hora+1)
                minuto = -1
                minuto_numero.config(text=minuto+1)
        segundo_numero.config(text=segundo+1)
        actualizar = tkinter.Label()
        actualizar.after(1000,tiempo)
    else:
        minuto_numero.config(text=0)
        segundo_numero.config(text=0)
        hora_numero.config(text=0)  

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
    
    x.destroy()
    y.deiconify()
    
#==============================================CONFIGURACION============================================#

def config():

    global ventana
    global dificultad
    global control_reloj
    global panel
      
    ventana.state(newstate="withdraw")
    ventana_config = tkinter.Tk()
    ventana_config.title("VENTANA PRINCIPAL")
    ventana_config.geometry("578x620")

    botton_regreso = tkinter.Button(ventana_config,text="X",command=lambda: regreso(ventana_config,ventana))
    botton_regreso.place(x=558,y=65)

    nivel = tkinter.Label(ventana_config, text="Nivel:").place(x=50,y=50)
    reloj = tkinter.Label(ventana_config, text="Reloj:").place(x=50,y=155)
    digitos = tkinter.Label(ventana_config, text="Panel de Digitos:").place(x=50,y=260)

    facil = tkinter.Checkbutton(ventana_config, text="Facil",command=lambda: actualizar_difi_1(facil,medio,dificil))
    facil.place(x=50,y=75)
    medio = tkinter.Checkbutton(ventana_config, text="Medio",command=lambda: actualizar_difi_2(medio,facil,dificil))
    medio.place(x=50,y=100)
    dificil = tkinter.Checkbutton(ventana_config, text="Dificil",command=lambda: actualizar_difi_3(dificil,facil,medio))
    dificil.place(x=50,y=125)

    reloj_si = tkinter.Checkbutton(ventana_config, text="Si",command=lambda: actualizar_reloj_1(reloj_si,reloj_no,timer))
    reloj_si.place(x=50,y=180)
    reloj_no = tkinter.Checkbutton(ventana_config, text="No",command=lambda: actualizar_reloj_2(reloj_no,reloj_si,timer))
    reloj_no.place(x=50,y=205)
    timer = tkinter.Checkbutton(ventana_config, text="Timer",command=lambda: actualizar_reloj_1(timer,reloj_no,reloj_si))
    timer.place(x=50,y=230)

    panel_de = tkinter.Checkbutton(ventana_config, text="Derecha",command=lambda: actualizar_panel_1(panel_de,panel_iz))
    panel_de.place(x=50,y=285)
    panel_iz = tkinter.Checkbutton(ventana_config, text="Izquierda",command=lambda: actualizar_panel_2(panel_iz,panel_de))
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

def actualizar_reloj_1(x,y,z):

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
        segundo = segundo_numero["text"]   
        minuto = minuto_numero["text"]
        hora = hora_numero["text"]
        numero_manejado = 0
        mensaje = messagebox.showinfo(message="¡EXCELENTE! JUEGO TERMINADO CON ÉXITO, HA TARDADO: "+str(hora)+" "+"HORAS CON"+" "+str(minuto)+" "+"MINUTOS Y"+" "+str(segundo)+" "+"SEGUNDOS")
        
        if mensaje == "ok":
            return regreso(ventana_jugar,ventana)
    
    terminado.after(1000,ganador)
    
#===============================================PRINCIPAL===============================================#
    
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
