from Cards import Cards, suites,ranks,values
import random
class Deck:
    def __init__(self):
        self.all_cards = []
        for suite in suites:
            for rank in ranks:
                self.all_cards.append(Cards(suite,rank))
                #print(new_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

if __name__ == '__main__':
    tmp_deck = Deck()
    tmp_deck.shuffle
    var = tmp_deck.deal_one()
    len(tmp_deck.all_cards)
    print(tmp_deck.all_cards[0])
    print(var)
    len(tmp_deck.all_cards)