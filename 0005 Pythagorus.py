import math

print("c is the longest side of triangle")
print("please input a and b to find c")

a = int(input("a = ", ))
b = int(input("b = ", ))

c = math.sqrt(a**2 + b**2)
print("c =", c)