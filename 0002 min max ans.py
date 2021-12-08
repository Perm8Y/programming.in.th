n = int(input("how many number do you want to input: ", ))
max = 1
min = 1000

for i in range(n):
    num = int(input("number: ", ))
    if num < 1 or num > 1000:
        print("number range must be 1-1000, this number won't be compared with others")
    else:
        if num > max:
            max = num
        elif num < min:
            min = num
    
print("max =", max)
print("min = ", min)