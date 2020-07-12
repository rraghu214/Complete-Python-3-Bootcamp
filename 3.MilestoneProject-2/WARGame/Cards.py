
suites = ('hearts', 'spades','diamond','clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Cards:
    '''
    Card class to print the value of the card for a given suit & rank.

    '''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank=rank
        self.value=values[rank]
    
    
    def __str__(self):
        #self.card = card
        return f'{self.rank} of {self.suit}'


if __name__ == '__main__':
    new_card = Cards(suites[0],ranks[0])
    print(new_card)