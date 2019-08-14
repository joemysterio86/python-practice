theList = [2, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newList = [a for a in theList if a % 2 == 0]
print(newList)

def listComp(arg):
    newList = []
    for x in range(len(arg)):
        if arg[x] % 2 == 0:
            newList.append(arg[x])
        else:
            continue
    print(newList)

