#using return to get the desired result

def what_gender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"{gender} is an unknown gender."

print(what_gender("m"))
print(what_gender("M"))
print(what_gender("F"))
print(what_gender("f"))
print(what_gender("Hello"))
