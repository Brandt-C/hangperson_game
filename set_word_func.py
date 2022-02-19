import random
word = "execution"

w_list = [
    "balance", "gutter", "theater", "temple", "attract", "architect", "national", "garbage", "throw",
    "eyebrow", "venture", "unaware", "medicine", "outline", "spring", "dragon", "execution", "traction"
    ]
#function for setting up word
sec_let = list(word)
hid_let = []
guess_list = []
counter = 7
def set_word(string):
    for l in range(len(sec_let)):
        hid_let.append("_ ")
    print(hid_let)

def get_word(x):
    random.choice(x)


set_word(get_word(w_list))
print(hid_let)
gue = input("What letter you wanna try?")

def guess(g):
    guess_list.append(g)
    for i in range(len(sec_let)):
        if g == sec_let[i]:
            hid_let[i] = g
        else:
            continue
    print(f'\tPrevious guesses:\n{guess_list}')
    print(hid_let)

guess(gue)






#vari as input here
#if "e" in sec_let:
    
