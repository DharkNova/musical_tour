from geopy.geocoders import Nominatim
from Data.Json_Operations import Helper

class position: 
    cont=0
    def __init__(self, name, address, coordenadas):
        position.cont+=1
        self.id=position.cont
        self.name=name
        self.address=address
        self.coordenadas=coordenadas

    def create_position():
        nam=input("Ingrese el nombre del lugar: ")
        add=input("Ingrese la dirección del lugar (Num, calle, ciudad, provincia, Codigo postal): ")
        geolocator=Nominatim(user_agent="Musical_Tour")
        location=geolocator.geocode(add)
        if location is not None:
            lat=location.latitude
            lon=location.longitude
        else:
            print("No se reconoce la dirección, Por favor ingrese las coordenadas...")
            lat=float(input("Ingrese latitud: "))
            lon=float(input("Ingrese longitud: "))

        return position(nam, add, (lat,lon))
    
    @staticmethod
    def charge_position(item):
        ruta="Data\\Positions.json"
        Helper.save_in_list(ruta, item.__dict__)
    
    def __str__(self):
        return f"id: {self.id}\nNombre: {self.name}\nDirección: {self.address}\nCoordenadas: {self.coordenadas}"
