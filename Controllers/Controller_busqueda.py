from Models.search_and_filter import Search

class control_busqueda:
    def __init__(self, app):
        self.app=app

    def volver(self):
        self.app.vista_inicio()

    def buscar(self, texto):
       return Search.Busqueda(texto)
    
    def filtrar(self, hora_ini, hora_fin, lista):
        return Search.filtra_hora(self, hora_ini, hora_fin, lista)

    def abre_evento(self, evento, band):
        self.app.vista_evento(evento, band)
