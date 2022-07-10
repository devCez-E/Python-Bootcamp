from inspect import iscoroutinefunction
import os
import art
import game_data
import random

score = 0;
compareData = -1;
againstData = -1;
choice = ""
isContinue = True

def question():
    global compareData
    global againstData
    global choice

    if compareData == -1:
        compareData = random.randrange(0, len(game_data.data)-1)
    
    againstData = random.randrange(0, len(game_data.data)-1)
    
    while(againstData == compareData):
        againstData = random.randrange(0, len(game_data.data)-1)
    
    print(f"Campare A : {game_data.data[compareData]['name']}, {game_data.data[compareData]['description']}, {game_data.data[compareData]['country']}")
    print(art.vs)
    print(f"Against B : {game_data.data[againstData]['name']}, {game_data.data[againstData]['description']}, {game_data.data[againstData]['country']}")
    choice = input("Who has more followers? Type 'A' or 'B' : ").upper()


def compareResult(select):
    global score
    global isContinue
    global compareData
    
    os.system('cls')
    print(art.logo)

    if choice == "A" and game_data.data[compareData]['follower_count'] > game_data.data[againstData]['follower_count']:
        score += 1
        print(f"You're right! Current score : {score}.")
    elif choice == "B" and game_data.data[compareData]['follower_count'] < game_data.data[againstData]['follower_count']:
        score += 1
        compareData = againstData
        print(f"You're right! Current score : {score}.")
    else:
        score = 0
        print(f"Sorry, that's wrong. Final score : {score}")
        isContinue = False


print(art.logo)

while(isContinue):
    question()
    compareResult(choice)