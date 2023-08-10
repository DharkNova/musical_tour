import tkinter as tk
from tkinter import ttk, messagebox
import Util.generic as utl
from Controllers.Controller_evento import control_evento
class vista_evento():

    def __init__(self, objeto, band):
        self.window=tk.Tk()
        self.window.title("MUSICAL TOUR")
        utl.Centre_window(self.window,1300,620)
        self.window.config(bg="#e5e5e5")
        self.window.resizable(width=0, height=0)
        self.controller=control_evento()
        self.evento=objeto
        self.band=band
        
        
        #Frame de barra superior 
        self.frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#2f242c")
        self.frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)

        boton_volver=tk.Button(self.frame_supbar, text="Volver", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10, command=self.volver_atras)
        boton_volver.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        boton_inicio=tk.Button(self.frame_supbar, text="Inicio", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10, command=self.controller.Volver_inicio)
        boton_inicio.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        boton_Asistido=tk.Button(self.frame_supbar, text="Marcar como evento asistido", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=25, padx=10)
        boton_Asistido.pack(side="left",expand=tk.NO,padx=20, fill=tk.NONE)

        boton_cerrar_sesion=tk.Button(self.frame_supbar, text="Cerrar sesion", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=10, padx=10)
        boton_cerrar_sesion.pack(side="right",expand=tk.NO,padx=10, fill=tk.NONE)

        boton_visualizar=tk.Button(self.frame_supbar, text="Visualizar en Mapa", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=20, padx=10)
        boton_visualizar.pack(side="right",anchor="center",expand=tk.NO,padx=50, fill=tk.NONE)

        boton_Agregar_R=tk.Button(self.frame_supbar, text="Agregar a Ruta", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=20, padx=10, command=self.agregar_ruta)
        boton_Agregar_R.pack(side="right",anchor="center",expand=tk.NO,padx=50, fill=tk.NONE)



        self.frame_evento=tk.Frame(self.window,bd=10,width=600, relief=tk.SOLID,bg="#e5e5e5")
        self.frame_evento.pack(side="left",expand=tk.YES, fill=tk.BOTH)

        self.titulo=tk.Label(self.frame_evento, text=self.evento.name, font=("Roboto, 25"), fg="#2f242c", bg="#e5e5e5")
        self.titulo.pack(side="top", anchor="nw",padx=240, pady=20)

        self.descripcion=tk.Label(self.frame_evento,text="Descripción: "+self.evento.description, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5", wraplength=550, justify=tk.LEFT)
        self.descripcion.pack(side="top", anchor="nw",padx=10, pady=5)

        self.artista=tk.Label(self.frame_evento,text="Artista: "+self.evento.artist, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5",wraplength=630)
        self.artista.pack(side="top", anchor="nw",padx=10, pady=5)

        self.genero=tk.Label(self.frame_evento,text="Genero: "+self.evento.genre, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5")
        self.genero.pack(side="top", anchor="nw",padx=10, pady=5)

        self.hora_inicio=tk.Label(self.frame_evento,text="Hora de inicio: "+self.evento.time_start, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5")
        self.hora_inicio.pack(side="top", anchor="nw",padx=10, pady=5)

        self.hora_fin=tk.Label(self.frame_evento,text="Hora de finalización: "+self.evento.time_end, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5")
        self.hora_fin.pack(side="top", anchor="nw",padx=10, pady=5)

        imagen=utl.redefine_imagen(".\\images\\"+ self.evento.picture, (200,300))
        imaevento=tk.Label(self.frame_evento,image=imagen, bg="#e5e5e5")
        imaevento.image=imagen
        imaevento.place(x=550,y=20, relwidth=0.3, relheight=0.6)

        self.frame_panel_reseñas=tk.Frame(self.window, bd=10,width=400,relief=tk.SOLID, bg="red")
        self.frame_panel_reseñas.pack(side="right",expand=tk.NO,fill=tk.BOTH)

        frame_botones_inf=tk.Frame(self.frame_panel_reseñas, width=400, height=240, bd=0, relief=tk.SOLID, bg="#2f242c")
        frame_botones_inf.pack(side="bottom", anchor="s", expand=tk.NO, fill=tk.NONE)

        frame_barra_coment=tk.Frame(frame_botones_inf, width=400, height=120, bd=0, relief=tk.SOLID, bg="#2f242c")
        frame_barra_coment.pack(side="bottom", anchor="s", expand=tk.NO, fill=tk.NONE)

        self.entra_comentario=tk.Text(frame_barra_coment, width=50, height=3, font=("Opensans, 12"), fg="#2f242c")
        self.entra_comentario.pack(side="bottom", anchor="sw", padx=10,pady=20)
        
        boton_comentar=tk.Button(frame_barra_coment, text="Comentar", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10, command=self.Agrega_comentario)
        boton_comentar.pack(side="bottom",anchor="se",expand=tk.NO,padx=10, pady=10, fill=tk.NONE)

        frame_combo_valoani=tk.Frame(frame_botones_inf, width=400, height=120, bd=0, relief=tk.SOLID, bg="#2f242c")
        frame_combo_valoani.pack(side="top", anchor="n", expand=tk.YES, fill=tk.BOTH)

        valora_label=tk.Label(frame_combo_valoani, text="Valoracion:",font=("Roboto, 12"),width=8,height=1, fg="#e5e5e5", bg="#2f242c")
        valora_label.pack(side="left", anchor="center",padx=5, pady=20)
        
        self.var= tk.StringVar() 
        valoracion = ttk.Combobox(frame_combo_valoani,values=[chr(9733),(chr(9733),chr(9733)),(chr(9733),chr(9733),chr(9733)),(chr(9733),chr(9733),chr(9733),chr(9733)),(chr(9733),chr(9733),chr(9733),chr(9733),chr(9733))],state="readonly",textvariable=self.var, width= 20, height=10)
        valoracion.configure(background="#e6d884", foreground="#2f242c")
        valoracion.set("Valoración de evento")
        valoracion.pack(side="left", anchor="center", padx=5, pady=2)

        animo_label=tk.Label(frame_combo_valoani, text="Animo:",font=("Roboto, 12"),width=4,height=1, fg="#e5e5e5", bg="#2f242c",padx=5)
        animo_label.pack(side="left",anchor="center",padx=5, pady=20)

        self.vara= tk.StringVar() 
        animo = ttk.Combobox(frame_combo_valoani,values=["Bueno","Neutral","Malo"],state="readonly",textvariable=self.vara, width= 20, height=10)
        animo.configure(background="#e6d884", foreground="#2f242c")
        animo.set("Animo del comentario")
        animo.pack(side="right", anchor="center", padx=5, pady=20)

        frame_list_comentarios=tk.Frame(self.frame_panel_reseñas, bd=0, relief=tk.SOLID, bg="yellow")
        frame_list_comentarios.pack(expand=tk.YES, fill=tk.BOTH)

        scroll_list=tk.Scrollbar(frame_list_comentarios)
        scroll_list.pack(side="right", fill=tk.Y)

        self.list_comentario=tk.Listbox(frame_list_comentarios, yscrollcommand=scroll_list.set, state=tk.DISABLED, activestyle=tk.NONE, bd=0, relief=tk.SOLID, fg="#2f242c", bg="#e5e5e5")
        self.list_comentario.pack(expand=tk.YES, fill=tk.BOTH)
        scroll_list.config(command=self.list_comentario.yview)

        self.window.mainloop()
    
    def Agrega_comentario(self):
        self.list_comentario.configure(state=tk.NORMAL, exportselection=False)
        id_evento=self.evento.id
        comentario=self.entra_comentario.get("1.0", tk.END)
        valoracion=self.var.get()
        animo=self.vara.get()
        #id_user=self.app.user.id
        #self.controller.agrega_comentario(id_evento, id_user, valoracion, animo, comentario)
        user=f"Usuario: 1"
        valida=f"Valoración: {valoracion}"
        ani=f"Ánimo: {animo}"
        comenta=f"comentario: {comentario}"

        allcoment=[user, valida, ani, comenta]

        for label in allcoment:
            self.list_comentario.insert(tk.END, label)
         
        self.list_comentario.configure(state=tk.DISABLED, exportselection=False)
        self.entra_comentario.delete("1.0", tk.END)

        self.var.set("")
        self.vara.set("")

    def agregar_ruta(self):
        id_ubi=self.evento.id_position
        self.controller.Agregar_ruta(id_ubi)

    def volver_atras(self):
        if self.band==1:
            self.controller.Volver_inicio()
        else:
            self.controller.Volver_busca()












    
        