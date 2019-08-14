tableData = [['apples', 'oranges', 'cherries', 'Banananacabana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(arg):
    colWidth = [0] * len(arg)
    for j in range(len(arg[0])):
        for i in range(len(arg)):
            colWidth[i] = len((max(arg[i], key=len)))
            combined = arg[i][j]
            print(combined.ljust(colWidth[i] + 2," "), end=" ")
        print()


printTable(tableData)


