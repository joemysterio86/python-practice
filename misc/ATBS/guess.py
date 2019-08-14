import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")

for guessesTaken in range(1,7):
    print("Take a guess, baby!")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low, sorry!")
    elif guess > secretNumber:
        print("Your guess is too high, darn!")
    else:
        break

if guess == secretNumber:
    print("Wow good guess... It took you " + str(guessesTaken) + " guesses.")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))