print("ARE YOU SMART?")

playing = input("Wanna play? ")

if playing.lower() != "yes": 
    quit()

print("Let's play then!")
Scorecount = 0

answer = input("What year did Queen ELizabeth II die? ")
if answer.lower() == "2022":
    print("Correct! Nice Work!")
    Scorecount +=1
else:
    print("Incorrect! :( ")

answer = input("Which language has the more native speakers: English or Spanish? ")
if answer.lower() == "spanish":
    print("Correct! Nice Work!")
    Scorecount +=1
else:
    print("Incorrect! :( ")

answer = input("How many minutes are in a full week? ")
if answer.lower() == "10080":
    print("Correct! Nice Work!")
    Scorecount +=1
else:
    print("Incorrect! :( ")

answer = input("What country has won the most World Cups? ")
if answer.lower() == "brazil":
    print("Correct! Nice Work!")
    Scorecount +=1
else:
    print("Incorrect! :( ")


answer = input("What Netflix show had the most streaming views in 2021? ")
if answer.lower() == "squid game":
    print("Correct! Nice Work!")
    Scorecount +=1
else:
    print("Incorrect! :( ")

answer = input("Kratos is the main character of what video game series? ")
if answer.lower() == "god of war":
    print("Correct! Nice Work!")
    Scorecount +=1
else:
    print("Incorrect! :( ")

answer = input("What is a group of pandas known as? ")
if answer.lower() == "an embarrassment":
    print("Correct! Nice Work!")
    Scorecount +=1
else:
    print("Incorrect! :( ")

answer = input("How many bones do we have in an ear? ")
if answer.lower() == "3":
    print("Correct! Nice Work!")
    Scorecount +=1
else:
    print("Incorrect! :( ")

print("You got " + str(Scorecount) + "questions correct! /n Congratulations! ")
print("You got " + str((Scorecount/8) * 100) + "% ! Great Job!!")