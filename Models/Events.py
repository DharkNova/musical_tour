from Data.Json_Operations import Helper
from datetime import datetime
from Position import position

class Event:
    Cont=0
    def __init__(self, name, artist, genre, time_start, time_end, description, picture):
        Event.Cont+=1
        self.id=Event.Cont
        self.name=name
        self.artist=artist
        self.genre=genre
        position.create_position()
        self.id_position=position.get_position()
        self.time_start=Event.charge_time(time_start)
        self.time_end=Event.charge_time(time_end)
        self.description=description
        self.picture=picture
    
    def charge_time(hora):
        formato="%H:%M"
        fecha=datetime.now().date()
        hora=datetime.strptime(hora,formato).time()
        hora_fecha=datetime.combine(fecha,hora)
        hora_iso=datetime.isoformat(hora_fecha)
        return hora_iso
    
    def charge_event(item):
        ruta="Data\\Events.json"
        Helper.save_in_list(ruta, item.__dict__)

    def remove_Event(item):
        ruta="Data\\Events.json"
        Helper.delete_item(ruta, item)

#    def modify_event(self):
 #       ruta="Data\\Events.json"
  #      Helper.modify_item(ruta, self.id)


    def __str__(self):
        return f"id: {self.id}\nNombre: {self.name}\nArtista: {self.artist}\nGenero: {self.genre}\nposición: {self.id_position}\nTiempo inicio: {self.time_start}\nTiempo final: {self.time_end}\ndescripción: {self.description}\nimagen: {self.picture}"
        
