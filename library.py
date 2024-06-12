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
        return None

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
            for key, book in user.books:
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
            return user.getActiveBooks()
        return None

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

def expect(index, expected, actual):
    if expected == actual:
        print("Test " + str(index)+ " passed, expected " + str(expected) + " equaled " + str(actual))
    else:
        print("Test " + str(index) + " failed, Expected " + str(expected) + " did not equal actual " + str(actual))
        raise Exception("Test failed :(")

def test1(index):
    library = Library()
    library.addUser("u1")
    library.addUser("u1")
    expect(index, ["u1"], library.getUsers())

def test2(index):
    library = Library()
    library.addUser("u1")
    library.addBook("u1", "b1", "To kill a mockingbird")
    library.addBook("u2", "b1", "To kill a mockingbird")
    expect(index, ["To kill a mockingbird"], library.getAllBooks())

def runAllTests():
    tests = [test1, test2]
    for i, test in enumerate(tests):
        test(i)

runAllTests()