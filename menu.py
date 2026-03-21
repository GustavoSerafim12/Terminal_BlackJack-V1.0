import os
import time 
from cartas import *
from game import *
from ui import render_menu
from rules import *

def menu():
    render_menu()

    input_menu = 0
    input_menu = input("(1):Game  (2):LeaderBoard: (3):Rules (4):Quit  ")
    try:
        input_menu = int(input_menu)
    except ValueError:
         input_menu = 0

    if (input_menu == 1):
        return "game"

    if (input_menu == 2):
        #leaderboard
        os.system('clear')
        return "leaderboard"

    if (input_menu == 3):
        #rules
        os.system('clear')
        return "rules"

    if(input_menu == 4):
        #quit
        return "quit"
    
    else:
        os.system('clear')
        print("invalid input!")
        time.sleep(1)
        return "menu"
##
