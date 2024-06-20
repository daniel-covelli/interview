from helpers.test import expect, runAllTests

'''
Create a library system:
 - Multiple users should have multiple sets of books associated with themselves
    - getBooks(): gets all unique books
    - getBooks(user): gets unique book set for a user
    - getActiveBook(user): gets the name of the active book for a user
    - deleteBook(user, book): deletes a book from the users library
    - addUser(name): adds a user to the system
    - addBook(user, book): adds book for user
    - setBook(user, book): defines which book the user is reading

Classes:
    Library
        - here we will implement all of the methods above
    Book
        - id: string
        - title: string
    User:
        - books: {id: Book()}
        - activeBook: id / None
'''
class Book:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class User:
    def __init__(self, id):
        self.id = id
        self.books = dict()
        self.activeBook = None

    def getBooks(self):
        return [book.name for book in self.books.values()]

    def getActiveBook(self):
        if self.activeBook and self.activeBook in self.books:
            return self.books[self.activeBook].name
        return False

    def removeBook(self, bookId):
        if bookId in self.books:
            del self.books[bookId]
            return True
        return False

    def addBook(self, bookId, bookName):
        if bookId in self.books:
            return False
        self.books[bookId] = Book(bookId, bookName)
        return True

    def setActiveBook(self, bookId):
        if bookId in self.books:
            self.activeBook = bookId
            return True
        return False

class Library:
    def __init__(self):
        self.__users = dict()

    def getAllBooks(self):
        uniqueBooks = dict()
        for user in self.__users.values():
            for key, book in user.books.items():
                if key not in uniqueBooks:
                    uniqueBooks[key] = book
        return [book.name for book in uniqueBooks.values()]

    def getBooks(self, userId):
        if userId in self.__users:
            user = self.__users[userId]
            return user.getBooks()
        return []

    def getActiveBook(self, userId):
        if userId in self.__users:
            user = self.__users[userId]
            return user.getActiveBook()
        return False

    def deleteBook(self, userId, bookId):
        if userId in self.__users:
            user = self.__users[userId]
            return user.removeBook(bookId)
        return False

    def addUser(self, userId):
        if userId in self.__users:
            return False
        self.__users[userId] = User(userId)
        return True

    def getUsers(self):
        return [id for id in self.__users]

    def addBook(self, userId, bookId, bookName):
        if userId in self.__users:
            return self.__users[userId].addBook(bookId, bookName)
        return False

    def setActiveBook(self, userId, bookId):
        if userId in self.__users:
            return self.__users[userId].setActiveBook(bookId)
        return False

# Tests


def test1():
    library = Library()
    library.addUser("u1")
    library.addUser("u1")
    expect("user added correctly", ["u1"], library.getUsers())

def test2():
    library = Library()
    library.addUser("u2")
    library.addBook("u2", "b1", "To kill a mockingbird")
    library.addBook("u2", "b2", "All quiet")
    library.addUser("u1")
    library.addBook("u1", "b1", "Should not see this name")
    expect("books added correctly", ["To kill a mockingbird", "All quiet"], library.getAllBooks())

def test3():
    library = Library()
    library.addUser("u2")
    library.addBook("u2", "b1", "To kill a mockingbird")
    library.addBook("u2", "b2", "All quiet")
    expect("getActiveBook response correctly to a active book not being set", library.getActiveBook("u2"), False)
    library.setActiveBook("u2", "b2")
    expect("getActiveBook response correctly when active book is set", library.getActiveBook("u2"), "All quiet")

def test4():
    library = Library()
    library.addUser("u2")
    library.addBook("u2", "b1", "Mockingbird")
    library.addBook("u2", "b2", "All quiet")
    expect("users active books returns correctly", library.getBooks("u2"), ["Mockingbird", "All quiet"])
    library.deleteBook("u2", "b2")
    expect("library responds to deleting a book correctly", library.getBooks("u2"), ["Mockingbird"])

runAllTests([test1, test2, test3, test4])