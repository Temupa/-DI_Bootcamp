# Exercise 14

sandwich_orders = ["American sub","Shawarma","Bun Kebab","pastrami","Falafel","Sabich"]
print("Sorry, we're out of Shawarma.")
updated_list = []
for sandwich in sandwich_orders:
    if sandwich != "Falafel":
        updated_list.append(sandwich)
finished_sandwiches = []
for item in updated_list:
    print(f"I made your {item} sandwich.")
    finished_sandwiches.append(item)