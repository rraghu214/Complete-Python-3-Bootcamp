from sub_modules.card_activities import *
from sub_modules.Chips import *
from sub_modules.EvaluateResult import *
from sub_modules.Scoring import *
from sub_modules.Utilities import clear_screen,sleeper


def blackjack():
    player_chips = Chips() ##### Defining an Object to contain player's chips
    p_t_chips = player_chips.new_game_chips() ##### Initializing the chips for a new game.


    ##### This while loop is where the game begins for the player. The while loop exits when player is completely out of chips or Player decides to Quit the game.
    while True:
        print('Welcome to Black Jack!.')
        print(f'Available chips: {p_t_chips}')
        available_bets = player_chips.available_bets(p_t_chips) ##### Based on the chips available with the player, this module call provides the choices of bets for the player to place  from. 
        if len(available_bets)==0: ##### Checking if the list of bets available for the player is empty.
            print('Insufficient Chips. Restart the game. Exiting!!')
            break
        
        #####This while loop is to ensure the correct bet is placed from the given choies. Failing which the player will be prompted again. While loop exits when the bet value is available from the given list.
        while True:
            bet_chosen = int(input(f'Place your bet from one of the values: {available_bets} \n')) ##### Place the bet

            #####Evaluate the bet placed.
            if bet_chosen in available_bets:
                p_t_chips = player_chips.chips_after_placing_bet(total_chips=p_t_chips,bet_placed=bet_chosen) ##### Compute the effective chips after placing the bet.
                print(f'Available chips: {p_t_chips}')
                sleeper(3)

            else:
                print('Choose the right value!\n')
                continue
            break
    

        ##### All the initializations.

        # player & dealer
        game = Cards()
        total_cards = game.initialize_cards()
        #print(total_cards)

        player = Cards()
        player_cards = []
        dealer = Cards()
        dealer_cards =[]
        
        player_score=Scoring()
        dealer_score=Scoring()
        game_eval = Evaluate()

        ##### Distribute the cards to the dealer

        print('Dealer-Cards')
        d0 = dealer.random_pick(total_cards) ##### Randomly pick first card for the dealer.
        total_cards = game.get_new_deck(total_cards,d0) ##### Update the deck of 52 cards by removing the above chosen card. Then retrieve.
        dealer_cards.append(d0) ##### Stackin up the dealer's cards.
        d_value,suite = dealer.split_the_pick(d0) ##### A card in the list is a combination of the suite and value. Spliting them.
        dealer.print_card(suite=suite,value=d_value) ##### Reveal dealer's first card

        d_score=[] ##### Start calculating dealer's score.
        d_score.append(dealer_score.get_card_score(d_value)) ##### Maintain a list of every score of the dealer.
        d_t_score = player_score.get_total_score(d_score) ##### Effective dealer score.

        d1 = dealer.random_pick(total_cards) ##### Pick 2nd card.
        total_cards = game.get_new_deck(total_cards,d1)  ##### Effective deck after the pick.
        dealer_cards.append(d1)
        value,suite = dealer.split_the_pick(d1)
        dealer.print_card() ##### Print the card without revealing the value. 
        print(f'Dealer Score: {d_t_score}') ##### Reveal dealer's score without 2nd card.

        
        sleeper(5) ##### Wait for 5 secs

        ##### Similarly distribute the cards to the Player.
        ##### First card

        print('Player-Cards')
        p1 = player.random_pick(total_cards)
        total_cards = game.get_new_deck(total_cards,p1)
        player_cards.append(p1)
        value,suite = player.split_the_pick(p1)
        player.print_card(suite=suite,value=value)

        p_score=[]
        p_score.append(player_score.get_card_score(value))

        ##### Second card
        p1 = player.random_pick(total_cards)
        total_cards = game.get_new_deck(total_cards,p1)
        player_cards.append(p1)
        value,suite = player.split_the_pick(p1)
        player.print_card(suite=suite,value=value)

        p_score.append(player_score.get_card_score(value))
        p_t_score = player_score.get_total_score(p_score)
        print(f'Player Score: {p_t_score}')

        print()
        print("Player's Turn..")

        p_iter = 1
        ##### Player's Turn

        game_result = 'CONTINUE' ##### Initializing game's result

        ##### This section does a preliminary check if the first 2 cards tally's to 21 making a black jack!
        if p_t_score == 21:
            print(f'Player possibly gets a BLACKJACK')
            game_result == 'BLACK JACK'
        
        ##### Not a black jack
        else:
            choice = ' '
            ##### This while loop is to give chance for the player to draw more cards. Player to choose H / S. Other values will continue the loop.
            ##### Loop exits if the game's score crosses 21 or there is no result in the player's HITS. Or the player decide to Stand.
            while p_t_score < 21 or game_result == 'CONTINUE' or choice.upper() == 'S':                            
                p_iter+=1
                choice = str(input('Hit or Stand. h / s ?'))
                print(choice)
                ##### If condition to evalue the input h / s
                if choice.upper() == 'H' or choice.upper() == 'S':   
                    ##### If the player HITS, draw a random card. Reveal the new score and a new intermediate result.                       
                    if choice.upper() == 'H':
                        p1 = player.random_pick(total_cards)
                        #print(p1)
                        total_cards = game.get_new_deck(total_cards,p1)
                        player_cards.append(p1)
                        value,suite = player.split_the_pick(p1)
                        player.print_card(suite=suite,value=value)

                        p_score.append(player_score.get_card_score(value))
                        p_t_score = player_score.get_total_score(p_score)
                        print(f'Player Score: {p_t_score}')

                        game_result = game_eval.player_eval(player_score=p_t_score)
                        print(f'Possible result: {game_result}')
                        continue
                    ##### If the player decides to STAND.
                    else:                      
                        #print('Inner break')
                        break
                else:
                    print('Incorrect choice!')
                    continue


        ##### Dealer's Turn
        ##### Display first and second card
        d_iter = 1
        print("Revealing Dealer's initial cards")
        d_value,suite = dealer.split_the_pick(d0)
        dealer.print_card(suite=suite,value=d_value)
        
        d_value,suite = player.split_the_pick(d1)
        dealer.print_card(suite=suite,value=d_value)
        d_score.append(dealer_score.get_card_score(d_value))
        d_t_score = player_score.get_total_score(d_score)
        

        print(f'Dealer Score: {d_t_score}')

        ##### If the dealer's first 2 cards isnt a black jack, then draw cards for the player.
        ##### Dealer continues to draw cards until he reaches 17 with a conclusive result.

        if game_result == 'CONTINUE' and d_t_score <=17:
            ##### This while loop draw's player cards, computes the score and checks for result until the score is 17.
            #print("While Loop Dealer's Cards..")
            while True:
                d_iter+=1
                print()
                d1 = dealer.random_pick(total_cards)
                #print(f'd1 is {d1}')
                total_cards = game.get_new_deck(total_cards,d1)
                dealer_cards.append(d1)
                #print(f'dealer_cards is {dealer_cards}')
                d_value,suite = player.split_the_pick(d1)
                player.print_card(suite=suite,value=d_value)
                #print(f'd_score before appending {d_score}')

                d_score.append(dealer_score.get_card_score(d_value))
                #print(f'd_score before appending {d_score}')
                d_t_score = player_score.get_total_score(d_score)
                print(f'Dealer Score: {d_t_score}')
                if d_t_score >= 17:
                    break
                else:
                    sleeper(5)
                    continue
                    
        ##### Dealer and Player's turns are over. Evaluate final result.
        game_result = game_eval.full_eval(p_score=p_t_score,d_score=d_t_score,p_iter=p_iter,d_iter=d_iter)
        p_t_chips = player_chips.chips_after_initial_game(total_chips=p_t_chips,bet_placed=bet_chosen,result=game_result)
        print(f'Game Over. Result is {game_result}.\nTotal available chips: {p_t_chips}')

        continue_game = input('New Game Y / N : ')
        if continue_game == 'Y':
            clear_screen()
            continue
        else:
            print('BYE BYE!')
            break

blackjack()