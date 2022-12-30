import random

Var = ["Rock", "Paper", "Scissors"]
enemy = random.choice(Var)

while True:
    print("Hello! Welcome to game - Rock Paper Scissors!")
    print("Write 1 of 3 things (Rock Paper Scissors)")
    player = input()
 
    while player not in Var:
        print("Write 1 of 3 things (Rock Paper Scissors) again!")
        player = input()

    if enemy == "Rock" and player == "Scissors":
        print("You lose!")
        print("Enemy was:" + enemy)
    elif enemy == "Rock" and player == "Paper":
        print("You win!")
        print("Enemy was:" + enemy)
    elif enemy == "Paper" and player == "Scissors":
        print("You win!")
        print("Enemy was:" + enemy)
    elif enemy == "Paper" and player == "Rock":
        print("You lose!")
        print("Enemy was:" + enemy)
    elif enemy == "Scissors" and player == "Rock":
        print("You win!")
        print("Enemy was:" + enemy)
    elif enemy == "Scissors" and player == "Paper":
        print("You win!")
        print("Enemy was:" + enemy)
    elif enemy == player:
        print("Tie!")

    print("Do you want to play again? Y/N")
    choice = input()
    if choice == "N":
        break

print("Bye!")







