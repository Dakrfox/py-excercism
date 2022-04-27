"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    lista= [number,(number+1), (number+2)]
    return lista

def concatenate_rounds(rounds_1, rounds_2):
    rounds_1+=rounds_2
    return rounds_1


def list_contains_round(rounds, number):
    if (number in rounds):
        return True
    else:
        return False
    


def card_average(hand):
    sum =0
    for item in hand:
        sum+=item
    sum = sum/len(hand)
    return sum


def approx_average_is_average(hand):
    avr = card_average(hand)
    
    sum = (hand[0] + hand[-1])/2

    op = 0.0
    middle = len(hand)//2
    hand.sort()
    if not len(hand) % 2:
        op = (hand[middle - 1] + hand[middle]) / 2 
    op = hand[middle]

    if(avr==sum or avr==op):
        return True
    return False


def average_even_is_average_odd(hand):
    sum=0
    cont=0
    for items in hand:    
        if not items %2==0:
            sum+=items
            cont+=1
    sum = sum/cont
    if (card_average(hand)==sum):
        return True
    return False
    
    
def maybe_double_last(hand):
    if hand[-1]==11:
        hand[-1]=22
        return hand
    return hand