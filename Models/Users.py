
from Data.Json_Operations import Helper
import re

class User:
    Cont=0
    ruta="Data\\Users.json"
    def __init__(self, name, surname, email, password):
        User.Cont+=1
        self.id=User.Cont
        self.name=name
        self.surname=surname
        self.email=email
        self.password=password
        self.eventos_asistidos=[]

    @staticmethod
    def sign_up():
        band=False
        while band!=True:
            email=input("Ingrese su correo electronico: ")
            if User.validation_email(email)==True:
                band=True
            else:
                print("Correo invalido.")
        password=input("Ingrese su contraseña: ")
        band=False
        while band!=True:
            contra=input("Ingrese nuevamente su contraseña: ")
            if contra==password:
                band=True
            else:
                print("Las contraseñas no coinciden: ")
        nam=input("Ingrese su nombre: ")
        sur=input("Ingrese su apellido: ")
        user=User(nam,sur,email,password)
        User.charge_user(user)
        print("Usuario Registrado!!")
        
    @staticmethod
    def sign_in():
        band=False
        Regi=False
        while band==False and Regi==False:
            email=input("Ingrese el correo: ")
            if User.validation_email(email)==True:
                password=input("Ingrese la contraseña: ")
                id_user=User.Valida_User(User.ruta, email, password)
                if id_user is not None:
                    user=User.instancia_User(User.ruta, id_user)
                    return user
                else:
                    print("Si desea reintentarlo ingrese 1 o si desea registrarse ingrese 0.")
                    Op=input("Ingrese su opción: ")
                    if Op == "0":
                        Regi=True
                        User.sign_up()
                    elif Op!=1:
                        band=True
                        
            else:
                print("Correo inválido.")           
        
        
    @staticmethod
    def Valida_User(ruta_json, email_id, password_id):
         List = Helper.load_file(ruta_json)
         if List is not None:
            b=False
            for data in List:
                if data['email']==email_id:
                    b=True
                    if data['password']==password_id:
                        return data['id']
                    else:
                        print("La contraseña ingresada no es válida..")
            if b is False:
                print("El correo ingresado es incorrecto o aún no se ha registrado..")
                return None
            
    @staticmethod
    def instancia_User(ruta_json, item_id):
        List=Helper.load_file(ruta_json)
        for data in List:
             if data['id']==item_id:
                  return User(data['name'],data['surname'],data['email'],data['password'])
             
    @staticmethod
    def validation_email(email):

        patron=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron, email):
            return True
        else:
            return False

    def charge_user(item):
        Helper.save_in_list(User.ruta, item.__dict__)

    def remove_user(item):
        Helper.delete_item(User.ruta, item)

    def __str__(self):
        return f"id: {self.id}\nNombre: {self.name}\nApellido: {self.surname}\nCorreo: {self.email}\nContraseña: {self.password}"
        


