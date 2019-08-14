spam = ["dragon fruit","blueberries","cranberries","apples"]
banana = ["gooseberry","appleberry","bannaberry","guacaberry"]
cheese = ["havarti","cheddar","provolone","swisssy swiss"]

def iterAList(arg):
    newString = ''
    arg.sort()
    arg[0] = str.capitalize(arg[0])
    for i in arg:
        newString = newString + str(i)
        if arg.index(i) == len(arg)-2:
            newString = newString + ' and '
        elif arg.index(i) == len(arg)-1:
            newString = newString + '.'
        else:
            newString = newString + ', '
    print(newString)
    return newString


iterAList(spam)
iterAList(banana)
iterAList(cheese)