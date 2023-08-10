import tkinter as tk
from Models.Review import Review
class control_evento:

    def __init__(self, app):
        #self.app=app
        pass        
    def Volver_busca(self):
        self.app.vista_buscador()
        pass
    def Volver_inicio(self):
        self.app.vista_inicio()
        pass
    def Agregar_ruta(self, id_ubi):
        #self.app.control_mapa.agregar_a_ruta(id_ubi)
        pass
    def Visualiza_ruta(self, id_ubi_event):
        ubis=self.app.ubicaciones
        for ubi in ubis:
            if ubi.id==id_ubi_event:
                ubicacion=ubi
        self.app.vista_mapa(ubicacion)       
        pass

    def agrega_comentario(id_event, id_user, valora, animo, comentario):
        #Review.crea_review(id_event, id_user, valora, animo, comentario)
        pass
    def marca_asistido(self, id_evento):
        #self.app.user.agrega_historial(id_evento)
        pass

    def cerrar_sesion(self):
        pass
