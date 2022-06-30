import random
import words

chosen_word = random.choice(words.word_list)

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display.append("_")

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
print(f"Psst, the solution is {chosen_word}")

guess = input("Guess a letter: ").lower()
for position in range(len(chosen_word)):
    if(chosen_word[position] == guess):
        display[position] = guess
print(display)