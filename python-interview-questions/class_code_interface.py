import random
from helpers.test import expect, runAllTests
from itertools import count
# Thoughts:
#   - Code generator
#       - Codes are 8 letter strings with - in the middle
#       - Code user connect
#           - each user can only have 5 codes
#           - if more then 5 generation should fail
#           - each code should be consumed only once and return the user
# Implementation
# - User
#   - id: string
#   - codes: int number of codes generated for user
#
# paren class
# - CodeRegistry
#   - generate(userId) // generates code for given user
#   - consume(code, userId) // consumes code from another user, userId is the user who is consuming the code


class CodeRegistry:
    # Singleton
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls.users_codes_len = dict()
            cls.codes_user = dict()
            cls.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return cls._instance

    def consume(self, code, consumerId):
        if code in self.codes_user and self.codes_user[code]["consumerId"] == None:
            self.codes_user[code]["consumerId"] = consumerId
            return self.codes_user[code]["userId"]
        else:
            return False

    def __generate_code(self):
        code = ""
        for _ in range(9):
            index = random.randrange(len(self.letters))
            code += self.letters[index]
        result = code[:5] + "-" + code[5:]
        return result

    def generate(self, userId):
        if userId in self.users_codes_len and self.users_codes_len[userId] >= 5:
            return ""
        code = self.__generate_code()
        while code in self.codes_user:
            code = self.__generate_code()
        self.codes_user[code] = dict({
            "userId": userId,
            "consumerId": None
        })
        if userId not in self.users_codes_len:
            self.users_codes_len[userId] = 1
        else:
            self.users_codes_len[userId] = self.users_codes_len[userId] + 1
        return code

class User:
    def __init__(self, id):
        self.id = id
        self.codeRegistry = CodeRegistry.instance()

    def generate(self):
        return self.codeRegistry.generate(self.id)

    def consume(self, code):
        return self.codeRegistry.consume(code, self.id)

def test1():
    Dan = User("Dan")
    expect("generates code correctly", bool(Dan.generate()), True )

def test2():
    Dan = User("Dan")
    Dan.generate()
    Dan.generate()
    expect("third code generated to pass", bool(Dan.generate()), True)
    Dan.generate()
    expect("fifth code generated to fail", bool(Dan.generate()), False)

def test3():
    Scott = User("Scott")
    Trav = User("Trav")
    code = Scott.generate()
    expect("Trav to consume Dan's code correctly", Trav.consume(code), "Scott")
    expect("Trav can't consume the code again", Trav.consume(code), False)

runAllTests([test1, test2, test3])