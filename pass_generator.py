import string
import random

class Characters:
    
    #constructor of the class
    def __init__(self, symbols, nums):
        self.symbols = symbols
        self.nums = nums

    def capital_alphabets(self):
        capital = list(string.ascii_uppercase)
        return capital

    def small_alphabets(self):
        small_letters = list(string.ascii_lowercase)
        return small_letters

    def special_characters(self):
        symbols = self.symbols
        return symbols.split(" ")

    def numbers(self):
        nums = self.nums.split(" ")
        return nums

class Password:
    def generate_password(self):
        nums = "0 1 2 3 4 5 6 7  8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5"
        signs = "+ @ # % [ & ] / ( ) ? } £ $ _ ~ ¦ - | { < > ` ^ = "
        ch = Characters(signs, nums) #assigning of class in ch
        capital_letters = ch.capital_alphabets()
        small_letters = ch.small_alphabets()
        numbers = ch.numbers()
        symbols = ch.special_characters()

        characters = [capital_letters, small_letters, numbers, symbols]
        pass_length = int(input("What should be the length of password : ?"))
        password = ""
        for length in range(0, pass_length):
            index1 = int (random.uniform(0,4)) #there are four lists capital, small, numbers and symbols
            index2 = int(random.uniform(0, 26)) #every list has 26 characters
            character = characters[index1][index2]
            password += str(character)
        return password


def _main():
        ps = Password()
        password = ps.generate_password()
        print(f"password:{password}")
        return password
