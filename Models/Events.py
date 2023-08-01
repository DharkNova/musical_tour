from Data.Json_Operations import Helper
from datetime import datetime

class Event:
    Cont=0
    ruta="Data\\Events.json"
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
        pic="images\\"+rut

        return Event(nam,art,gen,id,ti,te,des,pic)
    
    def charge_time(hora):
        formato="%H:%M"
        fecha=datetime.now().date()
        hora=datetime.strptime(hora,formato).time()
        hora_fecha=datetime.combine(fecha,hora)
        hora_iso=datetime.isoformat(hora_fecha)
        return hora_iso
    
    def invierte_iso(hora_ISO):
        hora=datetime.strptime(hora_ISO,"%Y-%m-%dT%H:%M:%S")
        hora_final=datetime.strftime(hora,"%H:%M")
        return hora_final

    @staticmethod
    def charge_event(item):
        Helper.save_in_list(Event.ruta, item.__dict__)

    @staticmethod
    def remove_Event(item):
        Helper.delete_item(Event.ruta, item)

    @staticmethod
    def indice_eventos():
        eventos=Event.instancia_Lista_Even(Event.ruta)
        return eventos
    
    @staticmethod
    def Muestra_eventos(op, Lista):
        for objeto in Lista:
             if op==True:
                muestra=Event.Muestra_evento_indice(objeto)
                print(muestra)
             else:
                muestra=Event.__str__(objeto)
                print(muestra)
    def instancia_Lista_Even(ruta_json):
        List=Helper.load_file(ruta_json)
        Lista=[]
        for data in List:
            even=Event(data['name'], data['artist'], data['genre'], data['id_position'], Event.invierte_iso(data['time_start']), Event.invierte_iso(data['time_end']), data['description'], data['picture'])
            Lista.append(even)
        return Lista
    
    def __str__(self):
        return f"id: {self.id}\nNombre: {self.name}\nArtista: {self.artist}\nGenero: {self.genre}\nposición: {self.id_position}\nTiempo inicio: {self.time_start}\nTiempo final: {self.time_end}\ndescripción: {self.description}\nimagen: {self.picture}"
        
    def Muestra_evento_indice(item):
        return f"Nombre: {item.name}\nArtista: {item.artist}\nGenero: {item.genre}\nLugar: {item.id_position}\n\n"
    