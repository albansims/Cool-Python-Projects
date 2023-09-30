import art
import random

play = False
start_game = input("Would you like to play a game of Blackjack? Type 'y' or 'n':\n")
if start_game == "y":
    play = True
    print(art.logo)
else:
    play = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
score = 0
dealer_score = 0
def deal_card(player_or_dealer, no_cards):
    dealt_cards = []
    for i in range(no_cards): 
        card = random.choice(cards)
        dealt_cards.append(card)
    if player_or_dealer == "player":
        return player_cards.extend(dealt_cards)
    if player_or_dealer == "dealer":
        return dealer_cards.extend(dealt_cards)
def calculate_score(player_or_dealer):
    global score
    global dealer_score
    if player_or_dealer == "player":
        score = 0
        for i in player_cards:
            score += i
        if score>21 and 11 in player_cards:
            player_cards[player_cards.index(11)] = 1
            score = 0
            for i in player_cards:
                score += i
    if player_or_dealer == "dealer":
        dealer_score = 0
        for i in dealer_cards:
            dealer_score += i
game_over = False

if play:
    #First hand
    deal_card("player", 2)
    calculate_score("player")
    deal_card("dealer", 2)
    calculate_score("dealer")
    dealer_first_card = dealer_cards[0]
    print(f"Your cards: {player_cards}, current score: {score}\n Dealer's first card: {dealer_first_card}")
    if score >= 21:
        game_over = True
    while not game_over:
        #next hand
        next_hand = input("Type 'y' to get another card, type 'n' to pass: \n")
        if next_hand == "y":
            deal_card("player", 1)
            calculate_score("player")
            if dealer_score < 17:
                deal_card("dealer", 1)
                calculate_score("dealer")
            print(f"Your cards: {player_cards}, current score: {score}\n Dealer's first card: {dealer_first_card}")
            if score >= 21:
                game_over = True
        if next_hand == "n":
            game_over = True
if game_over:
    if score == 21:
        print("You win")
    if score > 21:
        print("You lose")
    if score > dealer_score and score < 21:
        print(f"Your final hand: {player_cards}, final score: {score}\n Dealer's final hand: {dealer_cards}, final score: {dealer_score}\n You win!")
    if score < dealer_score:
        print(f"Your final hand: {player_cards}, final score: {score}\n Dealer's final hand: {dealer_cards}, final score: {dealer_score}\n You lose!")
    if score == dealer_score:
        print(f"Your final hand: {player_cards}, final score: {score}\n Dealer's final hand: {dealer_cards}, final score: {dealer_score}\n It's a draw!")