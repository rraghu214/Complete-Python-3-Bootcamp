def show_card(suite):
    num_values = [str(i) for i in range(2,11)]
    new_values = ['J','Q','K','A']
    card_values = num_values + new_values
    suites = {"spade":"♠","heart":"♥","clubs":"♣","diamond":"♦"}
    sym=suites[suite]
    for i in card_values:
        print('-------')
        print(f'|{sym}    |')
        if i == '10':
            print(f'| {i}  |')
        else:
            print(f'|  {i}  |')
        print(f'|    {sym}|')
        print('-------')
        


show_card("spade")