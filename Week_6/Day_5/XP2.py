# Exercise 2 : Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost=0
for value in family.values():
    if int(value) < 3:
        total_cost += 0
    elif int(value) < 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"Your total cost is ${total_cost} for {len(family)} tickets.")

