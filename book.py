class Book:

    # Constructeur
    def __init__(self, id, score):
        self.index = id
        self.score = int(score)

    def __repr__(self):
        return "Book " + str(self.index) + " avec un score de " + str(self.score)

    def __eq__(self, other):
        if not isinstance(other, Book):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.index == other.index