allDwarves = list(range(9))
sum = 0

for i in range(9):
    hat = int(input("enter dwarve's hat number: ", ))
    allDwarves[i] = hat
    sum = sum + hat
    #sum must be over 100

sumNotDwarves = sum - 100

for i in range(9):
    for j in range(9-i):
        if allDwarves[i] + allDwarves[j] == sumNotDwarves:
            allDwarves = allDwarves.remove(allDwarves[i])
            allDwarves = allDwarves.remove(allDwarves[j])

print(allDwarves)