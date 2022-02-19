import random

w_list = [
    "balance", "gutter", "theater", "temple", "attract", "architect", "national", "garbage", "throw",
    "eyebrow", "venture", "unaware", "medicine", "outline", "spring", "dragon", "execution", "traction"
    ]

word = ""
sec_let = list(word)
hid_let = []
guess_list = []


def get_word(x):
    random.choice(x)

def set_word(s_l):
    for l in range(len(s_l)):
        hid_let.append("_ ")
    print(hid_let)

get_word(w_list)
set_word(sec_let)

