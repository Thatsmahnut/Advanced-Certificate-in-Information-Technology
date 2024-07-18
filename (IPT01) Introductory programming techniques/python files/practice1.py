import math

file2 = open("ll.txt", "r")
newData=file2.read()
# print(newData)

list2 = newData.split(" ")
print(list2)

# file3 = open("ll.txt", "w")
# file3.write("it works")

toylist = list2.copy()
print(toylist)

# print(toylist[1:7:2])
# [start:end:step]

# print(len(toylist))
#find length of toylist

x = 5
# print(id(x))
#shows where data of x is stored

li = [3,4,55,6,7,88]
# tt=math.lcm(10,15,20)
# print(tt)

print(math.lcm(10,15,20))
print(math.factorial(10))

x=55
print(hex(100))