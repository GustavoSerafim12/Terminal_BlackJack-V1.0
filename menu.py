import os
import time
from cartas import *
from game import *
from ui import render_menu, print_error
from rules import *
from rich.console import Console

_console = Console()

def menu():
    render_menu()

    _console.print("  [bold yellow]1[/bold yellow]  Game   [bold yellow]2[/bold yellow]  Leaderboard   [bold yellow]3[/bold yellow]  Rules   [bold yellow]4[/bold yellow]  Quit", end="")
    input_menu = input("  > ")
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
        print_error("Invalid input")
        time.sleep(1)
        return "menu"
##
