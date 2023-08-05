import tkinter as tk
from tkinter import ttk

class window_mapa(tk.Frame):

    def __init__(self, window=None, controller=None):
        
        super().__init__(window)
        self.window=window
        self.controller=controller

        #Frame de barra superior 
        frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#a1a892")
        frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)

        #Botones de barra superior
        boton_volver=tk.Button(frame_supbar, text="Volver", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_volver.pack(side="left",expand=tk.NO,padx=10, fill=tk.NONE)

        boton_buscar=tk.Button(frame_supbar, text="Buscar", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_buscar.pack(side="left", expand=tk.NO,padx=10, fill=tk.NONE)

        boton_cerrar_sesion=tk.Button(frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=5)
        boton_cerrar_sesion.pack(side="right",expand=tk.NO,padx=10, fill=tk.NONE)

        boton_Truta=tk.Button(frame_supbar, text="Terminar ruta", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=10)
        boton_Truta.pack(side="right",expand=tk.NO,padx=60, fill=tk.NONE)

        boton_Iruta=tk.Button(frame_supbar, text="Iniciar ruta", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=10)
        boton_Iruta.pack(side="right",expand=tk.NO,padx=50, fill=tk.NONE)

        #Frame de panel izquierdo de eventos 
        frame_panel_izq=tk.Frame(self.window, bd=0, width=600, relief=tk.SOLID, padx=10, pady=10, bg="#2F242C")
        frame_panel_izq.pack(side="left", expand=tk.NO, fill=tk.BOTH)