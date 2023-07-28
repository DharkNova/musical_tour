from geopy.geocoders import Nominatim


class position: 
    cont=0
    def __init__(self, name, address, coordenadas):
        position.cont+=1
        self.id=position.cont
        self.name=name
        self.address=address
        self.coordenadas=coordenadas

    def create_position(self):
        nam=input("Ingrese el nombre del lugar: ")
        add=input("Ingrese la dirección del lugar: ")
        geolocator=Nominatim(user_agent="Musical_Tour")
        location=geolocator.geocode(add)
        if location is not None:
            lat=location.latitude
            lon=location.longitude
        else:
            print("Ingrese las coordenadas: ")
            lat=float(input("Ingrese latitud: "))
            lat=float(input("Ingrese longitud: "))
        ubi=position(nam, add, (lat,lon))
        

    def get_position(self):
        return self.id