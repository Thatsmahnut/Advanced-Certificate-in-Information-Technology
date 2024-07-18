import math

# def addition(x, y):

#     answer = x + y
#     print("value is", answer)

# x = eval(input("enter first number: "))
# y = eval(input("enter second number: "))

# addition(x, y)


# def distance (x,y):
#     print("distance travelled", x*y)

# x = int(input("enter speed: "))
# y = int(input("enter time: "))

# distance(x,y)

# def hypo (x,y):

#     a=math.pow(x,2)
#     b=math.pow(y,2)
#     c=math.sqrt(a+b)
#     print("hypotenuse length", c)

# x = int(input("enter a: "))
# y = int(input("enter b: "))

# hypo(x,y)

def num(x,y):
    if x > 0:
        print(x, "it is negative")
    if x >= 2*y:
        print(y, "is greater than or equal to", x)