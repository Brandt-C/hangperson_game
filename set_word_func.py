import random
from func_module import *

word = "fallacy"

w_list = [
    "balance", "gutter", "theater", "temple", "attract", "architect", "national", "garbage", "throw",
    "eyebrow", "venture", "unaware", "medicine", "outline", "spring", "dragon", "execution", "traction"
    ]
#function for setting up word

turn = 7


set_word(get_word(w_list))

gue = input("What letter you wanna try?")

guess(gue)



