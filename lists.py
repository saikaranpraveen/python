#Basic methods with lists

my_list = [1, 4, -20, 3, 7, 99]

my_list.sort()
print(my_list) #sorts in ascending order

my_list.reverse() #sorts in descending order
print(my_list)

my_list.append(1000)
print(len(my_list))

print(4 in my_list)
print(5 not in my_list)

my_list.remove(4)
print(my_list)

del my_list[0]
print(my_list)

my_list_new = ["Banana", "Cherry", "Apples"]

for x in my_list_new:
    print(x)
