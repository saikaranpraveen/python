file = open("./text.txt", "r+")
file.write("Python programming is awesome.\n")
file.write("SIAM Computing.\n")
file.close()

file = open("./text.txt", "a")
file.write("File Handling in Python.\n")
file.close()

file = open("./text.txt", "r")
print(file.read())

import os.path
file_name = "./texxx.txt"
if os.path.isfile((file_name)):
    with open(file_name, "r") as file:
     print(file.read())
else:
    print(f"{file_name} is not a valid file name.\n")


file_name = "./text.txt"
if os.path.isfile((file_name)):
    with open(file_name, "r") as file:
     print(file.read())
else:
    print(f"{file_name} is not a valid file name.")