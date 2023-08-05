import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import sys
sys.path.append("C:\\Users\\vasqu\\Desktop\\musical tour\\musical_tour\\Util\\generic.py")
import Util.generic as utl
from Controllers.Controller_inicio import Control_inicio

class vista_inicio:

    def __init__(self):
        self.window=tk.Tk()
        self.controller=Control_inicio()
        self.window.title("MUSICAL TOUR")
        utl.Centre_window(self.window,1300,620)
        self.window.config(bg="#e5e5e5")
        self.window.resizable(width=0, height=0)
        
        #Frame de barra superior 
        frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#a1a892")
        frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)


        #Indice de eventos
        opcion= tk.StringVar() 
        self.indice = ttk.Combobox(frame_supbar,state="readonly",textvariable=opcion, width= 50, height=10)
        self.indice.configure(background="#e6d884", foreground="#2f242c")
        self.indice.set("ÍNDICE DE EVENTOS")
        self.indice.bind("<<ComboboxSelected>>", self.combobox_on_select)
        self.indice.pack(side="left", padx=10)
        self.actualizar_eventos()
       

        # self.historial = ttk.Combobox(frame_supbar, values=opciones,textvariable=opcion, width= 40, height=10)
        # self.historial.configure(background="#e6d884", foreground="#2f242c")
        # self.historial.bind("<<ComboboxSelected>>", combobox_on_select)
        # self.historial.pack(side="left", padx=10)
        # self.actualizar_eventos()

        #Botones de barra superior
        boton_mapa=tk.Button(frame_supbar, text="Mapa", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_mapa.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        boton_buscar=tk.Button(frame_supbar, text="Buscar", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_buscar.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        var=tk.StringVar()
        barbusqueda=tk.Entry(frame_supbar, textvariable=var, width=52)
        barbusqueda.pack(side="left", padx=5)

        
        boton_cerrar_sesion=tk.Button(frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=5)
        boton_cerrar_sesion.pack(side="right",expand=tk.NO,padx=5, fill=tk.NONE)

        chekvar=tk.IntVar()
        checkboton=tk.Checkbutton(frame_supbar, text="selecciona", variable=chekvar)
        checkboton.pack(side="right")

        # filtro_var = tk.IntVar()
        # filtroUbi= tk.Radiobutton(frame_supbar, text="Ubicación", variable=filtro_var, value=1)
        # filtroUbi.pack(side="right", padx=5)
        # filtroHora = tk.Radiobutton(frame_supbar, text="Horario", variable=filtro_var, value=2)
        # filtroHora.pack(side="right", padx=5)
        

        #Frame ventana completa
        frame_ventana=tk.Frame(self.window, bd=0, relief=tk.SOLID, padx=10, pady=10, bg="#e5e5e5")
        frame_ventana.pack(expand=tk.YES, fill=tk.BOTH)

        logo=utl.redefine_imagen(".\\images\\logo.PNG", (400,400))

        imafondo=tk.Label(frame_ventana, image=logo, bg="#e5e5e5")
        imafondo.image=logo
        imafondo.place(x=0,y=0, relwidth=1, relheight=1)
        self.window.mainloop()

    def combobox_on_select(self, event):
        eleccion=self.indice.current()
        objeto=self.buscar_evento(eleccion)
        self.controller.detalle_evento(objeto)


    def actualizar_eventos(self):
        Lista=self.controller.obtiene_data()
        self.indice['values']=[f"Nombre: {item.name}\nArtista: {item.artist}\n>Genero: {item.genre}" for item in Lista]
    
    def buscar_evento(self, eleccion):
        eventos=self.controller.obtiene_data()
        return eventos[eleccion]
    

        







       
        



        