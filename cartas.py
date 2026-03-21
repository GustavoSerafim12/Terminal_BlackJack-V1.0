import random

valores = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}


naipes = ["♠", "♥", "♦", "♣"]


def value_card(carta):
    return valores[carta[0]]
##

def value_mao(mao):
    # Calculate hand value, counting aces as 11 initially
    value = 0
    aces = 0
    for carta in mao:
        if (carta[0] == "A"):
            aces += 1
        value += value_card(carta)
   
    # Convert aces from 11 to 1 if hand exceeds 21
    while(value > 21 and aces > 0):
        value -= 10
        aces -= 1

    return value
##

def print_mao(mao):
    for carta in mao:
        valor, naipe = carta
        print("(" + valor + naipe + ")", end=" ")
    print("valor:", value_mao(mao))
##
