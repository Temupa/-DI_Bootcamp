# Exercise 1 : Favorite Numbers

my_fav_numbers = {1,2,3,4,5}
my_fav_numbers.update((6,7))
my_fav_numbers.remove(7)

friend_fav_numbers = {101,105,106}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)