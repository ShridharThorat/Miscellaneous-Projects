import utils
import sorts

small_books_path = 'Computer Science Path/A Sorted Tale/books_small.csv'
bookshelf = utils.load_books(small_books_path)
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

# print()
# sort_1 = sorts.bubble_sort(bookshelf, sorts.by_title_ascending)
# for book in sort_1:
#     print(book['title_lower'])

# print()
# sort_2 = sorts.bubble_sort(bookshelf_v1, sorts.by_author_ascending)
# for book in sort_1:
#     print(book['author_lower'])

# print()
# sort_2 = sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, sorts.by_author_ascending)
# for book in sort_1:
#     print(book['author_lower'])


long_books_path = 'Computer Science Path/A Sorted Tale/books_small.csv'
long_bookshelf = utils.load_books(long_books_path)
long_bookshelf_v1 = long_bookshelf.copy()
print()
sort_3 = sorts.bubble_sort(long_bookshelf_v1, sorts.by_total_length)

print()
sort_3 = sorts.quicksort(long_bookshelf, 0, len(bookshelf_v2) - 1, sorts.by_total_length)