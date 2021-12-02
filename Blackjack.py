# Blackjack Homework W2D5


import random

playing_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

card_suits = ["Clubs", "Diamonds", "Spades", "Hearts"]

suits_values = {"Clubs": "♣️", "Diamonds": "♦️", "Spades": "♠️ ", "Hearts": "♣️"}


class Card:
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value


def print_cards(cards, hidden):
    s = ""
    for card in cards:
        s = s + " {} ".format(card.value)
    if hidden:
        s += "?"
    print(s)
    s = ""
    for card in cards:
        s = s + " {} ".format(card.suit)
    if hidden:
        s += "?"
    print(s)

    print()


def blackjack_game(deck):
    gambler_cards = []
    dealer_cards = []
    gambler_score = 0
    dealer_score = 0

    while len(gambler_cards) < 2:

        gambler_card = random.choice(deck)
        gambler_cards.append(gambler_card)
        deck.remove(gambler_card)
        gambler_score += gambler_card.card_value

        print("Gambler cards ")
        print_cards(gambler_cards, False)
        print("Gambler score = ", gambler_score)

        input("Press enter to
         continue with the game.")

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        dealer_score += dealer_card.card_value

        print("Dealer cards: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("Dealer score = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)
            print("Dealer score = ", dealer_score -
                  dealer_cards[-1].card_value)

        input("Press enter to continue with the game.")

    if gambler_score == 21:
        print("Winner Winner Chicken Dinner Baby. ")
        print("Dolla Dolla Billz Yall!")
        quit()

    print("Dealer cards: ")
    print_cards(dealer_cards[:-1], True)
    print("Dealer score = ", dealer_score - dealer_cards[-1].card_value)

    print("Press enter to continue with the game.")

    print("Gambler cards: ")
    print_cards(gambler_cards, False)
    print("Gambler score = ", gambler_score)

    while gambler_score < 21:
        choice = input("Enter H to Hit or S to Stand : ")

        if len(choice) != 1 or (choice.lower() != 'H' and choice.lower() != 'S'):

            print("You done messed up AAron")

        if choice.upper() == 'H':

            gambler_card = random.choice(deck)
            gambler_cards.append(gambler_card)
            deck.remove(gambler_card)

            gambler_score += gambler_card.card_value

            print("Dealer cards: ")
            print_cards(dealer_cards[:-1], True)
            print("Dealer score = ", dealer_score -
                  dealer_cards[-1].card_value)

            print()

            print("Gambler cards: ")
            print_cards(gambler_cards, False)
            print("Gambler score = ", gambler_score)

        if choice.upper() == 'S':
            break

    print("Gambler cards: ")
    print_cards(gambler_cards, False)
    print("Gambler score = ", gambler_score)

    print()

    print("Dealer cards: ")
    print_cards(dealer_cards, False)
    print("Dealer score = ", dealer_score)

    if gambler_score == 21:
        print("Winner Winner Chicken Dinner Baby.")
        quit()

    if gambler_score > 21:
        print("Loser")
        quit()

    input("Press enter to continue with the game.")

    while dealer_score < 17:

        print("The Dealer hit.")

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        dealer_score += dealer_card.card_value

        print("Gambler cards: ")
        print_cards(gambler_cards, False)
        print("Gambler score = ", gambler_score)

        print()

        print("Dealer cards: ")
        print_cards(dealer_cards, False)
        print("Dealer score = ", dealer_score)

        input("Press enter to continue with the game.")

    if dealer_score > 21:
        print("You win Brah!")
        quit()

    if dealer_score == 21:
        print("You lost to a Blackjack, sucks to suck.")
        quit()

    elif gambler_score > dealer_score:
        print("Winner Winner Chicken Dinner Baby!")

    else:
        print("Crap, I suck")


if __name__ == '__main__':

    deck = []

    for suit in card_suits:

        for card in playing_cards:

            deck.append(Card(suits_values[suit], card, cards_values[card]))

    blackjack_game(deck)
