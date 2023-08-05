import tkinter as tk
from tkinter import ttk

class window_inicio(tk.Frame):

    def __init__(self, window=None, controller=None):
        
        super().__init__(window)
        self.window=window
        self.controller=controller

        #Frame de barra superior 
        frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#a1a892")
        frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)


        #Indice de eventos
        opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
        opcion_seleccionada = tk.StringVar()
        opcion_seleccionada.set("ÍNDICE DE EVENTOS")
        def combobox_on_select(event):
            if opcion_seleccionada.get()=="ÍNDICE DE EVENTOS":
                opcion_seleccionada.set("")
        combobox = ttk.Combobox(frame_supbar, values=opciones, textvariable=opcion_seleccionada, width= 40, heigh=10)
        combobox.bind("<<ComboboxSelected>>", combobox_on_select)
        combobox.configure(background="#e6d884", foreground="#2f242c")
        combobox.select_clear()
        combobox.pack(side="left")

        #Botones de barra superior
        boton_historial=tk.Button(frame_supbar, text="Historial", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_historial.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        boton_mapa=tk.Button(frame_supbar, text="Mapa", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_mapa.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        boton_buscar=tk.Button(frame_supbar, text="Buscar", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_buscar.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)
        
        boton_cerrar_sesion=tk.Button(frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=5)
        boton_cerrar_sesion.pack(side="right",expand=tk.NO,padx=5, fill=tk.NONE)

        #Frame de panel izquierdo de eventos 
        frame_panel_izq=tk.Frame(self.window, bd=0, width=600, relief=tk.SOLID, padx=10, pady=10, bg="#2F242C")
        frame_panel_izq.pack(side="left", expand=tk.NO, fill=tk.BOTH)