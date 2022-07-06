import os
import art
import cards
import random

computer_score = 0
user_score = 0

def deal_card():
    game_cards = cards.deck;
    return random.randint(0, len(game_cards) - 1)

def calculate_score(card_list):
    blackjack = 0
    for card in card_list:
        if card == 0 : blackjack += 11
        elif card == 9 or card == 10 or card == 11 : blackjack += 10
        else : blackjack += (card + 1)

    if 11 in card_list and blackjack > 21 : return 12
    elif blackjack == 21 : return 0
    else : return blackjack

def compare(computer, user):
    if computer == user:
        print("It's Draw.")
    elif computer == 0 or user > 21 or (computer > user and computer < 22):
        print("Computer Wins.\nUser Loses.")
    else:
        print("User Wins. Computer Loses")

def play_game():
    user_cards = []
    computer_cards = []
    user_deck = []
    computer_deck = []
    is_game_over = False

    print(art.logo)

    for _ in range(2):
        user_cards.append(deal_card())
        user_deck.append(cards.deck[user_cards[_]])
        computer_cards.append(deal_card())
        computer_deck.append(cards.deck[computer_cards[_]])

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_deck}, Current score: {user_score}")
        print(f"    Computer's first cards: {computer_deck[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            isContinue = input(f"Type 'y' to get another card, type'n'to pass: ")
            if isContinue.lower() == "y": 
                user_cards.append(deal_card())
                user_deck.append(cards.deck[user_cards[len(user_cards) - 1]])
            else : is_game_over = True

    while computer_score != 0 and computer_score < 17 : 
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        computer_deck.append(cards.deck[computer_cards[len(computer_cards) - 1]])

    print(f"    Your final hand: {user_deck}, Final score: {user_score}")
    print(f"    Computer's final hand: {computer_deck}, Final score: {computer_score}")
    compare(computer_score, user_score)

play_game()

while input("Do you want to play a game of Blacjack? Type 'y' or 'n': ").lower() == "y":
    os.system('cls')
    play_game()