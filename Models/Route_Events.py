
from Data.Json_Operations import Helper

class Route_event:
    Cont=0
    ruta="Data\\Routes.json"
    def __init__(self, name, destinations):
        Route_event.Cont+=1
        self.id=Route_event.Cont
        self.name=name
        self.destinations=[]
        
    def charge_Route(item):
        Helper.save_in_list(Route_event.ruta, item.__dict__)

    def remove_Route(item):
        Helper.delete_item(Route_event.ruta, item)

    def __str__(self):
        return f"id: {self.id}\nNombre: {self.name}\nDestins"
        
