#Shubham Chandra
# Problem 8

# Write a Rock-Papers-Scissors game where a user plays against the computer.

#The program should ask the user to choose an object and then compare to a randomly generated object from the computer. 
#If the objects are the same, then play again. If the objects are different the winner is chosen from the following rules:
#The program should always ask if the player would like to play again. Use the following games as an example:


import random

def RPSgame(choice1, choice2):
    winner = ""
    if choice1 == "rock" and choice2 == "scissors":
        winner = 1
    elif choice1 == "scissors" and choice2 == "paper":
        winner = 1
    elif choice1 == "paper" and choice2 == "rock":
        winner = 1
    elif choice1 == choice2:
        winner = 0
    else:
        winner = 2
    return winner 


play_again = "y"
while play_again == "y":
    player = input("Choose: ")
    if player == "rock" or player == "paper" or player == "scissors":
        computer = random.choice(["paper", "rock", "scissors"])
        winner = RPSgame(player, computer)
        if winner == 1:
            print(f"Computer choose {computer}, you win!")
            play_again = input("Would you like to play again?")
        elif winner == 2:
            print(f"Computer choose {computer}, the computer wins :(")
            play_again = input("Would you like to play again?")   
        else:
            print(f"The computer choose {computer}. Let's settle this:")
    else:
        print("You must choose paper, rock or scissors.")
        play_again = input("Would you like to play again?")
    
   
