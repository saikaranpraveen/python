my_tuple = ("Banana", "Cherry", "Apples")

#Tuples are ordered, unchangeable and allow for duplicates

print(len(my_tuple))

one_item_tuple = ("Oranges",) # Do not forget the comma
print(type(one_item_tuple))

my_list = list(my_tuple)
my_list.append("Oranges")
new_tuple = tuple(my_list)
print(new_tuple)