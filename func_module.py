
import random

def guess(s_list, h_list, g):
    for i in range(len(s_list)):
        if g == s_list[i]:
            h_list[i] = g
        else:
            continue
      



def get_word(som_list):
    word = random.choice(som_list)
    return word

def set_word(stri):
    hid_let = []
    sec_let = list(stri)
    for l in range(len(sec_let)):
        hid_let.append("_ ")
    return hid_let, sec_let


def check_turns(hid_let, sec_let, turn):
    if "_ " not in hid_let:
        print(f'You did it!\n!!WINNER!!\n {hid_let}')
        turn = 0
        return turn
    elif "_ " in hid_let:
        turn -= 1 
        return turn  
    print(f'Turns left: {turn}')