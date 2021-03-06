import sys
from library import Library
from book import Book
import time
import collections

fname = sys.argv[1]
nb_libraries = 0
nb_different_books = 0
nb_days = 0
x = 0
book_scores = []
libraries = []

seconds = time.time()

# Partie Lecture fichier
with open("input/" + fname) as f:
    for line in f:
        if x == 0:
            # Lecture nb_different_books, nb_different_books, nb_days
            nb_different_books, nb_libraries, nb_days = line.split()
            nb_days = int(nb_days)
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
            sorted_x = sorted(libraries[-1].books.items(), key=lambda kv: kv[1], reverse=True)
            libraries[-1].books = collections.OrderedDict(sorted_x)
        x += 1

# Partie Algo...
scannedLibrairies = []
daysUntilNextSignUp = 0

nb_librairies = len(libraries)
librairiesSorted = libraries[:]

for x in range(nb_days):
    print(x)
    if daysUntilNextSignUp == 0 and nb_librairies > len(scannedLibrairies):
        librairiesSorted.sort(key=lambda lib: lib.getScore(nb_days - x), reverse=True)
        signingLibrary = librairiesSorted[0]
        daysUntilNextSignUp += signingLibrary.signupTime

    for lib in scannedLibrairies:
        lib.getNextBooksToScan()

    daysUntilNextSignUp -= 1

    if daysUntilNextSignUp <= 0 and x +1 != nb_days and len(librairiesSorted) > 0:
        scannedLibrairies.append(signingLibrary)
        books = signingLibrary.getAllFurtherReadBooks(nb_days - x)
        # Suppression par dictionnaire de tous les livres qui seront traités par la lib
        if x < nb_days - 1 and len(books) > 0:
          for allLib in libraries:
            if allLib != signingLibrary:
              allLib.removeBooks(books)
        librairiesSorted.pop(0)


# Suppression librairies sans livres lus
scannedLibrairiesWithBooks = list(filter(lambda lib: len(lib.readBooks) > 0, scannedLibrairies))
# Partie Ecriture Sortie
fichier = open("output/" + fname, "w+")
fichier.write(str(len(scannedLibrairiesWithBooks)) + "\n")
for lib in scannedLibrairiesWithBooks:
    fichier.write(str(lib.id) + " " + str(len(lib.readBooks)) + "\n")
    for book in lib.readBooks:
        fichier.write(str(book) + " ")
    fichier.write("\n")

fichier.close()

secondsEnd = time.time()
print("Local time:", secondsEnd - seconds)