from ui import render_aposta
import time
import os

def aposta(coins, bet):

    render_aposta(coins)

    input_buffer = input(" digite quanto quer apostar: ")
    try:
        bet = int(input_buffer)
    except ValueError:
        bet = 0
    
    # Validate bet: must be positive and not exceed available coins
    if(bet > coins or bet <= 0):
        print("valor invaldo!")
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

