# Connor Pavicic, main function
# Main function to run the program:

from display_high_scores import displayHighScores
from num_guessing import num_guessing_game
from tic_tac_toe import tic_tac_toe

def main():
    print('\nWelcome! Play some fun games and save your high scores. Have fun!')

    while True:
        choice = input("""\nWhat would you like to do?:
1: Play Tic-Tac-Toe
2: Play Number Guessing
3: Display High Scores
4: Exit the program

(Enter 1, 2, 3, or 4): """)

        if choice == '1':
            print("\nStarting Tic-Tac-Toe...\n")
            tic_tac_toe()

        elif choice == '2':
            print("\nStarting Number Guessing Game...\n")
            num_guessing_game()

        elif choice == '3':
            print("\nDisplaying High Scores...\n")
            displayHighScores()

        elif choice == '4':
            confirm = input("\nAre you sure you want to exit? (y/n): ").strip().lower()
            if confirm == 'y':
                print('\nThanks for playing!\n')
                break

        else:
            print('\nInvalid choice, please try again.')

# Start the program:
if __name__ == "__main__":
    main()