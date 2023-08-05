#IMPLEMENTACION DE MAPA


# import tkinter
# import tkintermapview
# import geocoder

# root_tk = tkinter.Tk()
# root_tk.geometry(f"{800}x{600}")
# root_tk.title("map_view_example.py")

# map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
# map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# coordenadas=geocoder.ip("me")
# latitud=coordenadas.lat
# longitud=coordenadas.lng
# map_widget.set_position(latitud,longitud)  # Paris, France
# map_widget.set_zoom(12)
# root_tk.mainloop()



#MODULO PARA GENERAR EVENTOS SIMULTANEAMENTE CON UBICACION


# from Models.Events import Event
# from Models.Position import position

# def Crea_ubi_event():
#     Posi=position.create_position()
#     id=Posi.id
#     position.charge_position(Posi)
#     #Posi=None
#     event=Event.create_event(id)
#     Event.charge_event(event)
#     #event=None
# def Elimina_ubi_event():
#     id=1
#     position.remove_position(id)
#     Event.remove_Event(id)


# Crea_ubi_event()

# Elimina_ubi_event()


#REGISTRO E INICIO DE SESION DE USUARIO

#from Models.Users import User

# print("Inicio sesion...\n\n")
# user1=User.sign_in()
# print(user1)
# print("Elimino usuario:\n\n")
# User.remove_user(user1.id)

# print("Inicio sesion:\n\n")
# User.sign_in()



#---INDICE DE EVENTOS---
#from Models.Events import Event
# even1=Event("pool party", "david guetta", "electronic House", "1", "21:00", "00:00", "La mejor fiesta en piscina del mundo, con el mejor artista", "consoladj1.jpg")
# even2=Event("festival de rock", "Artistas varios", "rock", "2", "11:00", "12:00", "El festival de rock que tanto estabas buscando", "festival_rock.jpg")
#even3=Event("Concierto estelar de los rolling stones", "rolling stones", "rock", "3", "01:00", "05:00","Uno de los conciertos más importantes del mundo del rock", "rolling.jpeg")
# Event.charge_event(even1)
# Event.charge_event(even2)
# Event.charge_event(even3)
# Lista=Event.indice_eventos()
# op=1
# Event.Muestra_eventos(op , Lista)


#BUSQUEDA Y FILTRADO

# from Models.search_and_filter import Search

# Lista=Search.Busqueda("rock")
# if Lista is not None:
#    for i in Lista:
#       print(i)
# else:
#    print("Vacío")

# import tkinter as tk

# class MiApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Tour Musical")
#         self.geometry("600x600")

#         if __name__=="__main__":
#             app=MiApp()
#             app.mainloop()

# class Aplicacion(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title("Aplicación de Videojuegos")
#         self.geometry("330x300")
#         self.resizable(False, False)
#         self.inicializar()
#         self.cambiar_frame(self.vista_inicio)

#     def inicializar(self):
        
#         #juegos = Juego.cargar_de_json("data/juegos.json")

#         #controlador_inicio = ControladorInicio(self)
#         #controlador_juegos = ControladorJuegos(self, juegos)
#         #controlador_info = ControladorInfo(self)

#         self.vista_inicio = VistaInicio(self)
#         #self.vista_juegos = VistaJuegos(self, controlador_juegos)
#         #self.vista_info = VistaInfo(self, controlador_info)

#         self.ajustar_frame(self.vista_inicio)
#         #self.ajustar_frame(self.vista_juegos)
#         #self.ajustar_frame(self.vista_info)

#     def ajustar_frame(self, frame):
#         frame.grid(row=0, column=0, sticky="nsew")

#     def cambiar_frame(self, frame_destino):
#         frame_destino.tkraise()

# if __name__=="__main__":
#     app=Aplicacion()
#     app.mainloop()


import tkinter as tk

from tkinter.font import BOLD
import Util.generic as utl
from Models.Events import Event
from Controllers.Controller_inicio import Control_inicio
from Views.view_evento import vista_evento
from Views.view_inicio import vista_inicio
from Views.view_Mapa_ruta import window_mapa
even2=Event("festival de rock", "Artistas varios", "rock", "2", "11:00", "12:00", "El festival de rock que tanto estabas buscando, preparate porque es el ultimo gran evento que organizamos por los artistas que tanto desean ploriferar en el mundo de la musica, esperamos que lo disfrutes al maximo y  a rockandrollear!!      ", "festival_rock.jpg")

vista_evento(even2)

# class Aplication(tk.Tk):

#     def __init__(self):
#         tk.Tk.__init__(self)

#         self.inicializa()
#         self.cambiar_ventana(self.vista_inicio)
        
        
#     def inicializa(self):
#         Eventos=Event.indice_eventos()

#         control_inicio=Control_inicio(self, Eventos)        
#         self.vista_inicio=vista_inicio(self, control_inicio)
#         self.vista_evento=vista_evento(self)

#         self.vista_inicio.pack()
#         self.vista_evento.pack()

#         self.cambiar_ventana(self.vista_inicio)
#         self.cambiar_ventana(self.vista_evento)

#         #self.vista_Mapa=window_mapa()

#     def ajustar_ventana(self, frame):
#        frame.pack(fill="both", expand=True)

#     def cambiar_ventana(self, frame_destino):
#         self.vista_inicio.pack_forget()
#         self.vista_evento.pack_forget()
#         frame_destino.pack(side="left")

# if __name__=="__main__":
#     app=Aplication()
#     app.mainloop()
    

# from tkinter import messagebox, ttk
# import tkinter as tk
# class Application(ttk.Frame):
    
#     def __init__(self, main_window):
#         super().__init__(main_window)
#         main_window.title("Combobox")
#         self.combo = ttk.Combobox(
#             self,
#             values=["Python", "C", "C++", "Java"]
#         )
#         self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
#         self.combo.place(x=50, y=50)
#         main_window.config(width=300, height=200)
#         self.place(width=300, height=200)
#     def selection_changed(self, event):
#         selection = self.combo.get()
#         messagebox.showinfo(
#             title="Nuevo elemento seleccionado",
#             message=selection
#         )
# main_window = tk.Tk()
# app = Application(main_window)
# app.mainloop()
