print("Enter a number:")
while True:
    try:
        number = int(input())
    except ValueError:
        print("Please enter a valid INTEGER.")
    else:
        break

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

while number != 1:
    number = collatz(number)