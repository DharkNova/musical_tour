
from Data.Json_Operations import Helper
import re
from tkinter import messagebox

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
    def sign_up(self, correo, contra, nombre, apellido):
        email=correo
        if User.validation_email(email)==True:
            password=contra
            nam=nombre
            sur=apellido
            if User.valida_nombre(nam)==True and User.valida_nombre(sur)==True:
                user=User(nam,sur,email,password)
                User.charge_user(user)
                messagebox.showinfo(title="Informe", message="El usuario se a registrado con exito")
                return True
                
            else:
                messagebox.showerror(title="Error", message="El nombre o apellido es incorrecto, solo se permiten caracteres alfabeticos")
                return None
        else:
            messagebox.showerror(title="Error", message="El Correo ingresado es invalido")
            return None

    @staticmethod
    def sign_in(self, correo, contra):
        email=correo
        password=contra
        if User.validation_email(email)==True:
            id_user=User.Valida_User(User.ruta, email, password)
            if id_user is not None:
                user=User.instancia_User(User.ruta, id_user)
                return user
            else:
                return None
        else: 
            messagebox.showerror(title="Error", message="El Correo ingresado es incorrecto")          
        
        
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
                        messagebox.showerror(title="Error", message="Contraseña Incorrecta")
                        return None        
            if b is False:
                messagebox.showerror(title="Error", message="El usuario No se encuentra registrado")
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

    def agrega_historial(self, id):
        self.eventos_asistidos.append(id)
        
    def charge_user(item):
        Helper.save_in_list(User.ruta, item.__dict__)

    def remove_user(item):
        Helper.delete_item(User.ruta, item)

    def valida_nombre(self, ingreso):
        patron=re.compile("[a-zA-ZáéíóúñÁÉÍÓÚÑüÜ\s]+$")
        if patron.match(ingreso):
            return True
        else:
            return False
        
    def __str__(self):
        return f"id: {self.id}\nNombre: {self.name}\nApellido: {self.surname}\nCorreo: {self.email}\nContraseña: {self.password}"
        


