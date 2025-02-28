# Evan McCabe, Asher Wangia, Connor Pavicic, Gavin Pierce Highscore Tracker

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