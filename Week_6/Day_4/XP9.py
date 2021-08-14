# Exercise 9: Favorite Fruits

user = input("Please enter your favorite fruits, serparate the fruits with space ")
list_fruits = list(user.split( ''))
user_fav = input("enter your choosen fruits")
if user_fav in list_fruits: 
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")