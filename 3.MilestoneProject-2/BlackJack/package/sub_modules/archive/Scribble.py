tmp = Cards()
tmp.print_card()

tmp1 = Chips()
x=tmp1.new_game_chips()
print(x)

tmp2 = Evaluate()
y = tmp2.initial_eval(21)
print(y)

tmp3 = Scoring()
z = tmp3.get_card_score('J')
print(z)

sleeper()
clear_screen()