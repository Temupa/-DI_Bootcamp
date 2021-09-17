
class AnagramChecker():
    def __init__(self, Textlist):
        # will show the list of sowpods.txt
        self.Textlist = Textlist
        
    # check if the given word is a valid word
    def is_valid_word(self, word):

        if word in self.Textlist:
            return True
            
        else:
            return False

    # find all anagrams for the given word
    def get_anagrams(self, word):
        word.assertEquals(Textlist(True))

    # will sort if the anagram is Equals 
    def is_anagram(self, word1, word2):

        if word1 == word2:
            return False

        if (sorted(word1) == sorted(word2)):
            return True

        else:
            return False

    def play(self):
        self.get_anagrams(self.get_word().upper())

Textlist = open('D:\BootCampDI2021\-DI_Bootcamp\Week_10\Day_5\Exersice\sowpods.txt','r').read().splitlines()

anagram = AnagramChecker(Textlist)
print(anagram.is_valid_word('ABACTERIAL'))
