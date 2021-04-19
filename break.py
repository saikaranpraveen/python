number = 0

def count_till_five(number):
    while True:
        number += 1
        print(number)
        if number == 5:
            break
    print("Loop breaks at five.")

count_till_five(number)