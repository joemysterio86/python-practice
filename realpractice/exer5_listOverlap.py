import random

def listOverlap():
    aI = 0
    bI = 0
    listA = []
    listB = []
    num1 = int(input("Please enter how many numbers you want in list A.\n"))
    num2 = int(input("Please enter how many numbers you want in list B.\n"))
    while aI != num1:
        aI = aI + 1
        listA.append(random.randrange(0, 11))
    while bI != num2:
        bI = bI + 1
        listB.append(random.randrange(0, 11))
    print("Your lists now look like this:\n", listA, "\n", listB, "\n")
    print("The following numbers appear in both lists:")
    print(set(listA) & set(listB))

listOverlap()