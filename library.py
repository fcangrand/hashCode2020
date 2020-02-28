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

    def getAllFurtherReadBooks(self, nb_days_left):
        nb_books_read = nb_days_left * self.nbBooksPerDay
        if (nb_books_read > len(self.books)):
            nb_books_read = len(self.books)
        all_books_read = list(self.books)[:nb_books_read]
       # print('all_books_read', all_books_read)
        return all_books_read

    def getScore(self, nb_days):
        if self.signupTime >= int(nb_days):
            return 0
        # Calcul du score exact sur les X jours restants
        remaining_days = nb_days - self.signupTime
        nb_books_read = remaining_days * self.nbBooksPerDay
        score = sum(list(self.books.values())[:nb_books_read])
        return score / self.signupTime

    def __repr__(self):
        librairie_string = "id:" + str(self.id) + " nbBooks:" + str(self.nbBooks) + " signupTime:" + str(
            self.signupTime) + " nbBooksPerDay:" + str(self.nbBooksPerDay)
        for i in range(len(self.books)):
            librairie_string += "\n"
            librairie_string += self.books[i].__repr__()
        librairie_string += "\n" + str(self.getScore())
        return librairie_string

    def removeBooks(self, readByOtherLibrary):
        for bookToRemove in readByOtherLibrary:
            if bookToRemove in self.books:
                del self.books[bookToRemove]