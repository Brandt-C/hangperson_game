import random
#from IPython.display import clear_output


w_list = [
    "balance", "gutter", "theater", "temple", "attract", "architect", "national", "garbage", "throw",
    "eyebrow", "venture", "unaware", "medicine", "outline", "spring", "dragon", "execution", "traction"
    ]

wel = "\t\tWelcome to Hangperson!\nThis should all be pretty self-explanatory but. . . \nAll lowercase."
wel += "\n\tWanna play?  'y' to continue, any other key will exit.\t"
turn = 20
menu = input(wel)
guess_list = []

while True:
    if menu == "y":
        word = random.choice(w_list)
        hid_let = []
        sec_let = list(word)
        for l in range(len(sec_let)):
            hid_let.append("_ ")
        
        while turn > 0:
            g = input("What letter you wanna try?\t")
            for i in range(len(sec_let)):
                guess_list.append(g)
                if g == sec_let[i]:
                    hid_let[i] = g
                else:
                    pass
            if "_ " not in hid_let:
                #clear_output()
                print("You did it!")
                turn = 0
            #clear_output()
            print(hid_let)
            print(f'Previous guesses: \t{guess_list}')
            print(f'Turns left: {turn}\n{hid_let}')
            turn -= 1 
        if "_ " not in hid_let:
            #clear_output()
            print(f'Well done!\nWINNER!\n You got\t {sec_let}')
            break
        elif "_ " in hid_let:
            #clear_output()
            print("Better luck next time!")
            print(f"here's the word- {sec_let}")
            break
    else:
         False

    
    
    
    