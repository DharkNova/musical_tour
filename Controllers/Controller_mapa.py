class control_mapa:
        def __init__(self, app=None, ubicaciones=None, eventos=None):
            #self.ubicaciones=ubicaciones
            #self.eventos=eventos
            #self.app=app
            pass
        def compara_coords(self, coords):
            for ubi in self.ubicaciones:
                if ubi.coordenas==coords:
                    id=ubi.id
                    return id
            pass
        def compara_ids(self, id):
            for event in self.eventos:
                if event.id_position==id:
                    return event
                    
                
        def abre_evento(self, evento):
            self.app.vista_evento(evento)
            pass

                
        def agregar_a_ruta(self, variable):
            if isinstance(variable, tuple):
                id_ubi=self.compara_coords(variable)
            else:
                id_ubi=variable

            for ubi in self.ubicaciones:
                if ubi.id==id_ubi:
                    ubicacion=ubi
                    break
            self.app.ruta.destinations.append(id_ubi)
            self.agrega_ruta_vista(ubicacion)
            pass
                    


                                