fiboList = [1]

fiboMax = int(input("How many numbers would you like to generate?\n\n"))

for i in range(1,(fiboMax)):
    if i == 1:
        fiboList.append(i)
    else:
        fiboList.append(fiboList[i-2]+fiboList[(i-1)])
        
print(fiboList)







    