from num_guessing import num_guessing_game  # Fixed typo in function name
from tic_tac_toe import tic_tac_toe
from main import main

def game_main():  

    # Ask the user which game they want to play:
    game_to_play = input("""\nWhich game do you want to play?:
1: Tic-Tac-Toe
2: Number Guessing Game
3: Go back

(1, 2, or 3): """)  
    
    # If the user chooses Tic-Tac-Toe:
    if game_to_play == "1":
        tic_tac_toe()

    # If the user chooses Number Guessing Game:
    elif game_to_play == "2":
        num_guessing_game()  # Fixed typo in function name

    # If the user chooses to go back to the main menu:
    elif game_to_play == "3":
        main()

    # If the user enters an invalid choice:
    else:
        print("\nInvalid input. Please enter 1, 2, or 3.")
