import random

a = random.sample(range(20), 6)
b = random.sample(range(20), 8)

myList = [i for i in b if i in a]

print(myList)
