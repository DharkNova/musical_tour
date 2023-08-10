from Models.Events import Event

class Search:

    All_Events=Event.indice_eventos()

    def Buscador(self, Nombre, Artista, Genero):
        resultados=set()
        for Eventos in Search.All_Events:
            if Nombre is not None:
                if Eventos.name==Nombre:
                    resultados.add(Eventos)
            if Artista is not None:
                if Eventos.artist==Artista:
                    resultados.add(Eventos)
            if Genero is not None:
                if Eventos.genre==Genero:
                    resultados.add(Eventos)
                    
        if len(resultados)==0:
           print("No se encontró ningún evento")
        else:
            return resultados

    @staticmethod
    def Busqueda(self, para1=None ,para2=None, para3=None):
        if para1 is not None:
            Nombre=Search.determina_nombre(para1)
            Artista=Search.determina_artista(para1)
            Genero=Search.determina_genero(para1)

        if para2 is not None:
            if Nombre is None:
                Nombre=Search.determina_nombre(para2)
            if Artista is None:
                Artista=Search.determina_artista(para2)
            if Genero is None:
                Genero=Search.determina_genero(para2)
            
        if para3 is not None:
            if Nombre is None:
                Nombre=Search.determina_nombre(para3)
            if Artista is None:
                Artista=Search.determina_artista(para3)
            if Genero is None:
                Genero=Search.determina_genero(para3)

        return Search.Buscador(Nombre, Artista, Genero)

    @staticmethod
    def determina_nombre(self,parametro):
        b=False
        for objeto in Search.All_Events:
            if objeto.name.lower()==parametro.lower():
                b=True
        if b==False:
            return None
        else:
            return parametro
    @staticmethod
    def determina_artista(self,parametro):
        b=False
        for objeto in Search.All_Events:
            if objeto.artist.lower()==parametro.lower():
                b=True
        if b==False:
            return None
        else:
            return parametro
    @staticmethod
    def determina_genero(self,parametro):
        b=False
        for objeto in Search.All_Events:
            if objeto.genre.lower()==parametro.lower():
                b=True
        if b==False:
            return None
        else:
            return parametro

    def filtra_hora(self, hora_ini, hora_fin, lista):
        hora_ini_iso=Event.charge_time(hora_ini)
        hora_fin_iso=Event.charge_time(hora_fin)
        lista_filtrada=[]
        for evento in lista:
           if evento.time_start>=hora_ini_iso and evento.time_end<=hora_fin_iso:
               lista_filtrada.append(evento)
        return lista_filtrada       
        

