#while lists are ordered and allow for duplicates, sets are unordered and do not allow duplicates
letters_one = {"A", "B", "B", "C" }
letters_two = {"E", "F", "F", "B"}

#set union
print(letters_one | letters_two)

#set intersection
print(letters_one & letters_two)

#set difference
print(letters_one - letters_two)