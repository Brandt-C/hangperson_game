
import random

def guess(sec_let, hid_let, g):
    for i in range(len(sec_let)):
        if g == sec_let[i]:
            hid_let[i] = g
        else:
            pass
    print(hid_let)
    return sec_let, hid_let

def get_word(som_list):
    word = random.choice(som_list)
    return word

def set_word(stri):
    hid_let = []
    sec_let = list(stri)
    for l in range(len(sec_let)):
        hid_let.append("_ ")
    print(hid_let)
    return hid_let, sec_let


def check_turns(hid_let, turn):
    if "_ " not in hid_let:
        print(f'You did it!\n!!WINNER!!\n {hid_let}')
        turn = 0
        return turn
    elif "_ " in hid_let:
        turn -= 1 
        return turn  
    print(f'Turns left: {turn}')