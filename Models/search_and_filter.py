from Models.Events import Event

class Search:
    
    All_Events=Event.indice_eventos()

    def Buscador(Nombre, Artista, Genero):
        resultados=[]
        if (Nombre is None and Artista is None and Genero is None):
            return "No se asignó nada para buscar..."
        else:
            for event in Search.All_Events:
                if (Nombre is None or event.name.lower()==Nombre) and \
                (Artista is None or event.artist.lower()==Artista) and \
                (Genero is None or event.genre.lower()==Genero):
                    resultados.append(event)

        return resultados

    def Ordena_busqueda(para1=None ,para2=None, para3=None):

        if Search.determina_nombre(para1)==None:
            if Search.determina_artista(para1)==None:
                if Search.determina_genero(para1)==None:
                    Genero=Search.determina_genero(para1)
            else:
                Artista=Search.determina_artista(para1)
        else:
            Nombre=Search.determina_nombre(para1)


        if Search.determina_nombre(para2)==None:
            if Search.determina_artista(para2)==None:
                if Search.determina_genero(para2)==None:
                    print("El segundo valor ingresado no es válido.")
                else:
                    Genero=Search.determina_genero(para2)
            else:
                Artista=Search.determina_artista(para2)
        else:
            Nombre=Search.determina_nombre(para2)


        if Search.determina_nombre(para3)==None:
            if Search.determina_artista(para3)==None:
                if Search.determina_genero(para3)==None:
                    print("El tercer valor ingresado no es válido.")
                else:
                    Genero=Search.determina_genero(para3)
            else:
                Artista=Search.determina_artista(para3)
        else:
            Nombre=Search.determina_nombre(para3)
        

    def determina_nombre(self, parametro):
        for objeto in self.lista:
            LisNombres=str.lower(objeto['name'])
        paraNom=str.lower(parametro)
        Nombre=None
        for nombre in LisNombres:
            if nombre==paraNom:
                Nombre=paraNom
        return Nombre
            

    def determina_artista(self, parametro):
        for objeto in self.lista:
            Lisartistas=str.lower(objeto['artist'])
        paraArt=str.lower(parametro)
        Artista=None
        for artista in Lisartistas:
            if artista==paraArt:
                Artista=paraArt
        return Artista
            

    def determina_genero(self, parametro):
        for objeto in self.lista:
            Lisgenero=str.lower(objeto['genre'])
        paraGen=str.lower(parametro)
        Genero=None
        for genero in Lisgenero:
            if genero==paraGen:
                Genero=paraGen
        return Genero
    

