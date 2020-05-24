class Chips():

    def __init__(self):
        pass

    def new_game_chips(self):
        '''
        Chips given while starting a game
        '''
        return 500

    def available_bets(self,chips=500):
        '''
        Bets available for the player to choose from.
        '''
        lst = [20,50,100,250,500,750,1000,1250,1500,1750,2000,2500,3000,4000,5000,7500,10000]
        bets = [i for i in lst if i <=chips]
        return bets

    def chips_after_placing_bet(self,total_chips,bet_placed):
        '''
        Chips remaining after placing a bet, before the result
        '''
        return total_chips-bet_placed

    def chips_after_initial_game(self,total_chips,bet_placed,result):
        '''
        Computes the chip count after initial game based on the result.
        '''
        if result == 'PLAYER BLACKJACK':
            return int(total_chips + (bet_placed * 2.5))
        elif result == 'DEALER BLACKJACK':
            return int(total_chips - (bet_placed * 1.5))
        elif result == 'PLAYER WINS':
            return int(total_chips + (bet_placed * 2))
        elif result == 'PLAYER BUST':
            return int(total_chips)
        else:
            #'PUSH'
            return int(total_chips + bet_placed)

    def chips_after_game(self,total_chips,bet_placed,player_result):

        '''
        Computes the chip count after final game based on the result.
        '''        

        if player_result == 'PLAYER WINS':
            return int(total_chips + (bet_placed * 2))
        if player_result == 'PLAYER BUST':
            return int(total_chips)
        else:
            #PUSH
            return int(total_chips + bet_placed)



if __name__ == '__main__':
    player1_chips = Chips()
    bets_chosen = player1_chips.available_bets(480)
    print(bets_chosen)