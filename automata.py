
from transiciones import *
from arco import *
from tkinter import *
from estados import *


class Automata:
    def __init__(self, raiz):
        self.raiz = raiz
        self.estados = []
        self.transiciones = []
        self.lienzo=Canvas(raiz, width=800, height=400, bg="#e0e0e0")
        self.lienzo.pack()
        self.inicio = self.lienzo.create_line([120,300,150,300],arrow=LAST,width=3, fill="black")
        self.transiciones.append(Transicion(self.lienzo,[130,240],"a/a/R"))
        self.transiciones.append(Transicion(self.lienzo,[130,220],"b/a/R"))
        self.mensaje = self.lienzo.create_text([400, 100], fill="green", text="")
        #Estado q1
        self.q1 = Estado(self.lienzo, "q1", [150,250,250,350])
        self.arcop = Arco(self.lienzo, [160, 190, 240, 340], [240,270,240,271])
        self.q1q2 = self.lienzo.create_line([250,300,350,300],arrow=LAST,width=3, fill="black")
        self.estados.append(self.q1)
        
        self.transiciones.append(Transicion(self.lienzo,[290,280],"B/B/L"))

        #Estado q2
        self.q2 = Estado(self.lienzo, "q2", [350,250,450,350])
        self.texto2= self.lienzo.create_text(400,298,fill="black",font="Algerian 16 bold",text="q2")
        self.arcoq = Arco(self.lienzo, [360, 190, 440, 340], [440,270,440,271])
        self.q2q3 = self.lienzo.create_line([450,300,550,300],arrow=LAST,width=3, fill="black")
        self.transiciones.append(Transicion(self.lienzo,[500,320],"B/B/R"))
        self.transiciones.append(Transicion(self.lienzo,[460,220],"a/a/L"))
 
        self.estados.append(self.q2)
        
        #Estado q3
        self.q3 = Estado(self.lienzo, "q3", [550,250,650,350])
        self.texto3= self.lienzo.create_text(600,298,fill="black",font="Algerian 16 bold",text="q3", activefill='magenta')
        self.estados.append(self.q3)
        
    
    def activarEstado(self, valor):
        for estado in self.estados:
            if estado.valor == valor:
                estado.activar()
    
    def desactivarEstado(self, valor):
        for estado in self.estados:
            if estado.valor == valor:
                estado.desactivar()
    
    def activarTransicion(self, valor):
        for transicion in self.transiciones:
            if transicion.valor == valor:
                transicion.activar()
    def desactivarTransicion(self, valor):
        for transicion in self.transiciones:
            if transicion.valor==valor:
                transicion.desactivar()
                
                
    def actualizar(self, raiz):
        self.lienzo.delete("all")
        self.estados = []
        self.transiciones = []
        self.inicio = self.lienzo.create_line([120,300,150,300],arrow=LAST,width=3, fill="black")
        self.transiciones.append(Transicion(self.lienzo,[130,240],"a/a/R"))
        self.transiciones.append(Transicion(self.lienzo,[130,220],"b/a/R"))
        self.mensaje = self.lienzo.create_text([400, 100], fill="green", text="")
        #Estado q1
        self.q1 = Estado(self.lienzo, "q1", [150,250,250,350])
        self.arcop = Arco(self.lienzo, [160, 190, 240, 340], [240,270,240,271])
        self.pq = self.lienzo.create_line([250,300,350,300],arrow=LAST,width=3, fill="black")
        self.estados.append(self.q1)
        
        self.transiciones.append(Transicion(self.lienzo,[290,280],"B/B/L"))

        #Estado q2
        self.q2 = Estado(self.lienzo, "q2", [350,250,450,350])
        self.texto2= self.lienzo.create_text(400,298,fill="black",font="Algerian 16 bold",text="q")
        self.arcoq = Arco(self.lienzo, [360, 190, 440, 340], [440,270,440,271])
        self.qr = self.lienzo.create_line([450,300,550,300],arrow=LAST,width=3, fill="black")
        self.transiciones.append(Transicion(self.lienzo,[460,220],"a/a/L"))
 
        self.estados.append(self.q2)
        
        self.q3 = Estado(self.lienzo, "q3", [550,250,650,350])
        self.texto3= self.lienzo.create_text(600,298,fill="black",font="Algerian 16 bold",text="q3", activefill='magenta')
        self.estados.append(self.q3)