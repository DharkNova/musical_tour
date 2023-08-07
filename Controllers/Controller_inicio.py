from Models.Events import Event
from Views.view_evento import vista_evento
from tkinter import messagebox

class Control_inicio:
    def __init__(self):
        self.vista_evento=vista_evento
    def obtiene_data(self):
        return Event.indice_eventos()
    def cambia_evento(self, objeto): 
         vista_evento(objeto)
         
         



    
    


        