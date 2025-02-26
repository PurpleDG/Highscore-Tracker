# Evan McCabe, Asher Wangia, Connor Pavicic, Gavin Pierce Highscore Tracker


#Asher's function
# Function to Display High Score 
def display_highscore():
    print("""
    Which game do you want To display high scores of
    1. Number Game
    2. Rock Paper Scissors
    3. Tic Tac Toe
          """)
    
    #Asks the user for what game they want to display highscores of
    display_game = input("Choose a Number: ")

    if display_game == "1": #Displays the highscores for the number guessing game
        print("Number Game High Scores")
        print("1st",numbergame_highscore["High Score 1"])
        print("2nd",numbergame_highscore["High Score 2"])
        print("3rd",numbergame_highscore["High Score 3"])
    elif display_game == "2":#Displays the highscores for rock paper scissors
        print("Rock Paper Scissors High Scores")
        print("1st",rock_highscore["High Score 1"])
        print("2nd",rock_highscore["High Score 2"])
        print("3rd",rock_highscore["High Score 3"])
    elif display_game == "3":#Displays the highscores for tic tac toe
        print("Tic Tac Toe High Scores")
        print("1st",tictactoe_highscore["High Score 1"])
        print("2nd",tictactoe_highscore["High Score 2"])
        print("3rd",tictactoe_highscore["High Score 3"])
    else:#Tells the user that their input was not one of the choices
        print("Not An Option!")
