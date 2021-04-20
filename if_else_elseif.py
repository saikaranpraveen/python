a = float(input("Enter the first number you want to compare: "))
b = float(input("Enter the second number you want to compare: "))

if a < b :
    print (str(b) +" is greater than " + str(a))
elif a > b:
    print(str(a) + " is greater than " + str(b))
elif a == b:
    print(str(a) + " is equal to " + str(b))
else:
    print("Invalid Entry")