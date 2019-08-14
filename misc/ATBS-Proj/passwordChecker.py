import re, stdiomask

pwRegex = re.compile(r'''(
    ^
    (?=.*[A-Z])
    (?=.*[a-z])
    (?=.*[0-9]|.*[!@#$%^&*()=])
    .{8,25}
    $
    )''', re.VERBOSE)

def pwCheck():
    while True:
        m = stdiomask.getpass(prompt="Enter: ", mask="*")
        mo = pwRegex.search(m)
        if (not mo):
            print("Didn't work. Try again!\n")
        else:
            print("It worked, good job!!")
            break

print("Please enter a new password.\n\nMust contain at least 1 upper case, 1 lower case and 1 number OR 1 special character.\n")
pwCheck()



