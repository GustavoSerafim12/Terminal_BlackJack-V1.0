import os
import time 
from cartas import *
from game import *
from ui import render_menu


def menu():
    render_menu()

    x = 0
    integer = input("(1):Game                     (2):LeaderBoard:")
    try:
        x = int(integer)
    except ValueError:
        x = 0

    if (x == 1):
        game()
    if (x == 2):
        #leaderboard
        os.system('clear')
        print("leaderboard")
    if(x != 1 & x!= 2):
        os.system('clear')
        print("invalid input!")
        time.sleep(1)
        menu()

menu()


