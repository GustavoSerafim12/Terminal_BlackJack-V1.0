from ui import render_aposta, print_error
import time
import os

win_states = {
    "CONTINUE": 0,
    "PLAYER_WIN": 1,
    "DEALER_WIN": 2,
    "TIE": 3
}

def aposta(coins, bet):

    render_aposta(coins)

    input_apostas = input("  How much to bet? > ")
    try:
        bet = int(input_apostas)
    except ValueError:
        bet = 0
    
    # Validate bet: must be positive and not exceed available coins
    if(bet > coins or bet <= 0):
        print_error("Invalid bet amount")
        time.sleep(1)
        os.system('clear')
        bet = 0
        return coins, bet, False
    if(bet < coins*0.1):
        print_error(f"Minimum bet is 10% ({int(coins*0.1)} coins)")
        time.sleep(1)
        os.system('clear')
        bet = 0
        return coins, bet, False
    
    else:
        # Deduct bet from coins
        coins -= bet
        os.system('clear')
        return coins, bet, True
##

def payout(coins, bet, win):
    if(win == win_states["PLAYER_WIN"]):
        coins += 2*bet
    if(win == win_states["DEALER_WIN"]):
        coins = coins
    if(win == win_states["TIE"]):
        coins += bet

    return coins