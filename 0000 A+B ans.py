a = input("A = ", )
b = input("B = ", )


try:
    a = int(a)
    b = int(b)

    if a < 0 or a > 10**9 or b < 0 or b > 10**9:
        print("number range must between 0 to 10**9 ")
    else:
        print(int(a) + int(b))
except:
    print("please enter only number")