import os
from cartas import print_mao
import time

win_states = {
    "CONTINUE": 0,
    "PLAYER_WIN": 1,
    "DEALER_WIN": 2,
    "TIE": 3
}

def render_menu():
    os.system('clear')
    print("---------------------------------------------")
    print("                 BlackJack                   ")
    print("---------------------------------------------")
##

def render_game(coins, bet, player_hand, dealer_hand):
    
    os.system('clear')
    print("--------------------------------------")
    print("dealer: ", end=" ")
    print_mao(dealer_hand)
    print("--------------------------------------")
    print("player: ", end=" ")
    print_mao(player_hand)
    print("--------------------------------------")
    print("coins:", coins, "      bet:", bet)

##

def render_aposta(coins):
    os.system('clear')
    print("--------------------------------------")
    print("             APOSTA                   ")
    print("--------------------------------------")
    print("dinheiro:", coins,"      ", end=" ")
##

def render_win(win_state):

    if(win_state == win_states["CONTINUE"]):
        return 0
    if(win_state == win_states["PLAYER_WIN"]):
        os.system('clear')
        print("jogador ganhou!")
    if(win_state == win_states["DEALER_WIN"]):
        os.system('clear')
        print("dealer ganhou")
    if(win_state == win_states["TIE"]):
        os.system('clear')
        print("empachi")

    time.sleep(1)
##