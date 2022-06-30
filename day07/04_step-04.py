import random
import words
import stage

chosen_word = random.choice(words.word_list)
display = []
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
life = len(stage.stages) - 1
print(stage.stages[life])

for letter in chosen_word:
    display.append("_")

isDone = False

while not isDone:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
        
    if guess not in display:
        life -= 1
        print(f"{stage.stages[life]}\n{display}")
        if life == 0 :
            print("You Lose")
            isDone = True
    else:
        print(f"{stage.stages[life]}\n{display}")
        if "_" not in display:
            isDone = True
            print("You Win")