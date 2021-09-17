from anagram_checker import AnagramChecker

def Menu():
    while True:
        user_word = input("Input a word or write a 'e' to exit the Anagram Checker: ")
        if user_word.isalpha(): 
            return user_word

def anagrams(): 
    print("Welcome to Anagram Checker! ")
    user_word = Menu()
    if user_word.lower() == 'e':
        print('Exiting the Anagram Checker ')
        return " "
    print(f"Your Word: {user_word}")
    print("This is a valid English word.")
    word_list = open('D:\BootCampDI2021\-DI_Bootcamp\Week_10\Day_5\Exersice\sowpods.txt','r').read().splitlines()
    anagrams = AnagramChecker(word_list)
    print(f"Anagrams for your word: {anagrams.get_anagrams(user_word)}")

anagrams()