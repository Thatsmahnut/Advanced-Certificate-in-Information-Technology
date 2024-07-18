# class Dog:
#     def init__(self, name: str, age: float, breed: str, weight: int):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.weight = weight

#     def bark(self):
#         return f'{self.name} goes bark!'
    
#     def ispuppy(self):
#         if self.age <= 1:
#             return f'{self.name} is a puppy!'
        
#         else: return f'{self.name} is not puppy.'

#     def size(self):
#         if self.weight <= 30:
#             return f'{self.name} is a small dog.'
        
#         elif self.weight > 30 and self.weight <= 60:
#             return f'{self.name} is a medium dog.'

#         else:
#             return f'{self.name} is a big dog.'
        
# charlie = Dog("Charlie", 1, "Poodle", 30)

class Dog:
    def __init__(self, name: str, age: float, breed: str, weight: int):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight

    def bark(self):
        return f'{self.name} goes bark!'

dog1=Dog.self

dog1("joe")