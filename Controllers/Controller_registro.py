from Models.Users import User

class control_registro:
    
    def registrar(self, correo, contra, nombre, apellido):
        valor=User.sign_up(self, correo, contra, nombre, apellido)
        return valor