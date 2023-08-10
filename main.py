#IMPLEMENTACION DE MAPA





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
from Models.Events import Event
# even1=Event("pool party", "david guetta", "electronic House", "1", "21:00", "00:00", "La mejor fiesta en piscina del mundo, con el mejor artista", "consoladj1.jpg")
even2=Event("festival de rock", "Artistas varios", "rock", "2", "11:00", "12:00", "El festival de rock que tanto estabas buscando", "imagen.jpeg")
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


from Views.view_inicio import Vista_inicio
from Views.view_evento import vista_evento
from Views.view_Mapa_ruta import vista_mapa
from Views.view_busqueda_filtrado import busca_filtra
# # Vista_inicio()
# # vista_evento(even2)
# #vista_mapa( )
busca_filtra()


