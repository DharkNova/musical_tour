from Models.Events import Event
from Views.view_evento import vista_evento

class Control_inicio:

    def obtiene_data(self):
        return Event.indice_eventos()

    
    def detalle_evento(evento):
        vista_evento.detalles_evento(evento)
        