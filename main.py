import sys
from library import Library
from book import Book

fname = sys.argv[1]
x = 0
nb_libraries = 0
nb_different_books = 0
nb_days = 0

book_scores = []
libraries = []

# Partie Lecture fichier
with open("input/" + fname) as f:
    for line in f:
        if x == 0:
            # Lecture nb_different_books, nb_different_books, nb_days
            nb_different_books, nb_libraries, nb_days = line.split()
        elif x == 1:
            # Lecture score livres
            books = line.split()
            for i in range(len(books)):
                book_scores.append(books[i])
        elif x % 2 == 0:
            # Lecture librairies
            tmp_nb_book, tmp_nb_days_to_sign_up, nb_books_per_day = line.split()
            libraries.append(Library(x / 2 - 1, tmp_nb_book, tmp_nb_days_to_sign_up, nb_books_per_day))
        else:
            # Lecture des livres de la librairie
            book_ids = line.split()
            for i in range(len(book_ids)):
                book_id = int(book_ids[i])
                libraries[-1].addBook(Book(book_id, book_scores[book_id]))
            libraries[-1].books.sort(key=lambda b: b.score, reverse=True)
        x += 1

# Partie Algo...
#print('nb_libraries', nb_libraries)
#print('nb_different_books', nb_different_books)
#print('nb_days', nb_days)

#print('Libraries :')
#for i in range(len(libraries)):
#    print(libraries[i])



scannedLibrairies = []
daysUntilNextSignUp = 0

librairiesSorted = libraries[:]
# librairiesSorted.sort(key=lambda lib: lib.signupTime)
librairiesSorted.sort(key=lambda lib: lib.getScore(nb_days), reverse=True)

librairiesWithBookSent = []

for x in range(int(nb_days)):
    print(x)
    if daysUntilNextSignUp == 0:
        if len(librairiesSorted) > len(scannedLibrairies):
          signingLibrary = librairiesSorted[len(scannedLibrairies)]
          daysUntilNextSignUp += signingLibrary.signupTime

    for lib in scannedLibrairies:
        books = lib.getNextBooksToScan()
		# A optimiser
        #if x < int(nb_days):
        #  for allLib in libraries:
        #     allLib.removeBooks(books)

    daysUntilNextSignUp -= 1

    if daysUntilNextSignUp <= 0 and len(librairiesSorted) != len(scannedLibrairies) and x +1 != nb_days:
        # print(signingLibrary)
        scannedLibrairies.append(signingLibrary)



# Partie Ecriture Sortie
fichier = open("output/" + fname, "w+")
fichier.write(str(len(scannedLibrairies)) + "\n")
for lib in scannedLibrairies:
    fichier.write(str(lib.id) + " " + str(len(lib.readBooks)) + "\n")
    for book in lib.readBooks:
        fichier.write(str(book.index) + " ")
    fichier.write("\n")

fichier.close()
