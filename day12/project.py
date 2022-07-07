#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art

def guess_number():
    global chance, guess

    guess = int(input("Make a guess: "))
    chance -= 1
    
    if guess < number: print(f"Too low.")
    elif guess > number: print("Too high.")
    
    if chance != 0 and guess != number: print(f"Guess again.\nYou have {chance} attempts remaining to guess the number.")

print(f"{art.logo}Welcom to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 101)
chance = 1
guess = 0

if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy": chance = 10
else: chance = 5

while chance != 0 and guess != number:
    guess_number()

if guess == number: print(f"You got it! The answer was {number}")
else : print("You've run out of guesses, you lose.")