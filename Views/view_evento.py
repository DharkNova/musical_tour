import tkinter as tk
from tkinter import ttk, messagebox
import Util.generic as utl
from Controllers.Controller_evento import control_evento
class vista_evento(tk.Frame):

    def __init__(self, objeto):
        self.window=tk.Tk()
        self.window.title("MUSICAL TOUR")
        utl.Centre_window(self.window,1300,620)
        self.window.config(bg="#e5e5e5")
        self.window.resizable(width=0, height=0)
        self.controller=control_evento()
        
        
        #Frame de barra superior 
        self.frame_supbar=tk.Frame(self.window, bd=0, height=40, relief=tk.SOLID, padx=10, pady=10, bg="#2f242c")
        self.frame_supbar.pack(side="top", expand=tk.NO, fill=tk.X)

        boton_volver=tk.Button(self.frame_supbar, text="Volver", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_volver.pack(side="left",expand=tk.NO,padx=5, fill=tk.NONE)

        self.frame_evento=tk.Frame(self.window,bd=0,width=600, relief=tk.SOLID,bg="#e5e5e5")
        self.frame_evento.pack(side="left",expand=tk.YES, fill=tk.BOTH)

        self.titulo=tk.Label(self.frame_evento, text=objeto.name, font=("Roboto, 25"), fg="#2f242c", bg="#e5e5e5")
        self.titulo.pack(side="top", anchor="nw",padx=240, pady=20)

        self.descripcion=tk.Label(self.frame_evento,text="Descripción: "+objeto.description, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5", wraplength=550, justify=tk.LEFT)
        self.descripcion.pack(side="top", anchor="nw",padx=10, pady=5)

        self.artista=tk.Label(self.frame_evento,text="Artista: "+objeto.artist, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5",wraplength=630)
        self.artista.pack(side="top", anchor="nw",padx=10, pady=5)

        self.genero=tk.Label(self.frame_evento,text="Genero: "+objeto.genre, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5")
        self.genero.pack(side="top", anchor="nw",padx=10, pady=5)

        self.hora_inicio=tk.Label(self.frame_evento,text="Hora de inicio: "+objeto.time_start, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5")
        self.hora_inicio.pack(side="top", anchor="nw",padx=10, pady=5)

        self.hora_fin=tk.Label(self.frame_evento,text="Hora de finalización: "+objeto.time_end, font=("Opensans, 18"), fg="#2f242c", bg="#e5e5e5")
        self.hora_fin.pack(side="top", anchor="nw",padx=10, pady=5)

        # imagen=utl.redefine_imagen(".\\images\\"+ objeto.picture, (250,300))
        # imaevento=tk.Label(self.frame_evento,image=imagen, bg="#e5e5e5")
        # imaevento.image=imagen
        # imaevento.place(x=630,y=10, relwidth=0.3, relheight=0.5)

        self.frame_panel_reseñas=tk.Frame(self.window, bd=0,width=400,relief=tk.SOLID, bg="#2f242c")
        self.frame_panel_reseñas.pack(side="right",fill=tk.BOTH)

        frame_reseñas=tk.Frame(self.frame_panel_reseñas, bd=0, width=300, height=350, relief=tk.SOLID, bg="#2f242c")
        frame_reseñas.pack(side="top")
        scroll_bar=tk.Scrollbar(frame_reseñas)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas=tk.Canvas(frame_reseñas, yscrollcommand=scroll_bar.set,height=300,bg="#2f242c")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_bar.config(command=canvas.yview)

        frame_comentador=tk.Frame(self.frame_panel_reseñas, bd=0,relief=tk.SOLID, bg="#2f242c")
        frame_comentador.pack(expand=tk.YES, fill=tk.BOTH)

        frame_botones_inf=tk.Frame(frame_comentador,bd=0, relief=tk.SOLID, bg="#2f242c")
        frame_botones_inf.pack(expand=tk.YES, fill=tk.BOTH)

        frame_botones_sup=tk.Frame(frame_comentador,bd=0, relief=tk.SOLID, bg="#2f242c")
        frame_botones_sup.pack(expand=tk.YES, fill=tk.BOTH)

        entra_comentario=tk.Text(frame_comentador, width=50, height=3, font=("Opensans, 12"), fg="#2f242c")
        entra_comentario.pack(side="bottom", anchor="sw", padx=10,pady=5)
        boton_comentar=tk.Button(frame_comentador, text="Comentar", font=("Roboto, 13"), fg="#2f242c", bg="#e6d884", width=5, padx=10)
        boton_comentar.pack(side="bottom",anchor="se",expand=tk.NO,padx=10, fill=tk.NONE)

        
        valora_label=tk.Label(frame_botones_inf, text="Valoracion:",font=("Roboto, 12"),width=8,height=1, fg="#e5e5e5", bg="#2f242c")
        valora_label.pack(side="left", anchor="center",padx=10, pady=10)
        
        var= tk.StringVar() 
        valoracion = ttk.Combobox(frame_botones_inf,values=[chr(9733),(chr(9733),chr(9733)),(chr(9733),chr(9733),chr(9733)),(chr(9733),chr(9733),chr(9733),chr(9733)),(chr(9733),chr(9733),chr(9733),chr(9733),chr(9733))],state="readonly",textvariable=var, width= 43, height=10)
        valoracion.configure(background="#e6d884", foreground="#2f242c")
        valoracion.set("Valoración de evento")
        #valoracion.bind("<<ComboboxSelected>>", self.combobox_on_select)
        valoracion.pack(side="left", anchor="center", padx=10, pady=10)



        animo_label=tk.Label(frame_botones_sup, text="Animo:",font=("Roboto, 12"),width=4,height=1, fg="#e5e5e5", bg="#2f242c",padx=5)
        animo_label.pack(side="left",anchor="center",padx=10, pady=10)

        vara= tk.StringVar() 
        animo = ttk.Combobox(frame_botones_sup,values=["Bueno","Neutral","Malo"],state="readonly",textvariable=vara, width= 43, height=10)
        animo.configure(background="#e6d884", foreground="#2f242c")
        animo.set("Animo del comentario")
        #valoracion.bind("<<ComboboxSelected>>", self.combobox_on_select)
        animo.pack(side="right", anchor="center", padx=10, pady=20)

        self.window.mainloop()




    
        