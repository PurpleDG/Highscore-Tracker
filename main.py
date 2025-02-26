# Evan McCabe, Asher Wangia, Connor Pavicic, Gavin Pierce Highscore Tracker


#██████╗  ██████╗ ███╗   ██╗████████╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗
#██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝
#██║  ██║██║   ██║██╔██╗ ██║   ██║       ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  
#██║  ██║██║   ██║██║╚██╗██║   ██║       ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  
#██████╔╝╚██████╔╝██║ ╚████║   ██║       ██████╔╝███████╗███████╗███████╗   ██║   ███████╗
#╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝

import random

import tic_tac_toe
from tic_tac_toe import tic_tac_toe


with open("student_handbook.txt", "r") as file:
    print(file.readline())

likeToPlay = "yes"                                                                                                                                          

attempt_num = 5



#this is the number guessing game
def num_gussing_game():
    print("welcom to num buessing game terminal.")
    rand_num = random.int(1, 1000000)
    print("you will have 5 apempts to guess the number it is between 1 and 1,000,000.")
        #adds loop to make it so that the user can only try a certain amount of times
    while attempt_num > 0:
        user_num = input("what is the number that you want? ")
        #hidden eater egg for bible
        user_num=int(user_num)
        if user_num == 923194:
            print("""

""")    #hidden eater egg for the student hand book
        elif user_num == 535072:
            print("""

""")
        # tells user that their number is to large
        elif rand_num > user_num:
            print("""yooooooooooooooooooooooooooooooo, your number is toooooo small.""")
        #tells user that they got it right and that the odds of it were next to impossible
        elif rand_num == user_num:
            print("""you got it right! you realize the odds of the right? is is just as likly as you getting the Ucas Student Handbook number. there is a number inbetween 1 and 1,000,000 that will indeed print the .""")
        #tells user that their number is to high.
        elif user_num > rand_num:
            print("so... umm... you number is a little high.")

    #if user_num > rand_num: 
#main function for the game
def game():
    while "3":
        game_to_play=input("""what game do you want to play?
                    1. tic tak toe.
                    2. number guessing game.
                    3. Home screen
                    (example choise 1. Use intager number).
                    """)
        #sends to tic tac toe
        if game_to_play == "1":
            tic_tac_toe()
        #sends to number guessing game
        elif game_to_play == "2":
            num_gussing_game()
        #sends back to main.
        elif game_to_play == "3":
            break
        else:
            print("give valid varible")

game()