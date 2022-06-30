import os
import random
import words
import stage

chosen_word = random.choice(words.word_list)
display = []
isDone = False
life = len(stage.stages) - 1

for letter in chosen_word:
    display.append("_")

print(f"{stage.logo}\nPsst, the solution is {chosen_word}.")

while not isDone:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
        
    if guess not in display:
        life -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"{' '.join(display)}\n{stage.stages[life]}")
        if life == 0 :
            print("You Lose")
            isDone = True
    else:
        print(f"You guessed {guess}, that's in the word.")
        print(f"{' '.join(display)}\n{stage.stages[life]}")
        if "_" not in display:
            isDone = True
            print("You Win")