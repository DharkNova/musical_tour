from Models.Users import User
class control_logueo:
    
    def __init__(self):
        pass
    def verifica_inicio(self, correo, contra):
        user=User.sign_in(self, correo, contra)
        return user