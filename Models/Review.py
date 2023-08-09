from Data.Json_Operations import Helper

class Review:
    Cont=0
    ruta="Data\\Reviews.json"
    def __init__(self, id_event, id_user, rating,  reaction, comment):
        Review.Cont+=1
        self.id=Review.Cont
        self.id_event=id_event
        self.id_user=id_user
        self.rating=rating
        self.reaction=reaction
        self.comment=comment

    def crea_review(id_evento, id_usuario, valora, animo, comentario):
        review=Review(id_evento,id_usuario, valora, animo,  comentario)
        Helper.save_in_list(Review.ruta, review)

        
