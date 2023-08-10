import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import Util.generic as utl
from Controllers.Controller_login import control_logueo
import main
from register import registro

class vista_login:

    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Inicio de sesión")
        self.window.config(bg="red")
        self.window.resizable(width=0,height=0)
        self.controller=control_logueo()
        utl.Centre_window(self.window,700,500)

        frame_logo=tk.Frame(self.window, bd=0,width=300, relief=tk.SOLID, bg="#2f242c")
        frame_logo.pack(side="left",anchor="w", expand=tk.YES, fill=tk.Y)

        logo=utl.redefine_imagen(".\\images\\logo.png", (300,300))
        imafondo=tk.Label(frame_logo, image=logo, bg="#2f242c")
        imafondo.image=logo
        imafondo.place(x=0,y=0, relwidth=1, relheight=1)

        frame_titulo=tk.Frame(self.window, bd=0, width=400, height=90, relief=tk.SOLID, bg="#a1a892")
        frame_titulo.pack(side="top", anchor="n", expand=tk.NO, fill=tk.NONE)

        Titulo=tk.Label(frame_titulo, text="Inicio de sesion",width=400, height=2,font=("times", 30), fg="#2f242c", bg="#a1a892")
        Titulo.pack(anchor="center", expand=tk.NO, fill=tk.NONE)

        frame_login=tk.Frame(self.window, height=400, width=400, bd=0, relief=tk.SOLID, bg="#e5e5e5")
        frame_login.pack(expand=tk.YES, fill=tk.BOTH)

        Correo=tk.Label(frame_login, text="Correo",font=("times", 12), fg="#2f242c", bg="#e5e5e5", anchor="w")
        Correo.pack(anchor="center", fill=tk.X, padx=20, pady=10)
        self.correo=ttk.Entry(frame_login, font=("times", 12))
        self.correo.pack(fill=tk.X, padx=20, pady=10)

        contraseña=tk.Label(frame_login, text="Contraseña",font=("times", 12), fg="#2f242c", bg="#e5e5e5", anchor="w")
        contraseña.pack(anchor="center", fill=tk.X, padx=20, pady=10)
        self.contraseña=ttk.Entry(frame_login, font=("times", 12))
        self.contraseña.pack(fill=tk.X, padx=20, pady=10)
        self.contraseña.config(show="*")

        boton_inicio_sesion=tk.Button(frame_login,text="Iniciar Sesion", font=("times", 15, BOLD), fg="#e5e5e5", bg="#2f242c")
        boton_inicio_sesion.pack(fill=tk.X, padx=20, pady=40)
        boton_inicio_sesion.bind("<Return>", lambda event: "funcion inicio")

        boton_registro=tk.Button(frame_login,text="Registrar Usuario", font=("times", 15), fg="#e5e5e5", bg="#2f242c")
        boton_registro.pack(fill=tk.X, padx=20)

        self.window.mainloop()

    def iniciar_sesion(self):
        correo=self.correo.get()
        contra=self.contraseña.get()
        user=self.controller.verifica_inicio(correo, contra)
        if user is not None:
            self.window.destroy()
            main()

    def registrar_usuario(self):
        registro()







