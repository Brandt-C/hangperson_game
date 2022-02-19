def guess(g):
    guess_list.append(g)
    for i in range(len(sec_let)):
        if g == sec_let[i]:
            hid_let[i] = g
        else:
            continue
    print(f'\tPrevious guesses:\n{guess_list}')
    print(hid_let)



def get_word(x):
    random.choice(x)



def set_word(s_l):
    for l in range(len(s_l)):
        hid_let.append("_ ")
    print(hid_let)


def counter(turns):
    turns -= 1