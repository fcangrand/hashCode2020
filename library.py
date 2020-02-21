class Library:

    # Constructeur
    def __init__(self, id, nbBooks, signupTime, nbBooksPerDay):
        self.id = int(id)
        self.nbBooks = int(nbBooks)
        self.signupTime = int(signupTime)
        self.nbBooksPerDay = int(nbBooksPerDay)
        self.books = []
        self.readBooks = []

    def addBook(self, book):
        self.books.append(book)

    def getNextBooksToScan(self):
        if self.nbBooksPerDay > len(self.books):
            self.nbBooksPerDay = len(self.books)
        booksToRead = self.books[:self.nbBooksPerDay]
        self.books = self.books[self.nbBooksPerDay:]
        self.readBooks = self.readBooks + booksToRead
        return booksToRead

    def getScore(self, nb_days):
        if self.signupTime >= int(nb_days):
            return 0
        scoreTotal = sum(b.score for b in self.books)
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
		    for bookInbooks in self.books:
			    if bookInbooks.index == bookToRemove.index:
				    self.books.remove(bookInbooks)
				    break
			    elif bookToRemove.score > bookInbooks.score:
				    break