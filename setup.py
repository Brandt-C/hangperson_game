import random
from func_module import *


w_list = [
    "balance", "gutter", "theater", "temple", "attract", "architect", "national", "garbage", "throw",
    "eyebrow", "venture", "unaware", "medicine", "outline", "spring", "dragon", "execution", "traction"
    ]

wel = "\t\tWelcome to Hangperson!\nThis should all be pretty self-explanatory but. . . \nAll lowercase."
wel += "\n\tWanna play?  'y' to continue, any other key will exit.\t"
turn = 7
menu = input(wel)
while True:
    
    if menu == "y":
        #clearO
        while turn > 0:
            gue = input("What letter you wanna try?\t")
            guess(set_word(get_word(w_list)))
    