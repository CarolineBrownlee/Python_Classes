# A class is not a thing that you're going to reference it's just instructions for how to make a thing

class Book:
    # init is method is when you set your properties
    # you use a class to create instances of that class which are objects, this is how you create objects in python
    # 
    def __init__(self, author, title):
        # Establish the properties of each book
        # with a default value
        # these are attributes
        # runs every time an instance is created
        # "self" is kind of like "this"
        self.title = title
        self.publisher = ""
        self.author = author
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} by {self.author} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page

book_one = Book("J.K. Rowling", "Harry Potter and the Sorcerer's Stone")

# book_one.title = "Harry Potter and the Sorcerer's Stone"
# book_one.author = "J.K. Rowling"
# book_one.current_page = 1
# print(f"I am reading {book_one.title} by {book_one.author}.")

book_one.start_reading()

# book_one.stop_reading(197)
# book_one.start_reading()
# book_one.stop_reading(568)
# book_one.start_reading()

# book_two = Book()
# book_two.title = "The Awakening"
# book_two.author = "Kate Chopin"
# book_two.current_page = 197
# book_two.start_reading()