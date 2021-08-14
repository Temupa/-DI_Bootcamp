# Exercise 10: Who Ordered A Pizza ?

print("topping menu : green olives , Tuna , Corn , Pepperoni , tomato , onion ")
user_topping = input("Please type a pizza topping (type 'quit' to stop): ")
list_topping = []
price = 10

while user_topping != "quit":
    print(f'{user_topping}The topping has been added')
    price += 2.5
    list_topping.append(user_topping)
    user_topping = input("Please type a pizza topping (type 'quit' to stop): ")

    print(f'your topping are :\n {list_topping}')
    print(f'your price is {price}')