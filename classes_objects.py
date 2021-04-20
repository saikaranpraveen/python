class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def handling(self, handling):
        print (f"{self.brand} {self.model} has {handling} handling.")

    def __str__(self) -> str:
        return f"Brand = {self.brand}\nModel = {self.model}"


honda_city = Car("Honda", "City")
print(honda_city)

honda_city.handling("good")