class Scoring():

    def __init__(self):
        pass

    def get_total_score(self,values):
        '''
        Returns the value of cards.
        Evaluates the presence of card 'A' and returns a suitable value
        '''
        
        if 'A' in values:
            
            factor = values.count('A')
            
            if sum(i for i in values if i != 'A') + 11 + ((factor-1) * 1) <=21:
                
                return sum(i for i in values if i != 'A') + 11 + ((factor-1) * 1)
                
            else:
                return sum(i for i in values if i != 'A') + (factor * 1)
                
            
        else:
            return sum(values)

    def get_card_score(self,value):
        '''
        Dictionary of card values.
        '''
        
        scores_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':'A'}
        
        return scores_dict[value]

if __name__ == '__main__':
    #cards = ['2','4','3','A']
    values = [2,4,3,'A','A','A','A']
    a = Scoring()
    b = a.get_total_score(values)
    print(b)
