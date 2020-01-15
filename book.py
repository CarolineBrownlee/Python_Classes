# A class is not a thing that you're going to reference it's just instructions for how to make a thing

class Book:

    def __init__(self):
        # Establish the properties of each book
        # with a default value
        # these are attributes
        # "self" is kind of like "this"
        self.title = ""
        self.publisher = ""
        self.author = ""
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page

book_one = Book()
book_one.title = "Harry Potter and the Sorcerer's Stone"
book_one.author = "J.K. Rowling"
book_one.current_page = 1
# print(f"I am reading {book_one.title} by {book_one.author}.")
book_one.start_reading()
book_one.stop_reading(197)
book_one.start_reading()
book_one.stop_reading(568)
book_one.start_reading()

book_two = Book()
book_two.title = "The Awakening"
book_two.author = "Kate Chopin"
book_two.current_page = 197
# book_two.start_reading()