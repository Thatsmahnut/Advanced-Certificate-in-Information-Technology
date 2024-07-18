# #name = "mr joseph abraham"
# #first = (name[3:9])
# #second = (name[10:])
# #print(second.title())
# # .upper() .lower() .title()
# #full_name = (first + " " + second)
# #print("Mr. " + full_name)
# #integer methods
# #num = float(5.5)
# #print(num.floor())
# fruits = ["apple", "banana", "guava", "carrot", "chilie", "cabbage",]
# fruits.append("beans") #appends a new entry to the end of the list
# #fruits.insert(1, "broccoli") #inserts behind index
# #fruits.sort(reverse=True) just .sort() will default print list in decending order (alphabetically etc)
# #fruits.pop() # pops the last item in the list but can choose which thru index
# #fruits.remove("chilie") # removes exactly what is written in the statement argument, is case sensitive
# fruits[4:6]=['cat', 'dog']
# print(fruits)
# print("hamster" in fruits) #used to find a specific item in the list
# #print(fruits)
# #vegetable = fruits[3:]
# #print(vegetable)

guess = int(input("what is your guess? "))
target = 50

if guess == target:
    print("you got it!")
else:
    print("wrong!")