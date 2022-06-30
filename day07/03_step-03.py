import random
import words

chosen_word = random.choice(words.word_list)
print(f"Psst, the solution is {chosen_word}")
display = []

for letter in chosen_word:
    display.append("_")

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
isDone = False

while not isDone:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    print(display)

    if "_" not in display:
        isDone = True
        print("You Win")
    else:
        isDone = False