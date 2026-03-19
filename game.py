import os
import time 
from cartas import *
import random
from ui import *
from apostas import aposta

win_states = {
    "CONTINUE": 0,
    "PLAYER_WIN": 1,
    "DEALER_WIN": 2,
    "TIE": 3
}

def game():
    os.system('clear')
    #iniciar as variaveis

    coins = 100

    time.sleep(0.5)
    while(1):
        coins = game_loop(coins)
##

def game_loop(coins):

    baralho = [
    (valor, naipe)
    for naipe in naipes
    for valor in valores
    ]
    random.shuffle(baralho)

    player_hand = None
    dealer_hand = None

    bet = 0
    valid_bet = False
    while(valid_bet == False):
        coins, bet, valid_bet = aposta(coins, bet)

    player_hand = [baralho.pop(), baralho.pop()]
    dealer_hand = [baralho.pop()]
    render_game(coins, bet, player_hand, dealer_hand)

    x = 1

    ##player turn
    while(x == 1):
        input_buffer = int(input("(1): HIT (2):STAY    :   "))

        if(input_buffer != 1 and input_buffer != 2):
            print("valor invalido")

        if(input_buffer == 2):
            x = 0
            continue

        if(input_buffer == 1):
            player_hand.append(baralho.pop())
            render_game(coins, bet, player_hand, dealer_hand)
            time.sleep(0.5)
            win = check_win(player_hand, dealer_hand, False)
            if(win == 0):
                continue
            else:
                x = 0
    
    #dealer turn
    dealer_hand.append(baralho.pop())
    render_game(coins, bet, player_hand, dealer_hand)
    win = check_win(player_hand, dealer_hand, False)
    time.sleep(1)

    while(value_mao(dealer_hand) < 17 and win == win_states["CONTINUE"]):
        dealer_hand.append(baralho.pop())
        render_game(coins, bet, player_hand, dealer_hand)
        win = check_win(player_hand, dealer_hand, False)
        time.sleep(1)

    if(value_mao(dealer_hand) >= 17 and win == win_states["CONTINUE"]):
        win = check_win(player_hand, dealer_hand, True)


    if(win == win_states["PLAYER_WIN"]):
        coins += 2*bet
    if(win == win_states["DEALER_WIN"]):
        coins = coins
    if(win == win_states["TIE"]):
        coins += bet
    render_win(win)
    return coins
##

## return 0 continue - 1 player win - 2 dealer win - 3 tie
def check_win(player_hand, dealer_hand, force_win):
    valor_player_hand = value_mao(player_hand)
    valor_dealer_hand = value_mao(dealer_hand)

    if(valor_player_hand > 21):
        return win_states["DEALER_WIN"]

    if(valor_dealer_hand > 21):
        return win_states["PLAYER_WIN"]
    
    if(force_win == False):
        return win_states["CONTINUE"]
    
    else:
        if(valor_player_hand<valor_dealer_hand):
            return win_states["DEALER_WIN"]
        
        if(valor_player_hand>valor_dealer_hand):
            return win_states["PLAYER_WIN"]
        
        if(valor_player_hand==valor_dealer_hand):
            return win_states["TIE"]
##