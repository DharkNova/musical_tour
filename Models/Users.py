
from Data.Json_Operations import Helper
import re

class User:
    Cont=0
    def __init__(self, name, surname):
        User.Cont+=1
        self.id=User.Cont
        self.name=name
        self.surname=surname
    
    @staticmethod
    def validation_email(email):

        patron=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron, email):
            return True
        else:
            return False


    
    def charge_user(item):
        ruta="Data\\Users.json"
        Helper.save_in_list(ruta, item.__dict__)

    def remove_user(item):
        ruta="Data\\Users.json"
        Helper.delete_item(ruta, item)

#    def modify_event(self):
 #       ruta="Data\\Events.json"
  #      Helper.modify_item(ruta, self.id)


    def __str__(self):
        return f"id: {self.id}\nNombre: {self.name}\nArtista: {self.artist}\nGenero: {self.genre}\nposición: {self.id_position}\nTiempo inicio: {self.time_start}\nTiempo final: {self.time_end}\ndescripción: {self.description}\nimagen: {self.picture}"
        


