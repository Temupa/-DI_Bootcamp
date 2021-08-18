# Exercise 6 : Magicians …

mag_names=["Israel","Shafik","Anna","Bruce"]

def show_magicians(list):
    for name in list:
        print(name)
        
show_magicians(mag_names)    

def make_great(list):
    for i in range(len(list)):
        list[i] += " the Great"
    for index, name in enumerate(list):
        list[index] += " the great"
make_great(mag_names)
show_magicians(mag_names)