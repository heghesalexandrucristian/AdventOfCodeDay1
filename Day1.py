"""
lastNumber = 0
increasedIndex = 0
totalNumber = 0
f = open("date.txt", "r")
for x in f:
    if (int(x) > int(lastNumber)):
        increasedIndex+=1
    lastNumber = x
    totalNumber+=1
print(totalNumber)
print(increasedIndex-1)
"""
######### Part II ################
lastSum = 0
currentSum = 0
increasedIndex = 0
totalNumber = 0
f = open("date.txt", "r")
lines = f.readlines()

i = 0
for i in range(len(lines)-2):
    currentSum = int(lines[i])+int(lines[i+1])+int(lines[i+2])
    if (int(currentSum) > int(lastSum)):
        increasedIndex+=1
    lastSum = currentSum
    i = i+3

print(totalNumber)
print(increasedIndex-1)
