# Evan McCabe, Asher Wangia, Connor Pavicic, Gavin Pierce Highscore Tracker


#██████╗  ██████╗ ███╗   ██╗████████╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗
#██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝
#██║  ██║██║   ██║██╔██╗ ██║   ██║       ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  
#██║  ██║██║   ██║██║╚██╗██║   ██║       ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  
#██████╔╝╚██████╔╝██║ ╚████║   ██║       ██████╔╝███████╗███████╗███████╗   ██║   ███████╗
#╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝

import tic_tac_toe

import random

likeToPlay = "yes"                                                                                                                                          

attempt_num = 5

from tic_tac_toe import tic_tac_toe


def num_gussing_game():
    print("welcom to num buessing game terminal.")
    rand_num = random.randint(1, 1000000)
    print("you will have 5 apempts to guess the number it is between 1 and 1,000,000.")

    while attempt_num > 0:
        user_num = input("what is the number that you want? ")

        user_num=int(user_num)
        if user_num == 923194:
            print("""

""")
        elif rand_num > user_num:
            print("""yooooooooooooooooooooooooooooooo, your number is toooooo small.""")
        elif rand_num == user_num:
            print("""you got it right! you realize the odds of the right? is is just as likly as you getting the Ucas Student Handbook number. there is a number inbetween 1 and 1,000,000 that will indeed print the .""")
        elif user_num > rand_num:
            print("so... umm... you number is a little high.")

    #if user_num > rand_num: 

def game():
    while "3":
        game_to_play=input("""what game do you want to play?
1. tic tak toe.
2. number guessing game.
3. Home screen
""")
        
        if game_to_play == "1":
            tic_tac_toe()
        elif game_to_play == "2":
            num_gussing_game()
        elif game_to_play == "3":
            break
        else:
            print("give valid varible")

game()