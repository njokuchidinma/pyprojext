#ROCK PAPER SCISSOR GAME
import random

user_score = 0
comp_score = 0

alternatives = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break
    
    if user_input not in alternatives:
        continue

    random_num = random.randint(0,2)
    #   let rock = 0, paper = 1, scissors = 2
    comp_guess = alternatives[random_num]
    print("Computer's choice", comp_guess + ".")

    if user_input == "rock" and comp_guess == "scissors":
        print("You won!")
        user_score += 1
        
    elif user_input == "scissors" and comp_guess == "paper":
        print("You won!")
        user_score += 1
        
    elif user_input == "paper" and comp_guess == "rock":
        print("You won!")
        user_score += 1
    
    else:
        print("LOSER!")
        comp_score += 1

print("You won", user_score, "times.")
print("Computer won", comp_score, "times")
print("Thank you!")