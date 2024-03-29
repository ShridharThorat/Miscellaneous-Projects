import csv


# This code loads the current book
# shelf data from the csv file
def load_books(filename):
    '''
    Returns bookshelf data as a list from a csv file
    '''
    bookshelf = []
    with open(filename) as file:
        shelf = csv.DictReader(file)
        for book in shelf:
            # add your code here
            bookshelf.append(book)
            book['title_lower'] = book['title'].lower()
            book['author_lower'] = book['author'].lower()
            print(book)
    return bookshelf
