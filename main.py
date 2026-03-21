import os
import time 
from cartas import *
from game import *
from ui import render_menu


def menu():
    render_menu()

    input_menu = 0
    input_menu = input("(1):Game                     (2):LeaderBoard:")
    try:
        input_menu = int(input_menu)
    except ValueError:
         input_menu = 0

    if (input_menu == 1):
        game()
    if (input_menu == 2):
        #leaderboard
        os.system('clear')
        print("leaderboard")
    if(input_menu != 1 & input_menu!= 2):
        os.system('clear')
        print("invalid input!")
        time.sleep(1)
        menu()
##

#running_code
menu()


