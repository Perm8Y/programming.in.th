hw = input("homework score: ", )
mid = input("midterm exam score: ", )
final= input("final exam score: ", )

try:
    hw = int(hw)
    mid = int(mid)
    final = int(final)

    if hw < 0 or hw > 30 or mid < 0 or mid > 30:
        print("homework and midterm exam score must be 0-30 pt")
    elif final < 0 or final > 40:
        print("final exam score must be 0-40 pt")
    else:
        sum = hw + mid + final
        if sum >= 80:
            print("A")
        elif sum >= 75 and sum < 80:
            print("B+")
        elif sum >= 70 and sum < 75:
            print("B")
        elif sum >= 65 and sum < 70:
            print("C+")
        elif sum >= 60 and sum < 65:
            print("C")
        elif sum >= 55 and sum < 60:
            print("D+")
        elif sum >= 50 and sum < 55:
            print("D")
        else:
            print("F")


except:
    print("please input number only")