import random
options = ("rock", "paper", "scissors")
running = True
while running:
    player = None
    Computer = random.choice(options)
    while player not in options:
        player = input("Enter (rock, paper, scissors) : ")
    print(f"player : {player}")
    print(f"Computer : {Computer}")
    if player == Computer:
        print("Its a tie")
    elif player == "rock" and Computer == "scissors":
        print("You win!")
    elif player == "paper" and Computer == "rock":
        print("You win!")
    elif player == "scissors" and Computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    if not input("Want to continue (y/n) : ").lower() == "y":
        running = False
print("Thanks for playing!")
