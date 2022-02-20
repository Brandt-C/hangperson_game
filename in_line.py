import random



w_list = [
    "balance", "gutter", "theater", "temple", "attract", "architect", "national", "garbage", "throw",
    "eyebrow", "venture", "unaware", "medicine", "outline", "spring", "dragon", "execution", "traction"
    ]

wel = "\t\tWelcome to Hangperson!\nThis should all be pretty self-explanatory but. . . \nAll lowercase."
wel += "\n\tWanna play?  'y' to continue, any other key will exit.\t"
turn = 20
menu = input(wel)
while True:
    if menu == "y":
        word = random.choice(w_list)
        hid_let = []
        sec_let = list(word)
        for l in range(len(sec_let)):
            hid_let.append("_ ")
        print(f'Turns left: {turn}\n{hid_let}')
        while turn > 0:
            #clear_output
            g = input("What letter you wanna try?\t")
            for i in range(len(sec_let)):
                if g == sec_let[i]:
                    hid_let[i] = g
                else:
                    pass
            if "_ " not in hid_let:
                print("You did it!")
                turn = 0
            print(hid_let)
            turn -= 1 
        if "_ " not in hid_let:
            print(f'Well done!\nWINNER!\n You got\t {sec_let}')
            break
        elif "_ " in hid_let:
            print("Better luck next time!")
            print(f"here's the word- {sec_let}")
            break
    else:
         False

    
    
    
    