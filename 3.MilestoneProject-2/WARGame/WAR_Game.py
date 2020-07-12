from Player import Player
from Deck import Deck

# Initialize Players

p1 = Player('One')
p2 = Player('Two')

# Shuffle new bunch of cards

new_deck = Deck()
new_deck.shuffle()

# Distribute the cards equally to each player

for i in range(26):
    p1.add_new_cards(new_deck.deal_one())
    p2.add_new_cards(new_deck.deal_one())

# Start the game

game_on = True
round_number = 0

while game_on:
    round_number += 1
    print('Round # {}'.format(round_number))

    if len(p1.all_cards) == 0:
        print('No more cards with Player 1. Player 2 wins.')
        game_on = False
        break

    if len(p2.all_cards) == 0:
        print('No more cards with Player 2. Player 1 wins.')
        game_on = False
        break

    p1_playing_cards = []
    p1_playing_cards.append(p1.remove_one())
    #print(p1_playing_cards[0])

    p2_playing_cards = []
    p2_playing_cards.append(p2.remove_one())

    at_war = True

    while at_war:

        if p1_playing_cards[-1].value > p2_playing_cards[-1].value:

            p1.add_new_cards(p2_playing_cards)
            p1.add_new_cards(p1_playing_cards)
            at_war = False

        elif p1_playing_cards[-1].value < p2_playing_cards[-1].value:

            p2.add_new_cards(p1_playing_cards)
            p2.add_new_cards(p2_playing_cards)
            at_war = False

        else:
            print('At War')

            if len(p1.all_cards) < 5:
                print('No more cards to draw for Player 1. Player 2 wins.')
                game_on = False
                break
            
            elif len(p2.all_cards) < 5:
                print('No more cards to draw for Player 2. Player 1 wins.')
                game_on = False
                break
            else:
                for num in range(5):
                    p1_playing_cards.append(p1.remove_one())
                    p2_playing_cards.append(p2.remove_one())