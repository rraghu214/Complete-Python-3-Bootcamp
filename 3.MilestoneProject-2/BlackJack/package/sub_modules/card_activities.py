import random

class Cards():
    def __init__(self):
        pass

    def initialize_cards(self):
        '''
        Initialize 52 cards
        '''
        val_spade = ['2-spade','3-spade','4-spade','5-spade','6-spade','7-spade','8-spade','9-spade','10-spade','J-spade','Q-spade','K-spade','A-spade']
        val_heart = ['2-heart','3-heart','4-heart','5-heart','6-heart','7-heart','8-heart','9-heart','10-heart','J-heart','Q-heart','K-heart','A-heart']
        val_diamond = ['2-diamond','3-diamond','4-diamond','5-diamond','6-diamond','7-diamond','8-diamond','9-diamond','10-diamond','J-diamond','Q-diamond','K-diamond','A-diamond']
        val_clubs = ['2-clubs','3-clubs','4-clubs','5-clubs','6-clubs','7-clubs','8-clubs','9-clubs','10-clubs','J-clubs','Q-clubs','K-clubs','A-clubs']
        
        all_cards = val_spade + val_heart + val_clubs + val_diamond
        return all_cards

    def random_pick(self,current_deck):
        '''
        Randomly return a card
        '''
        return random.choice(current_deck)


    def get_new_deck(self,current_deck,removed):
        '''
        new_deck = current_deck - removed-card
        '''
        new_deck=current_deck
        new_deck.remove(removed)
        return new_deck

    def print_card(self,suite='',value=' '):
        '''
        Print the card
        '''

        suites = {"spade":"♠","heart":"♥","clubs":"♣","diamond":"♦",'':'?'}
        #print(f'Suite is {suite}')
        #print(f'Value is {value}')
        sym=suites[suite]
        
        print('-------')
        print(f'|{sym}    |')
        if value == '10':
            print(f'| {value}  |')
        else:
            print(f'|  {value}  |')
          
        print(f'|    {sym}|')
        print('-------')
    
    def split_the_pick(self,value):
        '''
        Split the value to suite and card value
        '''
        return value.split('-')


if __name__ == "__main__":
    new_game = Cards()
    x=new_game.initialize_cards()
    #print(x)
    y=new_game.random_pick(x)
    #print()
    #print(y)
    z=new_game.get_new_deck(x,y)
    #print(z)

    split_val_lst=new_game.split_the_pick(y)
    value=split_val_lst[0]
    suite=split_val_lst[1]

    new_game.print_card(suite,value)

    new_game.print_card()