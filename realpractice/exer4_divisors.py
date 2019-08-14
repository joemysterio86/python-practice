def diviserFunc():
    numList = []
    num = 0
    divisedNum = int(input("Please enter a number.\n"))
    print(str(divisedNum) + " can be divised evenly with the following numbers:\n\n")
    while num != divisedNum:
        num = num + 1
        if divisedNum % num == 0:
            numList.append(num)
        else:
            continue
    print(numList)

diviserFunc()


