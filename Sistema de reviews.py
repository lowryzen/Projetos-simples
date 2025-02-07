class Analise:

    todas_reviews = {}

    def __init__(self):
        self.review = {}

    def adicionar(self, add:dict):
        self.review.update(add)
        Analise.todas_reviews.update(self.review)