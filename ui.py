import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from cartas import value_mao

console = Console()

win_states = {
    "CONTINUE": 0,
    "PLAYER_WIN": 1,
    "DEALER_WIN": 2,
    "TIE": 3
}

def _suit_color(naipe):
    return "red" if naipe in ["\u2665", "\u2666"] else "bright_white"

def _card_lines(valor, naipe):
    c = _suit_color(naipe)
    tv = f"{valor:<2}"
    bv = f"{valor:>2}"
    return [
        f"[{c}]\u250c\u2500\u2500\u2500\u2500\u2500\u2510[/]",
        f"[{c}]\u2502{tv}   \u2502[/]",
        f"[{c}]\u2502  {naipe}  \u2502[/]",
        f"[{c}]\u2502   {bv}\u2502[/]",
        f"[{c}]\u2514\u2500\u2500\u2500\u2500\u2500\u2518[/]",
    ]

def _hand_markup(mao):
    cards = [_card_lines(v, n) for v, n in mao]
    return "\n".join("  ".join(card[i] for card in cards) for i in range(5))

def print_error(msg):
    console.print(f"[bold red]  {msg}[/bold red]")

def render_menu():
    os.system('clear')
    console.print(Panel(
        Align.center(
            "[bold red]\u2660 \u2665[/bold red]  [bold bright_white]B L A C K J A C K[/bold bright_white]  [bold red]\u2666 \u2663[/bold red]\n\n"
            "  [bold yellow]1[/bold yellow]  Play Game\n"
            "  [bold yellow]2[/bold yellow]  Leaderboard\n"
            "  [bold yellow]3[/bold yellow]  Rules\n"
            "  [bold yellow]4[/bold yellow]  Quit\n"
        ),
        border_style="bright_yellow",
        padding=(1, 6),
        width=50
    ))

def render_game(coins, bet, player_hand, dealer_hand):
    os.system('clear')
    dealer_val = value_mao(dealer_hand)
    player_val = value_mao(player_hand)

    console.print(Panel(
        f"[dim]Value:[/dim] [bold yellow]{dealer_val}[/bold yellow]\n\n" + _hand_markup(dealer_hand),
        title="[bold cyan]  DEALER  [/bold cyan]",
        border_style="cyan",
        padding=(0, 2)
    ))
    console.print(Panel(
        f"[dim]Value:[/dim] [bold yellow]{player_val}[/bold yellow]\n\n" + _hand_markup(player_hand),
        title="[bold green]  PLAYER  [/bold green]",
        border_style="green",
        padding=(0, 2)
    ))
    console.print(Panel(
        f"[dim]Coins:[/dim] [bold green]{coins}[/bold green]      [dim]Bet:[/dim] [bold yellow]{bet}[/bold yellow]",
        border_style="bright_black",
        padding=(0, 2)
    ))

def render_aposta(coins):
    os.system('clear')
    min_bet = int(coins * 0.1)
    console.print(Panel(
        f"[dim]Your coins:[/dim] [bold green]{coins}[/bold green]\n\n"
        f"  [dim]Min bet:[/dim] [yellow]{min_bet}[/yellow]   "
        f"[dim]Max bet:[/dim] [yellow]{coins}[/yellow]\n",
        title="[bold yellow]  PLACE YOUR BET  [/bold yellow]",
        border_style="yellow",
        padding=(1, 4)
    ))

def render_win(win_state):
    if win_state == win_states["CONTINUE"]:
        return 0
    os.system('clear')
    if win_state == win_states["PLAYER_WIN"]:
        console.print(Panel(
            Align.center("[bold bright_green]  YOU WIN!  [/bold bright_green]"),
            border_style="bright_green",
            padding=(1, 4)
        ))
    elif win_state == win_states["DEALER_WIN"]:
        console.print(Panel(
            Align.center("[bold bright_red]  DEALER WINS  [/bold bright_red]"),
            border_style="bright_red",
            padding=(1, 4)
        ))
    elif win_state == win_states["TIE"]:
        console.print(Panel(
            Align.center("[bold bright_yellow]  IT'S A TIE  [/bold bright_yellow]"),
            border_style="bright_yellow",
            padding=(1, 4)
        ))
    time.sleep(1.5)

def render_regras():
    console.print(Panel(
        "[bold yellow]GOAL[/bold yellow]\n"
        "Get as close to 21 without going over and beat the dealer.\n\n"
        "[bold yellow]BETTING[/bold yellow]\n"
        "Minimum bet is [yellow]10%[/yellow] of your total coins.\n"
        "[green]Win[/green] = double the bet  |  [red]Loss[/red] = lose bet  |  [yellow]Tie[/yellow] = bet returned\n\n"
        "[bold yellow]CARD VALUES[/bold yellow]\n"
        "  2-10  face value     J, Q, K  10     A  11 or 1\n\n"
        "[bold yellow]YOUR TURN[/bold yellow]\n"
        "  [bold yellow]1[/bold yellow]  Hit   - take another card\n"
        "  [bold yellow]2[/bold yellow]  Stand - stop and let the dealer play\n\n"
        "[bold yellow]DEALER TURN[/bold yellow]\n"
        "Dealer must hit until reaching 17 or higher.\n\n"
        "[bold yellow]WINNING[/bold yellow]\n"
        "  Dealer busts          [green]you win[/green]\n"
        "  Your total > dealer   [green]you win[/green]\n"
        "  Your total < dealer   [red]you lose[/red]\n"
        "  Equal totals          [yellow]draw[/yellow]\n",
        title="[bold yellow]  BLACKJACK RULES  [/bold yellow]",
        border_style="yellow",
        padding=(1, 3)
    ))
