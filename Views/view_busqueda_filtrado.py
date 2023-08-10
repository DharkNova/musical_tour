import tkinter as tk
from tkinter import ttk
import Util.generic as utl

class busca_filtra:
    def __init__(self, controller=None):
        self.window=tk.Tk()
        self.window.title("MUSICAL TOUR")
        utl.Centre_window(self.window,1300,620)
        self.window.resizable(width=0, height=0)
        self.controller=controller

            
        #Frame de barra superior 
        frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#2f242c")
        frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)

        #Botones: Buscar, barra de busqueda, y cerrar sesion 
        boton_volver=tk.Button(frame_supbar, text="Volver", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=1) #command=self.controller.volver
        boton_volver.pack(side="left",expand=tk.NO,padx=10, fill=tk.NONE)

        self.var=tk.StringVar(value="Ingrese el evento a buscar...")
        self.barbusqueda=tk.Entry(frame_supbar, textvariable=self.var, width=100)
        self.barbusqueda.pack(side="left", padx=2)

        self.op3=tk.StringVar()
        self.horario=ttk.Combobox(frame_supbar,values=["Elige una opción","MAÑANA (04:00-12:00)", "TARDE(12:00-20:00)", "NOCHE(20:00-04:00)"] ,state="readonly", textvariable=self.op3, width=50)
        self.horario.set("Elige una opción")
        self.horario.configure(background="#e6d884", foreground="#2f242c")
        self.horario.pack(side="left", padx=2)

        boton_cerrar_sesion=tk.Button(frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=10)
        boton_cerrar_sesion.pack(side="right",expand=tk.NO,padx=10, fill=tk.NONE)

        boton_buscar=tk.Button(frame_supbar, text="Buscar", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=20, padx=1, command=self.busca_resultados)
        boton_buscar.pack(side="right",expand=tk.NO,padx=10, fill=tk.NONE)

        #ventana principal
        self.frame_ventana=tk.Frame(self.window, bd=0, relief=tk.SOLID, padx=10, pady=10, bg="#e5e5e5")
        self.frame_ventana.pack(expand=tk.YES, fill=tk.BOTH)


        logo=utl.redefine_imagen(".\\images\\logo.png", (400,400))
        imafondo=tk.Label(self.frame_ventana, image=logo, bg="#2f242c")
        imafondo.image=logo
        imafondo.place(x=0,y=0, relwidth=1, relheight=1)

        self.frame_ventana_busqueda=tk.Frame(self.window, bd=0, relief=tk.SOLID,width=1300,height=567, bg="red")
        self.frame_ventana_busqueda.pack(side="left", anchor="center", expand=tk.YES, fill=tk.BOTH)
        self.frame_ventana_busqueda.pack_forget()

        frame_logo_izq=tk.Frame(self.frame_ventana_busqueda, bd=0, relief=tk.SOLID,width=433, height=567, bg="#2f242c")
        frame_logo_izq.pack(side="left", anchor="w", expand=tk.YES, fill=tk.BOTH)

        logo=utl.redefine_imagen(".\\images\\logo.png", (350,350))
        imafondo=tk.Label(frame_logo_izq, image=logo, bg="#2f242c")
        imafondo.image=logo
        imafondo.place(x=0,y=0, relwidth=1, relheight=1)

        frame_logo_der=tk.Frame(self.frame_ventana_busqueda, bd=0, relief=tk.SOLID,width=433, height=567, bg="#2f242c")
        frame_logo_der.pack(side="right", anchor="e", expand=tk.YES, fill=tk.BOTH)

        logo=utl.redefine_imagen(".\\images\\logo.png", (350,350))
        imafondo=tk.Label(frame_logo_der, image=logo, bg="#2f242c")
        imafondo.image=logo
        imafondo.place(x=0,y=0, relwidth=1, relheight=1)

        frame_centro=tk.Frame(self.frame_ventana_busqueda, bd=0, relief=tk.SOLID,width=434, height=567, bg="brown")
        frame_centro.pack(side="top", anchor="center", expand=tk.NO, fill=tk.NONE)

        frame_cant_resultados=tk.Frame(frame_centro, bd=0, relief=tk.SOLID,width=434, height=80, bg="#e5e5e5")
        frame_cant_resultados.pack(side="top", anchor="n", expand=tk.YES, fill=tk.BOTH)

        self.cant_resultados=tk.Label(frame_cant_resultados, font=("Roboto, 25"), fg="#2f242c", bg="#e5e5e5")
        self.cant_resultados.pack(side="top", anchor="center",padx=240, pady=20)

        scroll_list=tk.Scrollbar(frame_centro)
        scroll_list.pack(side="right", fill=tk.Y)

        self.list_resultados=tk.Listbox(frame_centro,height=354, yscrollcommand=scroll_list.set, activestyle=tk.NONE, bd=0, relief=tk.SOLID, fg="#2f242c", bg="#e5e5e5")
        self.list_resultados.pack(expand=tk.YES, fill=tk.BOTH)
        self.list_resultados.bind("<Double-Button-1>", self.seleccionar_evento)
        scroll_list.config(command=self.list_resultados.yview)


        
        self.lista_final=None
        self.window.mainloop()


    def toma_horario(self):
        cadena=self.op3.get()
        if self.horario.current()==1:
            hora_ini=cadena[8:13]
            hora_fin=cadena[14:19]
            return hora_ini, hora_fin
        elif self.horario.current()==0:
            return None, None
        else:
            hora_ini=cadena[6:11]
            hora_fin=cadena[12:17]
            return hora_ini, hora_fin
            

    def busca_resultados(self):
        if self.list_resultados.curselection():
            self.list_resultados.delete(0, tk.END)

        self.frame_ventana.pack_forget()
        self.frame_ventana_busqueda.pack(side="left", anchor="center", expand=tk.YES, fill=tk.BOTH)

        hora_ini, hora_fin=self.toma_horario()
        busqueda=self.var.get()

        resultados=self.controller.buscar(busqueda)
        
        if hora_ini is not None and hora_fin is not None:
            lista_filtrada=self.controller.filtrar(hora_ini, hora_fin, resultados)
            cant=lista_filtrada,len()
            self.cant_resultados['text']=f"Se encontraron: {cant} resultados"
            self.cargar_resultados()
        else:
            cant=resultados.len()
            self.cant_resultados['text']=f"Se encontraron: {cant} resultados"
            self.cargar_resultados()


    def cargar_resultados(self, lista):
        for i in lista:
            elemento=f"Nombre: {i.name} \nArtista: {i.artist} \nGenero: {i.genre}"
            self.list_resultados.insert(tk.END, elemento)
        self.lista_final=lista

    def seleccionar_evento(self):
        indice=self.list_resultados.curselection()
        evento=self.lista_final[indice]
        band=2
        self.controller.abre_evento(evento, band)





