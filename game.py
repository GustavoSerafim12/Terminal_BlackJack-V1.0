import os
import time 
from cartas import *
import random
from ui import *
from apostas import *

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

    while(1):
        coins = game_loop(coins)
##

def game_loop(coins):

    # Create shuffled deck: all combinations of values and suits
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


    ##player turn
    while True:

        render_game(coins, bet, player_hand, dealer_hand)

        try:
            input_player_turn = int(input("(1): HIT (2):STAY    :  "))
        except ValueError:
            input_player_turn = ""

        if(input_player_turn != 1 and input_player_turn != 2):
            os.system('clear')
            print("valor invalido")
            time.sleep(0.5)
            

        if(input_player_turn == 2):
            break

        if(input_player_turn == 1):
            player_hand.append(baralho.pop())
            render_game(coins, bet, player_hand, dealer_hand)
            time.sleep(0.5)
            win = check_win(player_hand, dealer_hand, False)
            if(win == 0):
                continue
            else:
                break
    
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


    coins = payout(coins, bet, win)
    render_win(win)

    return coins
##

def check_win(player_hand, dealer_hand, force_win):
    # Determine winner: check busts first, then compare hands if force_win is True
    valor_player_hand = value_mao(player_hand)
    valor_dealer_hand = value_mao(dealer_hand)

    # Player busts: dealer wins immediately
    if(valor_player_hand > 21):
        return win_states["DEALER_WIN"]

    # Dealer busts: player wins immediately
    if(valor_dealer_hand > 21):
        return win_states["PLAYER_WIN"]
    
    # If force_win is False, game is still ongoing
    if(force_win == False):
        return win_states["CONTINUE"]
    
    # Compare final hands when both are under 21
    else:
        if(valor_player_hand<valor_dealer_hand):
            return win_states["DEALER_WIN"]
        
        if(valor_player_hand>valor_dealer_hand):
            return win_states["PLAYER_WIN"]
        
        if(valor_player_hand==valor_dealer_hand):
            return win_states["TIE"]
##