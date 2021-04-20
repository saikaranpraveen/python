#comparing two numbers using functions

def compare_two(a,b):
    if a < b:
        print(str(b) + " is greater than " + str(a))
    elif a > b:
        print(str(a) + " is greater than " + str(b))
    elif a == b:
        print(str(a) + " is equal to " + str(b))
    else:
        print ("Invalid Entry")


compare_two(20,400)
