num1 = int(input("1st number = ", ))
num2 = int(input("2st number = ", ))

n = 2000000000
divisor = 0

if n > num1 or n > num2:
    if num1 > num2:
        n = num1
    else:
        n = num2

for i in range(n):
    if num1%(i+1) == 0 and num2%(i+1) == 0:
        divisor = i+1

print(divisor)