import art
import game_data
import random

def computer_choice():
    compA = random.choice(game_data.data)
    print(f"Compare A: {compA['name']}, a {compA['description']}, from {compA['country']}")
    return compA

def user_choice():
    compB = random.choice(game_data.data)
    print(f"Compare B: {compB['name']}, a {compB['description']}, from {compB['country']}")
    return compB


# computer_choice()
stop = False
total = 0
while stop == False:
    print(art.logo)
    a = computer_choice()
    print(art.vs)
    b = user_choice()
    user_guess = input("Who has more followers? Type 'A' or 'B':  ")
    if ((user_guess == "A".lower() and a["follower_count"] > b["follower_count"])
            or (user_guess == "B".lower() and b["follower_count"] > a["follower_count"])):
        print("Correct")
        total += 1

    else:
        print("Incorrect")
        print(f"Sorry, your final score {total}")
        stop = True
