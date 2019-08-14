rpsRules = ["rock","paper","scissors"]

def gameOutcomes():
    if p1 == p2:
        return "Draw!\n"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 has rock, they win!\n"
    elif p2 == "rock" and p1 == "scissors":
        return "Player 2 has rock, they win!\n"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 has scissors, they win!\n"
    elif p2 == "scissors" and p1 == "paper":
        return "Player 2 has scissors, they win!\n"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 has paper, they win!\n"
    elif p2 == "paper" and p1 == "rock":
        return "Player 2 has paper, they win!\n"

def playerCheck(player):
    text = "Player {}: Please enter rock, paper, or scissors.".format(player)
    playerChoice = str(input(text + "\n")).lower()
    while playerChoice not in rpsRules:
        print("Please select rock, paper, or scissors! Try again!\n")
        playerChoice = str(input(text + "\n")).lower()
    return playerChoice

while True:
    p1 = playerCheck("1")
    p2 = playerCheck("2")
    print("\n" + gameOutcomes())
    print("Would you like to play again? Y/n")
    playAgain = str(input()).lower()
    if playAgain in ["n","no"]: break
    

