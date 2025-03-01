# Display High Scores Function: Asher Wangia

# Tic-Tac-Toe high score variables:
TTThighScore1 = {"name": "None", "score": 0}
TTThighScore2 = {"name": "None", "score": 0}
TTThighScore3 = {"name": "None", "score": 0}

# Number Guessing Game high score variables:
NGGhighScore1 = {"name": "None", "score": 0}
NGGhighScore2 = {"name": "None", "score": 0}
NGGhighScore3 = {"name": "None", "score": 0}

def displayHighScores():
    
    # Ask the user which game's high scores they want to display:
    display_game = input("""\nWhich game do you want to display the high scores of?
1: Number Guessing Game
2: Tic-Tac-Toe

(Enter 1 or 2): """)

    # If the user chooses to display the high scores of the number guessing game:
    if display_game == "1":
        
        # Display the number guessing game high scores:
        print("\nNumber Guessing Game High Scores:")
        print("1.", NGGhighScore1["name"], ":", NGGhighScore1["score"])
        print("2.", NGGhighScore2["name"], ":", NGGhighScore2["score"])
        print("3.", NGGhighScore3["name"], ":", NGGhighScore3["score"])
        
    # If the user chooses to display the high scores of tic-tac-toe:
    elif display_game == "2":
        
        # Display the tic-tac-toe high scores:
        print("\nTic-Tac-Toe High Scores:")
        print("1.", TTThighScore1["name"], ":", TTThighScore1["score"])
        print("2.", TTThighScore2["name"], ":", TTThighScore2["score"])
        print("3.", TTThighScore3["name"], ":", TTThighScore3["score"])

    # If the user enters an invalid choice:
    else:
        print("\nInvalid choice. Please enter 1 or 2.")
