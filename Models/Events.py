from Data.Json_Operations import Helper
from datetime import datetime
from PIL import Image
import base64

class Event:
    Cont=0
    def __init__(self, name, artist, genre,id_position, time_start, time_end, description, picture):        
        Event.Cont+=1

        self.id=Event.Cont
        self.name=name
        self.artist=artist
        self.genre=genre
        self.id_position=id_position
        self.time_start=Event.charge_time(time_start)
        self.time_end=Event.charge_time(time_end)
        self.description=description
        self.picture=picture
    
    @staticmethod
    def create_event(id_ubi):
        nam=input("Ingrese el nombre del evento: ")
        art=input("Ingrese el nombre del artista/s: ")
        gen=input("Ingrese el genero del artista/s: ")
        id=id_ubi
        ti=input("Ingrese la hora de inicio del evento en formato (HH:MM): ")
        te=input("Ingrese la hora de finalizacón del evento en formato (HH:MM): ")
        des=input("Ingrese una descripción del evento: ")
        rut=input("Ingrese el nombre del archivo imagen seguido de su formato (imagen.jpeg): ")
        pic="Data\\"+rut

        return Event(nam,art,gen,id,ti,te,des,pic)
    
    def charge_time(hora):
        formato="%H:%M"
        fecha=datetime.now().date()
        hora=datetime.strptime(hora,formato).time()
        hora_fecha=datetime.combine(fecha,hora)
        hora_iso=datetime.isoformat(hora_fecha)
        return hora_iso
    
    @staticmethod
    def charge_event(item):
        ruta="Data\\Events.json"
        Helper.save_in_list(ruta, item.__dict__)

    @staticmethod
    def remove_Event(item):
        ruta="Data\\Events.json"
        Helper.delete_item(ruta, item)

#    def modify_event(self):
 #       ruta="Data\\Events.json"
  #      Helper.modify_item(ruta, self.id)


    def __str__(self):
        return f"id: {self.id}\nNombre: {self.name}\nArtista: {self.artist}\nGenero: {self.genre}\nposición: {self.id_position}\nTiempo inicio: {self.time_start}\nTiempo final: {self.time_end}\ndescripción: {self.description}\nimagen: {self.picture}"
        
