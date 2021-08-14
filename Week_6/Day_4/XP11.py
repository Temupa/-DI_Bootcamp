# Exercise 11: Cinemax

family_ages =[]
age_input="0"
while age_input != "quit":
    age_input = input("Enter age of each family memeber who want to buy ticket: ")
    if age_input == "quit":
        break
    else:
        family_ages.append(age_input)
total_cost=0
for age in family_ages:
    if int(age)<3:
        total_cost+=0
    elif int(age)<12:
        total_cost+=10
    else:
        total_cost+=15
print(f"Your total cost is ${total_cost} for {len(family_ages)} tickets.")

names = ["Itai", "Ann", "Jana", "Genna", "Nastya"]
old_enough=[]
for name in names:
    age=input(f"How old is {name}?")
    if 21>int(age)>16:
        old_enough.append(name)
print("The following people may watch the movie: ")
for person in old_enough:
    print(person)