'''
Simple & Scientific calculator to perform basic operations.
'''

from math import sqrt,sin,cos,tan,log,exp



def basic_calculator():
    operations = ['+','-','*','/']
    while True:
        op = input(f'choose the operation {operations} : ')
        if op in operations:
            break
        else:
            print('Choose the correct operation!')
            continue

    ip1 = int(input('First Number: '))
    ip2 = int(input('Second Number: '))
    print('Result: ')

    if op == '+':
        #print('Adding')
        print( ip1 + ip2)
    elif op == '-':
        print(ip1 - ip2)
    elif op == '/':
        print( ip1/ip2)
    else:
        print(ip1 * ip2)
    

def scientific_calculator():
    #operations=['sq','sqrts','cubes','cubert','sine','cos','tan','log','exp']

    operations={'1':'square','2':'sqrt','3':'cube','4':'cubert','5':'sin','6':'cos','7':'tan','8':'log','9':'exp'}
    op = input(f'Choose your operation {operations} --> ')
    #act_op = str(operations[op]) +'_'
    print(operations[op])
    num = float(input('Number: '))    
    if op == '1':
        print(num ** 2)
    elif op == '2':
        print(sqrt(num))
    elif op == '3':
        print(num ** 3)
    elif op == '4':
        print(num ** (1/3))
    elif op == '5':
        print(sin(num))
    elif op == '6':
        print(cos(num))
    elif op == '7':
        print(tan(num))
    elif op == '8':
        print(log(num))
    else:
        print(exp(num))
 

def main():
    
    while  True:
        #print()
        mode = input('Choose your mode - Basic / Scientific? Press B / S : ')
        if mode.upper()=='B' or mode.upper() == 'S':
            if mode == 'B':
                print('Getting into Basic mode')
                basic_calculator()
                cont = input('X for Exit. C for Continue: ')
                
                if cont.upper() == 'X':                                     
                    break
                else:
                    print(f'Else Mode: {mode}')
                    continue
            else:
                print('Getting into Scientific mode')
                scientific_calculator()
                cont = input('X for Exit. C for Continue: ')
                if cont.upper() == 'X':                                     
                    break
                else:
                    print(f'Else Mode: {mode}')
                    continue                

        else:
            print('Choose B / S!')
            continue
    print('Im out')






if __name__ == '__main__':
    main()