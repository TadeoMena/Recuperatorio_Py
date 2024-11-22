import random

def createmat():
    holdmat = []
    for x in range(3):
        holdnums = []
        for y in range(3):
            holdnums.insert(0, random.randint(1,99))
        holdmat.insert(x, holdnums)
    return holdmat

def sumrow():
    totalrow = []
    for x in range(len(matrix)):
        res = 0
        for y in range(len(matrix[x])):
            res += matrix[x][y]
        totalrow.insert(x, res)
    return totalrow
def sumcol():
    totalcol = []
    for x in range(len(matrix)):
        res = 0
        for y in range(len(matrix[x])):
            res += matrix[y][x]
        totalcol.insert(x,res)
    return totalcol
def rotate():
    rotatedmat = []
    for x in range(len(matrix)):
        column = []
        for y in range(len(matrix[x])):
            column.insert(y, matrix[y][x])
        rotatedmat.insert(x,column)
    return rotatedmat
matrix = createmat()
print(matrix)
print(sumrow())
print(sumcol())
print(rotate())