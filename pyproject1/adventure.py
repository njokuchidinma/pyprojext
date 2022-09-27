name = input("Type your name: ")
print("Welcome", name, "to today's adventure!")

answer = input("You are at a deadend and can only go left or right. which do you prefer? ").lower()


if answer == "left":
    answer = input("You've arrived at a river, you can walk around it or swim across it. which do you prefer? ").lower()

    if answer == "swim":
        print("You tried swimming across, but drowned. why swim when you can't? ")
    elif answer == "walk":
        print("You walked for miles,ran out of water and died! YOU LOSE! ")
    else:
        print("Not valid, You lose")

elif answer == "right":
    print("You're at an old bridge, wanna cross or head back? (cross/back) ")

    if answer == "cross":
        print("You cross the bridge and meet a stranger, do you talk to them? (y/n) ")

        if answer == "y":
            print("You talk to the stranger, You win!")
        elif answer == "n":
            print("You ignore the stranger and get eaten by a wild beast!")
        else:
            print("Not a valid option!")
    elif answer == "back":
        print("You return to the deadend ")
    else:
        print("Not a valid option!")
else:
    print("Not valid, You lose!")