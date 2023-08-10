class control_mapa:
        def __init__(self, app=None, ubicaciones=None, eventos=None):
            #self.ubicaciones=ubicaciones
            #self.eventos=eventos
            #self.app=app
            pass

        def Volver_evento(self, id_ubi):
            for i in self.eventos:
                if i.id_position==id_ubi:
                    self.app.vista_buscador(i)
            pass

        def Volver_inicio(self):
            self.app.vista_inicio()
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

                
        def agregar_a_ruta(self, id_ubi):
            for ubi in self.ubicaciones:
                if ubi.id==id_ubi:
                    ubicacion=ubi
                    break
            self.app.ruta.destinations.append(id_ubi)
            self.app.agrega_ruta_vista(ubicacion.coordenadas)
            if self.app.vista_mapa.boton_fin_ruta.state=="normal":
                self.app.vista_mapa.agregar_event_ini(ubicacion.coordenadas)
            pass
        def quita_ruta(self,coords):
            id_ubi=self.compara_cords(coords)
            for id in self.app.ruta.destinations:
                if id==id_ubi:
                    self.app.ruta.destinations.remove(id)

        def limpia_lista(self):
            self.app.ruta.destinations.clear()

                    


                                