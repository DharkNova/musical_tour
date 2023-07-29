
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






# from Models.Events import Event
# from Models.Position import position

# def Crea_ubi_event():
#     Posi=position.create_position()
#     id=Posi.id
#     position.charge_position(Posi)
#     Posi=None
#     event=Event.create_event(id)
#     Event.charge_event(event)
#     event=None

# def Elimina_ubi_event():
#     id=1
#     position.remove_position(id)
#     Event.remove_Event(id)


# Crea_ubi_event()
# Crea_ubi_event()
# Elimina_ubi_event()




# from Models.Users import User
# print("Inicio sesion:\n\n")
# user1=User.sign_in()
# print("Registro usuario:\n\n")
# User.sign_up()
# print("Inicio sesion:\n\n")
# user1=User.sign_in()
# print("Elimino usuario:\n\n")
# User.remove_user(user1)
# print("Inicio sesion:\n\n")
# User.sign_in()



#---INDICE DE EVENTOS---
