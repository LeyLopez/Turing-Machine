from tkinter import *

class Cinta:
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(self.master, width=600, height=100)
        self.canvas.pack()

        # Define una cinta con 10 celdas
        self.cinta = ['B'] * 30
        self.cinta_labels = []
        self.pos = 1

        # Dibuja la cinta
        self.dibujar_cinta()

    def mover(self, direccion):
        if direccion == "R":
            self.pos += 1
        elif direccion == "L":
            self.pos -= 1
        self.actualizar_cinta()

    def cambiar_simbolo(self, simbolo):
        self.cinta[self.pos] = simbolo
        self.actualizar_cinta()

    def dibujar_cinta(self):
        for i, simbolo in enumerate(self.cinta):
            x = 50 + i * 100
            y = 50
            rect = self.canvas.create_rectangle(x, y, x + 50, y + 50)
            text = self.canvas.create_text(x + 25, y + 25, text=simbolo)
            self.cinta_labels.append((rect, text))

    def actualizar_cinta(self):
        for i, (rect, text) in enumerate(self.cinta_labels):
            self.canvas.itemconfig(text, text=self.cinta[i])