
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
# from Models.Position import position
# from Models.Events import Event

# ubi=position.create_position()


from Models.Events import Event
from Models.Position import position

def Crea_ubi_event():
    ubi1=position.create_position()
    id=ubi1.id
    position.charge_position(ubi1)
    even1=Event.create_event(id)
    Event.charge_event(even1)

