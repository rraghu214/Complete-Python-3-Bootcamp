from os import system
from time import sleep

def clear_screen():
    system('cls')

def sleeper(duration=3):
    sleep(duration)


if __name__ == '__main__':
    print('Before Sleep')
    sleeper()
    print('After Sleep')
    clear_screen()