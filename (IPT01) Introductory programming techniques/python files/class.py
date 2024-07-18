class User:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def Call_user(self, name):
        print("user name is "(self.name))

Student1 = User("firash", "1", "12")

print(Student1.Call_user("firash"))