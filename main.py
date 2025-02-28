# Evan McCabe Highscore Tracker Set High Score Function

#Tic-Tac-Toe and Number Guessing Game

#Tic-Tac-Toe high score variables:
TTThighScore1 = {
    "name": "None",
    "score": 0
}
TTThighScore2 = {
    "name": "None",
    "score": 0
}
TTThighScore3 = {
    "name": "None",
    "score": 0
}

#Number Guessing Game high score variables:
NGGhighScore1 = {
    "name": "None",
    "score": 0
}
NGGhighScore2 = {
    "name": "None",
    "score": 0
}
NGGhighScore3 = {
    "name": "None",
    "score": 0
}

#Evan's Function
#Set High Score Function:
def setHighScore(game, name, score):

	#If the function is being called for Tic-Tac-Toe:
    if game == "Tic-Tac-Toe":
        
        #if current score is greater than high score 1:
        if score >= TTThighScore1["score"]:
            
            #Transfer high score 2’s value to high score 3:
            TTThighScore3["name"] = TTThighScore2["name"]
            TTThighScore3["score"] = TTThighScore2["score"]

            #Transfer high score 1’s value to high score 2:
            TTThighScore2["name"] = TTThighScore1["name"]
            TTThighScore2["score"] = TTThighScore1["score"]

            #Transfer the value of the current score to high score 1:
            TTThighScore1["name"] = name
            TTThighScore1["score"] = score

        #if current score is not greater than high score 1:
        else:

            #if current score is greater than high score 2:
            if score >= TTThighScore2["score"]:

                #Transfer high score 2’s value to high score 3:
                TTThighScore3["name"] = TTThighScore2["name"]
                TTThighScore3["score"] = TTThighScore2["score"]

                #Transfer the value of the current score to high score 2:
                TTThighScore2["name"] = name
                TTThighScore2["score"] = score

            #if current score is not greater than high score 2:
            else:

                #if current score is greater than high score 3:
                if score >= TTThighScore3["score"]:

                    #Transfer the value of the current score to high score 3:
                    TTThighScore3["name"] = name
                    TTThighScore3["score"] = score

    #If the function is being called for Number Guessing Game:
    elif game == "Number Guessing Game":
        
        #if current score is greater than high score 1:
        if score >= NGGhighScore1["score"]:
            
            #Transfer high score 2’s value to high score 3:
            NGGhighScore3["name"] = NGGhighScore2["name"]
            NGGhighScore3["score"] = NGGhighScore2["score"]

            #Transfer high score 1’s value to high score 2:
            NGGhighScore2["name"] = NGGhighScore1["name"]
            NGGhighScore2["score"] = NGGhighScore1["score"]

            #Transfer the value of the current score to high score 1:
            NGGhighScore1["name"] = name
            NGGhighScore1["score"] = score

        #if current score is not greater than high score 1:
        else:

            #if current score is greater than high score 2:
            if score >= NGGhighScore2["score"]:

                #Transfer high score 2’s value to high score 3:
                NGGhighScore3["name"] = NGGhighScore2["name"]
                NGGhighScore3["score"] = NGGhighScore2["score"]

                #Transfer the value of the current score to high score 2:
                NGGhighScore2["name"] = name
                NGGhighScore2["score"] = score

            #if current score is not greater than high score 2:
            else:

                #if current score is greater than high score 3:
                if score >= NGGhighScore3["score"]:

                    #Transfer the value of the current score to high score 3:
                    NGGhighScore3["name"] = name
                    NGGhighScore3["score"] = score
                    
#Asher's function
# Function to Display High Scores:
def displayHighScores():
    
	#Asks the user for what game they want to display highscores of
    display_game = input("""
Which game do you want To display the high scores of?
1. Number Guessing Game
2. Tic-Tac-Toe
""")

	#If the user chooses to display the highscores of the number guessing game:
    if display_game == "1":
        
		#Display the number guessing game highscores:
        print("\nNumber Guessing Game Highscores:")
        print("1. ",NGGhighScore1["name"],": ",NGGhighScore1["score"])
        print("2. ",NGGhighScore2["name"],": ",NGGhighScore2["score"])
        print("3. ",NGGhighScore3["name"],": ",NGGhighScore3["score"])
        
	#If the user chooses to display the highscores of tic-tac-toe:
    elif display_game == "2":
        
		#Display the tic-tac-toe highscores:
        print("\nTic-Tac-Toe Highscores:")
        print("1. ",TTThighScore1["name"],": ",TTThighScore1["score"])
        print("2. ",TTThighScore2["name"],": ",TTThighScore2["score"])
        print("3. ",TTThighScore3["name"],": ",TTThighScore3["score"])

	#If the user doesn't choose a valid option:    
    else:
        
		#Tell the user they chose an invalid option:
        print("\nNot An Option!")
        

#Start the program:
main()