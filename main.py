from automata import Automata
from tkinter import *
from tkinter import ttk
from automata import Automata
from cinta import Cinta

class Ventana:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('Máquina de Turing')
        self.raiz.configure(bg='black')
        self.raiz.geometry("800x600")
        
        
        
        self.menu = Menu(self.raiz)
        self.raiz.config(menu=self.menu)
        
        file_menu = Menu(self.menu)
        self.menu.add_cascade(label="Idiomas", menu=file_menu)
        file_menu.add_command(label="Español", command=lambda: self.cambiar_idioma("es"))
        file_menu.add_command(label="Inglés", command=lambda: self.cambiar_idioma("en"))
        file_menu.add_command(label="Francés", command=lambda: self.cambiar_idioma("fr"))
        
        self.slider = Scale(self.raiz,from_=0, to=100, orient=HORIZONTAL)
        self.slider.pack()
        
        self.cinta = Cinta(self.raiz)
        
        
        
        self.automata = Automata(self.raiz)
        self.entry = Entry(self.raiz,  width=80)
        self.entry.pack()
        self.button = Button(self.raiz, text="Validar", command=lambda: self.validar())
        self.button.pack()
        self.raiz.configure(bg = "#e0e0e0")
        
        
        self.raiz.mainloop()

    def validar(self):
        self.automata.actualizar(self.raiz)
        self.automata.lienzo.delete(self.automata.mensaje)
        self.validador.validar(self.automata,self.entry.get())
if __name__ == "__main__":
    try:
        Ventana()
    except:
        print(" ")