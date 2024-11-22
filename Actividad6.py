import random

def createmat():
    holdmat = []
    for x in range(4):
        holdnums = []
        for y in range(4):
            holdnums.insert(0, random.randint(1,99))
        holdmat.insert(x, holdnums)
    return holdmat

def maindiasum():
    diasum = 0
    for x in range(len(matrix)):
        diasum += matrix[x][x]
    return diasum

def secodiasum():
    diasum = 0
    for x in range(len(matrix)):
        invx = len(matrix[x]) - (x+1)
        diasum += matrix[x][invx]
    return diasum

matrix = createmat()
print(maindiasum())
print(secodiasum())