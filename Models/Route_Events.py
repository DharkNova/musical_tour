from Data.Json_Operations import Helper

class Route_event:
    Cont=0
    def __init__(self, name, destinations):
        Route_event.Cont+=1
        self.id=Route_event.Cont
        self.name=name
        self.destinations=[]
        
    def charge_Route(item):
        ruta="Data\\Route.json"
        Helper.save_in_list(ruta, item.__dict__)

    def remove_Route(item):
        ruta="Data\\Route.json"
        Helper.delete_item(ruta, item)

    def __str__(self):
        return f"id: {self.id}\nNombre: {self.name}\nDestins"
        
