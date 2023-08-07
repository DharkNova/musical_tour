import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import Util.generic as utl
from Controllers.Controller_inicio import Control_inicio

class Vista_inicio:

    def __init__(self):
        self.window=tk.Tk()
        self.window.title("MUSICAL TOUR")
        utl.Centre_window(self.window,1300,620)
        self.window.config(bg="#e5e5e5")
        self.window.resizable(width=0, height=0)
        self.controller=Control_inicio()
        
        #Frame de barra superior 
        frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#a1a892")
        frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)

        #Indice de eventos
        op=tk.StringVar(value="ÍNDICE DE EVENTOS")
        self.indice=ttk.Combobox(frame_supbar, state="readonly", textvariable=op, width=50)
        self.indice.configure(background="#e6d884", foreground="#2f242c")
        self.indice.bind("<<ComboboxSelected>>", self.Combobox_select)
        self.indice.pack(side="left", padx=10)
        self.actualizar_eventos()

        #Botones: Buscar, barra de busqueda, y cerrar sesion 
        var=tk.StringVar()
        barbusqueda=tk.Entry(frame_supbar, textvariable=var, width=52)
        barbusqueda.pack(side="left", padx=5)

        boton_cerrar_sesion=tk.Button(frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=5)
        boton_cerrar_sesion.pack(side="right",expand=tk.NO,padx=5, fill=tk.NONE)

        #ventana principal
        frame_ventana=tk.Frame(self.window, bd=0, relief=tk.SOLID, padx=10, pady=10, bg="#e5e5e5")
        frame_ventana.pack(expand=tk.YES, fill=tk.BOTH)


        logo=utl.redefine_imagen(".\\images\\logo.png", (400,400))
        imafondo=tk.Label(frame_ventana, image=logo, bg="#e5e5e5")
        imafondo.image=logo
        imafondo.place(x=0,y=0, relwidth=1, relheight=1)

        self.window.mainloop()

    def Combobox_select(self, event):
        objeto=self.buscar_evento(self.indice.current())
        self.window.destroy()
        self.controller.cambia_evento(objeto)

    def actualizar_eventos(self):
        Lista=self.controller.obtiene_data()
        self.indice['values']=[f"Nombre: {item.name}\nArtista: {item.artist}\n>Genero: {item.genre}" for item in Lista]
    
    def buscar_evento(self, eleccion):
        eventos=self.controller.obtiene_data()
        return eventos[eleccion]

        
