import random
import sys
import time

print("ROCK, PAPER, SCISSORS")
print("0 Wins, 0 Losses, 0 Ties")
print("You have 10 Chances")
user_chance = 10
user_won = 0 
computer_won = 0
tie = 0

while True:
    computerInput = random.randint(1,3)
    userInput = input("Enter your move : (r)ock (p)aper (s)cissors or (q)uit : ")
    user_chance -= 1
    if user_chance == 0:
        print(f"Player won {user_won}")
        print(f"Computer won {computer_won}")
        print(f"Tie {tie}")
        exit()
    
    else:
        print(f"You have {user_chance} left")

    if userInput == 'r' and computerInput == 1:
        print("Tie!")
        tie += 1
        time.sleep(1)

    elif userInput == 'r' and computerInput == 2:
        print("Player Won!")
        user_won += 1
        time.sleep(1)

    elif userInput == 'r' and computerInput == 3:
        print("Player Won!")
        user_won += 1
        time.sleep(1)

    elif userInput == 'p' and computerInput == 1:
        print("Computer Won!")
        computer_won += 1
        time.sleep(1)

    elif userInput == 'p' and computerInput == 2:
        print("Tie!")
        tie += 1
        time.sleep(1)

    elif userInput == 'p' and computerInput == 3:
        print("Computer Won!")
        computer_won += 1
        time.sleep(1)

    elif userInput == 's' and computerInput == 1:
        print("Computer Won!")
        computer_won += 1
        time.sleep(1)
        
    elif userInput == 's' and computerInput == 2:
        print("Player Won")
        user_won += 1
        time.sleep(1)

    elif userInput == 's' and computerInput == 3:
        print("Tie!")
        tie += 1
        time.sleep(1)

    elif userInput == 'q':
        print("Thanks for Playing!")
        time.sleep(1)
        exit()