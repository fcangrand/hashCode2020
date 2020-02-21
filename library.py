class Library:

    # Constructeur
    def __init__(self, id, nbBooks, signupTime, nbBooksPerDay):
        self.id = int(id)
        self.nbBooks = int(nbBooks)
        self.signupTime = int(signupTime)
        self.nbBooksPerDay = int(nbBooksPerDay)
        self.books = {}
        self.readBooks = []

    def addBook(self, book):
        self.books[book.index] = book.score

    def getNextBooksToScan(self):
        if self.nbBooksPerDay > len(self.books):
            self.nbBooksPerDay = len(self.books)
        booksToRead = list(self.books)[:self.nbBooksPerDay]
        for i in booksToRead:
            del self.books[i]
        self.readBooks = self.readBooks + booksToRead
        return booksToRead

    def getScore(self, nb_days):
        if self.signupTime >= int(nb_days):
            return 0
        scoreTotal = sum(self.books.values())
        return (1 / self.signupTime) * scoreTotal * self.nbBooksPerDay# 1 / self.nbBooks / self.nbBooksPerDay + 1 / self.signupTime * 1 + 1 - 1 / scoreTotal

    def __repr__(self):
        librairieString = "id:" + str(self.id) + " nbBooks:" + str(self.nbBooks) + " signupTime:" + str(
            self.signupTime) + " nbBooksPerDay:" + str(self.nbBooksPerDay)
        for i in range(len(self.books)):
            librairieString += "\n"
            librairieString += self.books[i].__repr__()
        librairieString += "\n" + str(self.getScore())
        return librairieString

    def removeBooks(self, readByOtherLibrary):
        for bookToRemove in readByOtherLibrary:
            if bookToRemove in self.books:
                del self.books[bookToRemove]