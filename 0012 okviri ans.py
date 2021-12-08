text1 = input("enter your text: ", )

f1 = ""
f2 = ""
f3 = ""

for i in range(len(text1)):
    if (i+1) % 3 == 0:
        frame1 = "..*.."
        frame2 = ".*.*."
        frame3 = "*." + text1[i] + ".*"
    else:
        frame1 = "..#.."
        frame2 = ".#.#."
        frame3 = "#." + text1[i] + ".#"

    f1 = f1 + frame1
    f2 = f2 + frame2
    f3 = f3 + frame3

print(f1)
print(f2)
print(f3)
print(f2)
print(f1)