a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def listThis(arg):
    for num in a:
        if num <= 5:
            print(num)
        else:
            continue

listThis(a)

print("This is cool!")

