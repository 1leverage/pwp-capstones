class User(object):
    """Keep track of users"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        """Returns the email associated with the user"""
        return self.email

    def change_email(self, address):
        """Changes the email associated with the user."""
        self.email = address
        print("The user {} email has been updated to {}".format(self.name, self.email))

    def read_book(self, book, rating=None):
        """Add book/rating key pair value"""
        self.books[book] = rating

    def get_average_rating(self):
        """Find ratings and returns average"""
        sum_of_rating = 0
        num_of_books = 0
        for ratings in self.books.values():
            if ratings:
                sum_of_rating += ratings
                num_of_books += 1
                average = sum_of_rating / num_of_books
        return average

    def __repr__(self):
        """Return user object"""
        return "User: {}, Email: {}, Books Read: {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        """Compare between users"""
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
    
    def get_books_read(self):
        """Returns books read by the user"""
        return len(self.books)

class Book(object):
    """All Books"""
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self, title):
        """Returns the title of a book"""
        return self.title
    
    def get_isbn(self):
        """Returns the ISBN of a book"""
        return self.isbn

    def set_isbn(self, isbn):
        """Changes the ISBN of a book"""
        self.isbn = isbn
        return  ("The ISBN for {} has been updated".format(self.title))
    
    def add_rating(self, rating):
        """Add a rating of a book"""
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __hash__(self):
        """Makes object hashable"""
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):
        """Compare books"""
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        sum_of_ratings = 0
        for rating in self.ratings:
            sum_of_ratings += rating
            average = sum_of_ratings / len(self.ratings)
        return average


class Fiction(Book):
    """Fiction Books (Subclass of Book)"""
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self, author):
        """Return author of book"""
        return self.author
    
    def __repr__(self):
        """String Reprensentation of book title and author"""
        return "{} by {}".format(self.title, self.author)

class NonFiction(Book):
    """Non-Fiction books (Sublcass of Book)"""
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        """Return subject"""
        return self.subject

    def get_level(self):
        """Return level"""
        return self.level

    def __repr__(self):
        """String Reprensentation of book title, level and subject"""
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater():
    """Main Application"""
    def __init__(self):
        self.users = {}
        self.books = {}
        
    def create_book(self, title, isbn):
        """Create book"""
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        """Create Fiction book"""
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        """Create Non-Fiction book"""
        return NonFiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        """Adds read book to user, adds book to self.books if not already there"""
        if self.users[email]:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1           
        else:
            print("No user with email {}".format(email))
    
    def add_user(self, name, email, user_books=None):
        """Add new user and books read"""
        self.users[email] = User(name, email)
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        """Print keys in book catalog"""
        for key in self.books.keys():
            print(key)

    def print_users(self):
        """Print users values in user dictionary"""
        for users in self.users.values():
            print(users)

    def most_read_book(self):
        """Returns book that has been read the most"""
        count = 0
        most_read = ""
        for book, value in self.books.items():
            if value > count:
                count = value
                most_read = book
        return most_read

    def highest_rated_book(self):
        """Returns highest rated book"""
        rated_book = ""
        rating_count = 0
        for book in self.books:
            if book.get_average_rating() > rating_count:
                rating_count = book.get_average_rating()
                rated_book = book
        return rated_book

    def most_positive_user(self):
        """Return the user with the highest average rating"""
        highest_user = ""
        count = 0
        for user in self.users.values():
            if user.get_average_rating() > count:
                count = user.get_average_rating()
                highest_user = user
        return highest_user
    
    def get_n_most_read_books(self, n):
        """Return the most read books in descending order"""
        if type(n) == int:
            books_sorted = [k for k in sorted(self.books, key=self.books.get, reverse=True)]
            return books_sorted[:n]
        else:
            print("Your input {} is not a int. Please enter a valid number.".format(n))

    def get_n_most_prolific_readers(self, n):
        """Return users that have read the most books in descending order"""
        if type(n) == int:
            readers = [(reader, reader.get_books_read()) for reader in self.users.values()]
            readers_sorted = [k[0] for k in sorted(readers, key=lambda reader: reader[1], reverse=True)]
            return readers_sorted[:n]
        else:
            print("Your input {} is not a int. Please enter a valid number.".format(n))


        




        






