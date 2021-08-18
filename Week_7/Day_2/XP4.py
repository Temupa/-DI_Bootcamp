# Exercise 4 : Random

from random import randint

def random(number):
    random = randint (1,100)
    if number == random:
        print("Success! You picked the same number!")
    else:
        print(f"Sorry! You picked {number} and the computer picked {random}.")

random(10)
