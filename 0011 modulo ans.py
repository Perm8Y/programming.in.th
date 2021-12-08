allNum = list(range(10))

for i in range(10):
    num = int(input())
    numMod = num % 42
    allNum[i] = numMod

count = set(allNum)
print(len(count))
