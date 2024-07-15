class Dog:
    def __init__(self, name: str, age: float, breed: str, weight: int):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight

    def bark(self):
        print(self.name, "goes bark")

dog1=Dog.bark("gyat")
        