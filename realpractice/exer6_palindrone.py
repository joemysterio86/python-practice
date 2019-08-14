def palindrome():
    string = input("Please enter a word to see if it is a palindrome:\n")
    reverseString = ""
    num = 0
    while num != -(len(string)):
        num -= 1
        reverseString = reverseString + string[num]
    if string.lower() == reverseString.lower():
        print(string + " IS a palindrome: " + reverseString, "\n")
    else:
        print(string + " is not a palindrome: " + reverseString, "\n")

palindrome()

def otherPalin():
    inp = input("Give me a random word\n")
    if inp.lower() == inp[::-1].lower():
        print("{} is a palindrome!".format(inp))
    else:
        print("{} is not a palindrome!".format(inp))

