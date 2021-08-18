# Exercise 5 : Let’s Create Some Personalized Shirts !

def make_shirt(size , text):
    print(f"Print a shirt in size {size} with the message {text} on it. ")

make_shirt("M","My rules your code")

def make_shirt(size="L", text="I love Python"):
    print(f"Print a shirt in size {size} with the message {text} on it.")

make_shirt()
make_shirt(size="S")
make_shirt(text="Python Rocks!")