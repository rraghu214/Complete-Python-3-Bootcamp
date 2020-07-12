from Deck import Deck
class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_new_cards(self,new_cards):
        if type(new_cards) ==  type([]):
            self.all_cards.extend(new_cards) 
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'  

if __name__ == '__main__':
    p1 = Player('P1')
    print(p1)
    tmp_deck = Deck()
    var = tmp_deck.deal_one()
    p1.add_new_cards(var)
    print(p1)
    var1=p1.remove_one()
    print(var1)
    print(p1)