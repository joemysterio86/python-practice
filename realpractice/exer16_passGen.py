import random
import string

allChars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def gen():
    newPass = ""
    num = int(input("Please enter how long you want your password to be: (minimum 12 characters)\n\n"))
    while num < 12:
        num = int(input("You entered a number less than 12. Please enter how long you want your password to be: (minimum 12 characters)\n\n"))
    else:
        while len(newPass) < num:
            newPass += allChars[random.randrange(0,len(allChars))]
        print("\nYour new password is: " + newPass)


gen()

