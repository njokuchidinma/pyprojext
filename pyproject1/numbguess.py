import random

highest_range = input("Type a number: ")

if highest_range.isdigit():
    highest_range = int(highest_range)

    if highest_range <= 0:
        print('Number must be greater than 0, Try again')
        quit()
else:
    print('Type a number next time!')
    quit()

random_num = random.randint(0,highest_range)
guesscount = 0

while True:
    guesscount += 1
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please type a number next time!')
        continue

    if guess == random_num:
        print("Correct!")
        break
    else:
        if guess > random_num:
            print("Oops! Above the number!")
        else:
            print("Oops!, Below the number!")
    
    
print("You got it in", guesscount, "guesses")