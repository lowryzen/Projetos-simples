class Analise:
    def __init__(self, reviews=None):
        if reviews is None:
            reviews = {}
        self.reviews = reviews

    def todas_reviews(self) -> None:
        print(self.reviews)

    def adicionar_reviews(self, nome, avaliacao) -> None:
        self.reviews[nome] = avaliacao