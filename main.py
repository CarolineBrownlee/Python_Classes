from book import Book
from library import Library

book_one = Book("J.K. Rowling", "Harry Potter and the Sorcerer's Stone")
print(book_one.title, book_one.author)

# book_one.title = "Harry Potter and the Sorcerer's Stone"
# book_one.author = "J.K. Rowling"
# book_one.current_page = 1
# print(f"I am reading {book_one.title} by {book_one.author}.")

book_one.start_reading()

# book_one.stop_reading(197)
# book_one.start_reading()
# book_one.stop_reading(568)
# book_one.start_reading()

book_two = Book("Kate Chopin", "The Awakening")
# book_two = Book()
# book_two.title = "The Awakening"
# book_two.author = "Kate Chopin"
# book_two.current_page = 197

book_two.start_reading()

book_three = Book("Eric Carle", "The Very Hungry Caterpillar")
book_four = Book("Margaret Wise Brown", "Goodnight Moon")

nss_library = Library("THE NSS LIBRARY")
print(nss_library.name)

nss_library.add_book(book_one)
nss_library.add_book(book_two)
nss_library.add_book(book_three)
nss_library.add_book(book_four)

nss_library.list_books()

nss_library.set_address("301 Plus Park Blvd")

print(nss_library.address)



