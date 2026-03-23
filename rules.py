from menu import menu
from ui import render_regras, print_error
from rich.console import Console
import os

_console = Console()

def rules():
    render_regras()
    _console.print("  [bold yellow]1[/bold yellow]  Back to menu", end="")
    input_rules = input("  > ")
    try:
        input_rules = int(input_rules)
    except ValueError:
        input_rules = 0

    if(input_rules == 1):
        return "menu"
    else:
        print_error("Invalid input")
        os.system('clear')
        return "rules"