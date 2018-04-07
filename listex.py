#1
numbers = [18,432,3431,6,64,34,76,85,666,345,238,22,45]
sum = 0
for num in numbers:
    sum += num
print(sum)

#2
numbers = [55,88,345,6452,434,863,25,5625]
print(max(numbers))

#3
numbers = [27,643,2345,73,784,374,7734,66,92,8]
print(min(numbers))

#4
numbers = [55,32,743,342,7906,23,8,486,2464,33,359]
for num in numbers:
    if num % 2 == 0:
        print(num)

#5
numbers = [98,3,-44,783,-5860,-103,-9,679,295]
for num in numbers:
    if num > 0:
        print(num)

#6
numbers = [-42,-888,34,379,-312,63,5634,-793]
poslist = [num for num in numbers if num > 0]
print(poslist)

#7
numbers = [33,53,74,11,895,364,9433]
multiple = 2
multilist = [num * multiple for num in numbers]
print(multilist)

#8
list1 = [88,42,219,19,55]
list2 = [66,32,85,2,183]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] * list2[i])
print(list3)

#9
matrix1 = [[12, 4], [5, 9]]
matrix2 = [[16, 2], [25,4]]
resultMatrix = []
for i in range(len(matrix1)):
    matrixadd = []
    for j in range(len(matrix1[i])):
        addnumber = matrix1[i][j] + matrix2[i][j]
        matrixadd.append(addnumber)
    resultMatrix.append(matrixadd)
print(resultMatrix)

#10
matrix1 = [[5,3], [8,2], [12,50,25,3], [6]]
matrix2 = [[17,1], [9,3], [21,4,14,35], [7]]
resultMatrix = []
for i in range(len(matrix1)):
    matrixadd = []
    for j in range(len(matrix1[i])):
        addnumber = matrix1[i][j] + matrix2[i][j]
        matrixadd.append(addnumber)
    resultMatrix.append(matrixadd)
print(resultMatrix)

#11
strings = ["I", "am", "Duh", "Kay", "Extreme", "am", "the", "best", "Duh", "!"]
newstrings = []
for string in strings:
    if string not in newstrings:
        newstrings.append(string)
print(newstrings)
