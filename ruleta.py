from tkinter import *
import random
global hacer_apuesta,minimo,din_dis,color,apostad
minimo=100
color=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    
def comienzo():
    global hacer_apuesta,minimo,din_dis,color
    
#    hacer_apuesta.withdraw()
    
    tdin=m.get()
    din_dis=float(tdin)
    hacer_apuesta=Toplevel()
    hacer_apuesta.title("Apuesta")
    hacer_apuesta.withdraw()

    BCR=Button(hacer_apuesta,text="rojos",command=rojos)
    BCR.grid(row=6,column=0)

    BCN=Button(hacer_apuesta,text="negros",command=negros)
    BCN.grid(row=6,column=1)

    BPAR=Button(hacer_apuesta,text="Pares",command=negros)
    BPAR.grid(row=6,column=2)

    BIPR=Button(hacer_apuesta,text="Impares",command=rojos)
    BIPR.grid(row=6,column=3)

    BPAS=Button(hacer_apuesta,text="Pasa",command=pasa)
    BPAS.grid(row=6,column=4)

    BFAL=Button(hacer_apuesta,text="Falta",command=falta)
    BFAL.grid(row=6,column=5)

    NUM=Entry(hacer_apuesta,textvariable=au)
    NUM.grid(row=6,column=6)

    BUM=Button(hacer_apuesta,text="verificar numero",command=numero)
    BUM.grid(row=6,column=7)
        
    a=1
    color[0]="verde"

    while(a<=18):
        color[2*a]="negro"
        color[(2*a)-1]="rojo"
        a=a+1
    color[37]="verde"

    if(din_dis<minimo):
        error.set("necesitas mas dinero")
    else:
        error.set("El jugador cuenta con: "+ str(din_dis))
        Brev.config(state=NORMAL)
        Ball.config(state=NORMAL)
        BI.config(state=DISABLED)
        dinero.config(state=DISABLED)
        bienvenido.set("Usted esta jugando")

def verificar():
    global din_dis,minimo,apostad

    dr=da.get()

    a=float(dr)

    if(a<=0 and a>din_dis):
        if(a<minimo):
            apostado.set("no puedes apostar esa cantidad \n Prueba de nuevo")
    if(a>=minimo and a<=din_dis):
        porapostar.set("Usted est apostando: " + str(a))
        apostad=a

        Ball.config(state=DISABLED)
        Brev.config(state=DISABLED)
        Dpa.config(state=DISABLED)

        hacer_apuesta.deiconify()
    else:
        apostado.set("no puedes apostar esa cantidad \n Prueba de nuevo")
        
def todo():
    global din_dis,minimo

    porapostar.set("Usted est apostando: " + str(din_dis))

    Ball.config(state=DISABLED)
    Brev.config(state=DISABLED)
    Dpa.config(state=DISABLED)

    hacer_apuesta.deiconify()

def rojos():

    G=1
    I=1
    N=0
    comparacion(G,I,N)
    
def negros():

    G=1
    I=2
    N=0
    comparacion(G,I,N)

def pasa():

    G=1
    I=4
    N=0       
    comparacion(G,I,N)
    
def fin():

    pass



def falta():

    G=1
    I=3
    N=0
    comparacion(G,I,N)
    
def numero():

    G=36
    I=0
    N=float(au)
    comparacion(G,I,N)

def comparacion(G,V,N):
    global din_dis,apostad

    hacer_apuesta.withdraw()
    
    num=random.randint(0,37)
    
    if(num<37):
        apostado.set("La ruleta cayo en: " + str(num) + "color: " + str(color[num]))
    else:
        apostado.set("La ruleta cayo en: 00" + "color: " + str(color[num]))

    r=1
    W=0
    
    if(V>0 and V<=4):
        if(V==1):

            if(color[num]=="rojo"):
                ganado.set("a ganado: " + str(G*apostad))
                dis_dis=din_dis+(G*apostad)
                W=1
             
            
        if(V==2):
            
            if(color[num]=="negro"):
                ganado.set("a ganado: " + str(G*apostad))
                dis_dis=din_dis+(G*apostad)
                W=1
                
        if(V==3):

            if(num<=18 and num>0):
                ganado.set("a ganado: " + str(G*apostad))
                dis_dis=din_dis+(G*apostad)
                W=1

        if(V==4):

            if(num<=36 and num>18):
                ganado.set("a ganado: " + str(G*apostad))
                dis_dis=din_dis+(G*apostad)
                W=1

    if(V==0):

        if(num==N):
            ganado.set("a ganado: " + str(G*apostad))
            dis_dis=din_dis+(G*apostad)
            W=1

    if(W==0):
        dis_dis=din_dis-(apostad)
        ganado.set("a perdido: " + str(apostad))
        d_act.set("El jugador cuenta con: "+ str(din_dis))
    if(W==1):    
        d_act.set("El jugador cuenta con: "+ str(din_dis))

    Ball.config(state=NORMAL)
    Brev.config(state=NORMAL)
    Dpa.config(state=NORMAL)
    BRet.config(state=NORMAL)

ventana=Tk()

m=StringVar()
da=StringVar()
au=StringVar()
error=StringVar()
bienvenido=StringVar()
apostado=StringVar()
porapostar=StringVar()
ganado=StringVar()
d_act=StringVar()


bienvenido.set("Bienvenido \n La apuesta minima es de: " + str(minimo) + "\n Cuanto dinero tiene?")
dinero=Entry(ventana,textvariable=m)
dinero.grid(row=3,column=2)
BI=Button(ventana,text="ingresar cantidad",command=comienzo)
BI.grid(row=4,column=2)


merror=Label(ventana,textvariable=error)
merror.grid(row=5,column=2)
Lb=Label(ventana,textvariable=bienvenido)
Lb.grid(row=1,column=2)
La=Label(ventana,textvariable=apostado)
La.grid(row=6,column=2)
Lpa=Label(ventana,textvariable=porapostar)
Lpa.grid(row=7,column=2)
Dpa=Entry(ventana,textvariable=da)
Dpa.grid(row=8,column=2)
Brev=Button(ventana,text="Verificar apuesta",command=verificar,state=DISABLED)
Brev.grid(row=9,column=2)
Ball=Button(ventana,text="Apostar todo",command=todo,state=DISABLED)
Ball.grid(row=9,column=3)
Lganado=Label(ventana,textvariable=ganado)
Lganado.grid(row=11,column=2)
BRet=Button(ventana,text="salir",command=fin,state=DISABLED)
BRet.grid(row=10,column=2)
Lact=Label(ventana,textvariable=d_act)
Lact.grid(row=12,column=2)
    
ventana.mainloop()
