import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import Util.generic as utl

class Vista_inicio:

    def __init__(self, controller=None):
        self.window=tk.Tk()
        self.window.title("MUSICAL TOUR")
        utl.Centre_window(self.window,1300,620)
        self.window.resizable(width=0, height=0)
        self.controller=controller
        
        #Frame de barra superior 
        frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#2f242c")
        frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)

        #Indice de eventos
        op=tk.StringVar(value="ÍNDICE DE EVENTOS")
        self.indice=ttk.Combobox(frame_supbar, state="readonly", textvariable=op, width=50)
        self.indice.configure(background="#e6d884", foreground="#2f242c")
        self.indice.bind("<<ComboboxSelected>>", self.Combobox_select)
        self.indice.pack(side="left", padx=10)
        self.actualizar_eventos()

        #Eventos asistidos
        op2=tk.StringVar(value="EVENTOS ASISTIDOS")
        self.asistidos=ttk.Combobox(frame_supbar, state="readonly", textvariable=op2, width=50)
        self.asistidos.configure(background="#e6d884", foreground="#2f242c")
        self.asistidos.bind("<<ComboboxSelected>>", self.Combobox_select)
        self.asistidos.pack(side="left", padx=10)
        self.actualizar_historial()


        #Botones: mapa, buscador, y cerrar sesion 
        boton_buscador=tk.Button(frame_supbar, text="Abrir Buscador", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=20, padx=1) #command="self.controller.abrir_buscador"
        boton_buscador.pack(side="left",expand=tk.NO,padx=10, fill=tk.NONE)

        boton_mapa=tk.Button(frame_supbar, text="Abrir Mapa", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=20, padx=1) #command="self.controller.abrir_mapa"
        boton_mapa.pack(side="left",expand=tk.NO,padx=10, fill=tk.NONE)

        boton_cerrar_sesion=tk.Button(frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=10) #command="self.controller.cerrar_sesion"
        boton_cerrar_sesion.pack(side="right",expand=tk.NO,padx=10, fill=tk.NONE)

        #ventana principal
        frame_ventana=tk.Frame(self.window, bd=0, relief=tk.SOLID, padx=10, pady=10, bg="#e5e5e5")
        frame_ventana.pack(expand=tk.YES, fill=tk.BOTH)

        logo=utl.redefine_imagen(".\\images\\logo.png", (400,400))
        imafondo=tk.Label(frame_ventana, image=logo, bg="#2f242c")
        imafondo.image=logo
        imafondo.place(x=0,y=0, relwidth=1, relheight=1)

        self.window.mainloop()



    def Combobox_select(self, event):
        objeto=self.buscar_evento(self.indice.current())
        band=1
        self.controller.cambia_evento(objeto, band)

    def actualizar_eventos(self):
        #Lista=self.controller.obtiene_data()
        #self.indice['values']=[f"Nombre: {item.name}\nArtista: {item.artist}\n>Genero: {item.genre}" for item in Lista]
        pass
    
    def actualizar_historial(self):
        #lista=self.controller.obtiene_asistidos()
        #self.asistidos['values']=[f"Nombre: {item.name}\nArtista: {item.artist}\n>Genero: {item.genre}" for item in Lista]
        pass

    def buscar_evento(self, eleccion):
        eventos=self.controller.obtiene_data()
        return eventos[eleccion]
