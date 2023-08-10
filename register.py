import tkinter as tk
from tkinter import ttk
from Controllers.Controller_registro import control_registro
import Util.generic as utl
class registro:

    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Inicio de sesión")
        self.window.config(bg="red")
        self.window.resizable(width=0,height=0)
        self.controller=control_registro()
        utl.Centre_window(self.window,700,500)

        frame_logo=tk.Frame(self.window, bd=0,width=300, relief=tk.SOLID, bg="#e6d884")
        frame_logo.pack(side="left",anchor="w", expand=tk.YES, fill=tk.Y)

        logo=utl.redefine_imagen(".\\images\\logo.png", (300,300))
        imafondo=tk.Label(frame_logo, image=logo, bg="#e6d884")
        imafondo.image=logo
        imafondo.place(x=0,y=0, relwidth=1, relheight=1)

        frame_titulo=tk.Frame(self.window, bd=0, width=400, height=90, relief=tk.SOLID, bg="#e5e5e5")
        frame_titulo.pack(side="top", anchor="n", expand=tk.NO, fill=tk.NONE)

        Titulo=tk.Label(frame_titulo, text="Registro de Usuario",width=400, height=2,font=("times", 30), fg="#2f242c", bg="#a1a892")
        Titulo.pack(anchor="center", expand=tk.NO, fill=tk.NONE)

        frame_login=tk.Frame(self.window, height=400, width=400, bd=0, relief=tk.SOLID, bg="#a1a892")
        frame_login.pack(expand=tk.YES, fill=tk.BOTH)

        Correo=tk.Label(frame_login, text="Correo",font=("times", 12), fg="#2f242c", bg="#a1a892", anchor="w")
        Correo.pack(anchor="center", fill=tk.X, padx=20, pady=10)
        self.correo=ttk.Entry(frame_login, font=("times", 12))
        self.correo.pack(fill=tk.X, padx=20, pady=5)

        contraseña=tk.Label(frame_login, text="Contraseña",font=("times", 12), fg="#2f242c", bg="#a1a892", anchor="w")
        contraseña.pack(anchor="center", fill=tk.X, padx=20, pady=10)
        self.contraseña=ttk.Entry(frame_login, font=("times", 12))
        self.contraseña.pack(fill=tk.X, padx=20, pady=10)
        self.contraseña.config(show="*")

        Nombre=tk.Label(frame_login, text="Nombre",font=("times", 12), fg="#2f242c", bg="#a1a892", anchor="w")
        Nombre.pack(anchor="center", fill=tk.X, padx=20, pady=10)
        self.Nombre=ttk.Entry(frame_login, font=("times", 12))
        self.Nombre.pack(fill=tk.X, padx=20, pady=5)

        Apellido=tk.Label(frame_login, text="Apellido",font=("times", 12), fg="#2f242c", bg="#a1a892", anchor="w")
        Apellido.pack(anchor="center", fill=tk.X, padx=20, pady=10)
        self.Apellido=ttk.Entry(frame_login, font=("times", 12))
        self.Apellido.pack(fill=tk.X, padx=20, pady=5)

        boton_registro=tk.Button(frame_login,text="Registrarse", font=("times", 15), fg="#2f242c", bg="#e6d884")
        boton_registro.pack(fill=tk.X, padx=20)

        self.window.mainloop()

    def registrar(self):
        correo=self.correo.get()
        contraseña=self.contraseña.get()
        nombre=self.Nombre.get()
        apellido=self.Apellido.get()
        registro_exitoso=control_registro.registrar(self, correo, contraseña, nombre, apellido)
        if registro_exitoso==True:
            self.window.destroy()
            