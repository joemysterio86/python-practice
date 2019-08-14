import sys
print("Type your name, or type 'exit' to exit:")
name = input()

while True:
    if name == "":
        print("Please enter a name or something!")
        name = input()
    elif name.lower() == "exit":
        print("Thanks for trying. Good bye!")
        sys.exit()
    else:
        break

def printingName(arg):
    for i in arg:
      print("*~*~*~. " + i + " .~*~*~*")

printingName(name)