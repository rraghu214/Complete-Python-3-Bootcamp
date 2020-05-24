#import

class Evaluate():

    def __init__(self):
        pass
    def full_eval(self,p_score,d_score,p_iter,d_iter):
        '''
        This is used during the initial evaluation of cards.
        '''
        if p_score == d_score == 21:
            return 'PUSH'
        elif p_score == 21 and d_score !=21 and p_iter == 1:
            return 'PLAYER BLACKJACK'
        elif p_score !=21 and d_score == 21 and d_iter == 1:
            return 'DEALER BLACKJACK'
        elif (p_score <=21 and d_score < p_score and d_score >= 17) or d_score > 21:
            return 'PLAYER WINS'
        elif (d_score <=21 and d_score > p_score and d_score >= 17) or p_score > 21:
        #elif p_score > 21 and d_score > p_score and d_score >= 17:
            return 'PLAYER BUST'
        elif p_score == d_score:
            return 'PUSH'
        else:
            return 'CONTINUE'    
    def dealer_eval(self,dealer_score):
        '''
        Check if the dealer is still eligible to draw the cards until he reaches a score of 17.
        A partial result is returned.
        '''
        if dealer_eval>=17:
            return 'BREAK'
        else:
            return 'CONTINUE'
    def player_eval(self,player_score):
        '''
        Check if the player is still eligible to draw the cards. Player can continue only if the score is less then 21.
        A partial result is returned.
        Score = 21 --> WINS
        Score > 21 --> BUST
        '''
        if player_score > 21:
            return 'BUST'
        elif player_score == 21:
            return 'WINS'
        else:
            return 'CONTINUE'






if __name__ == '__main__':
    player_eval = Evaluate()
    player_score = 19
    #player_res = player_eval.initial_eval(player_score)
    #print(player_res)

    #player_res = player_eval.evaluate_result(is_player=True,player_score=player_score)
    #print(player_res)

    dealer_eval = Evaluate()
    dealer_score = 22

    #dealer_res=dealer_eval.evaluate_result(is_player=False,player_score=player_score,dealer_score=dealer_score)
    #print(dealer_res)