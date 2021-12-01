def dayOnePartOne():
    lastNumber = 0
    increasedIndex = 0
    totalNumber = 0
    f = open("date.txt", "r")
    for x in f:
        if (int(x) > int(lastNumber)):
            increasedIndex+=1
        lastNumber = x
        totalNumber+=1

    return increasedIndex - 1

def dayOnePartTwo():
    lastSum = 0
    currentSum = 0
    increasedIndex = 0
    f = open("date.txt", "r")
    lines = f.readlines()

    for i in range(len(lines) - 2):
        currentSum = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        if (int(currentSum) > int(lastSum)):
            increasedIndex+=1
        lastSum = currentSum

    return increasedIndex - 1

def main():
    print(dayOnePartOne())
    print(dayOnePartTwo())

if __name__ == "__main__":
    main()