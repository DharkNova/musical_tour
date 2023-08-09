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
        self.window.resizable(width=0, height=0)
        self.controller=Control_inicio()
        
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


        #Botones: Buscar, barra de busqueda, y cerrar sesion 
        boton_buscador=tk.Button(frame_supbar, text="Abrir Buscador", font=("Roboto, 13"),command=self.simula_funcion, fg="#2f242c", bg="#e6d884", width=20, padx=1)
        boton_buscador.pack(side="left",expand=tk.NO,padx=10, fill=tk.NONE)
        # boton_buscar.bind("<<return>>", (lambda event: self.simula_funcion))
        boton_mapa=tk.Button(frame_supbar, text="Abrir Mapa", font=("Roboto, 13"),command=self.simula_funcion, fg="#2f242c", bg="#e6d884", width=20, padx=1)
        boton_mapa.pack(side="left",expand=tk.NO,padx=10, fill=tk.NONE)
        # var=tk.StringVar()
        # self.barbusqueda=tk.Entry(frame_supbar, textvariable=var, width=50)
        # self.barbusqueda.pack(side="left", padx=2)

        # chekop=tk.IntVar()
        # boton_ubicacion=tk.Checkbutton(frame_supbar, text="Ubicación", variable=chekop)
        # boton_ubicacion.pack(side="left", expand=tk.NO, fill=tk.NONE)

        # op3=tk.StringVar(value="HORARIO")
        # self.horario=ttk.Combobox(frame_supbar,values=["MAÑANA", "TARDE", "NOCHE"] ,state="readonly", textvariable=op3, width=9)
        # self.horario.configure(background="#e6d884", foreground="#2f242c")
        # #self.asistidos.bind("<<ComboboxSelected>>", self.Combobox_select)
        # self.horario.pack(side="left", padx=2)

        boton_cerrar_sesion=tk.Button(frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=10)
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
        self.window.destroy()
        self.controller.cambia_evento(objeto)

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

        
    def simula_funcion(self):
        messagebox.showinfo(message="Esto es una funcion ejecutandose")