# Exercise 12 : Who Is Under 16?

names = ["Itai", "Ann", "Jana", "Genna", "Nastya"]
old_enough=[]
for name in names:
    age=input(f"How old is {name}?")
    if int(age)>16:
        old_enough.append(name)
print(old_enough)