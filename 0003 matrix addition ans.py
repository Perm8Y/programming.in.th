x, y = input("set the values of matirix (x y)").split()
x = int(x)
y = int(y)
print(x, y)

matrix1 = list(range(y))
for i in range(y):
    sub = list(range(int(x)))
    for j in range(x):
        print("please enter the number for (", j+1, (","), i+1, ") of matrix1")
        num = int(input())
        sub[j] =  num
    matrix1[i] = sub

matrix2 = list(range(y))
for i in range(y):
    sub = list(range(int(x)))
    for j in range(x):
        print("please enter the number for (", j+1, (","), i+1, ") of matrix2")
        num = int(input())
        sub[j] =  num
    matrix2[i] = sub

print(matrix1)
print(matrix2)

sumMatrix = list(range(y))
for i in range(y):
    sub = list(range(int(x)))
    sumMatrix[i] = sub

for i in range(y): 
    for j in range(x):
        num = matrix1[i][j] + matrix2[i][j]
        sumMatrix[i][j] = num
    
print(sumMatrix)