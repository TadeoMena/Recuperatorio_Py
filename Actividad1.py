def listfiller():
    nums = []
    for n in range(50):
        nums.append(n+1)
    return nums

numlist = listfiller()

lowerlist = numlist[:10]
upperlist = numlist[41:]
evenlist = numlist[1::2]
oddlist = numlist[::2]

print(lowerlist)
print(upperlist)
print(evenlist)
print(oddlist)