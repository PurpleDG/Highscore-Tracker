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
        
#Gavin Pierce, Run Game Function


#██████╗  ██████╗ ███╗   ██╗████████╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗
#██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝
#██║  ██║██║   ██║██╔██╗ ██║   ██║       ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  
#██║  ██║██║   ██║██║╚██╗██║   ██║       ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  
#██████╔╝╚██████╔╝██║ ╚████║   ██║       ██████╔╝███████╗███████╗███████╗   ██║   ███████╗
#╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝

likeToPlay = "yes"                                                                                                                                          

import random

tic_tac_toe_highscore=0

def tic_tac_toe():
    rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    human_wins = ''
    computer_wins = ''

    display_count = 1

    for row in range(3):
        for col in range(3):
            print(display_count, end=' ')
            display_count += 1
        print()

    while True:
        count = 0
        #1 = 0 0
        #2 = 0 1
        #3 = 0 2
        #4 = 1 0
        #5 = 1 1
        #6 = 1 2
        #7 = 2 0
        #8 = 2 1
        #9 = 2 2

        num = input('Enter a number on the board: ')

        if num == '1':
            for row in range(3):
                for column in range(3):
                    if num == '1':
                        if row == 0 and column == 0:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('1')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '2':
            for row in range(3):
                for column in range(3):
                    if num == '2':
                        if row == 0 and column == 1:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('2')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '3':
            for row in range(3):
                for column in range(3):
                    if num == '3':
                        if row == 0 and column == 2:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('3')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '4':
            for row in range(3):
                for column in range(3):
                    if num == '4':
                        if row == 1 and column == 0:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('4')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '5':
            for row in range(3):
                for column in range(3):
                    if num == '5':
                        if row == 1 and column == 1:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('5')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '6':
            for row in range(3):
                for column in range(3):
                    if num == '6':
                        if row == 1 and column == 2:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('6')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '7':
            for row in range(3):
                for column in range(3):
                    if num == '7':
                        if row == 2 and column == 0:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('7')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '8':
            for row in range(3):
                for column in range(3):
                    if num == '8':
                        if row == 2 and column == 1:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('8')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '9':
            for row in range(3):
                for column in range(3):
                    if num == '9':
                        if row == 2 and column == 2:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('9')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()
        print()

    
        if rows[0] == rows[1] and rows[1] == rows[2] and rows[0] == 'X':
            print('You won!')
            tic_tac_toe_highscore+=1
            tic_tac_toe()
        elif rows[3] == rows[4] and rows[4] == rows[5] and rows[3] == 'X':
            print('You won!')
            tic_tac_toe_highscore+=1
            tic_tac_toe()
        elif rows[6] == rows[7] and rows[7] == rows[8] and rows[6] == 'X':
            print('You won!')
            tic_tac_toe_highscore+=1
            tic_tac_toe()
        elif rows[0] == rows[3] and rows[3] == rows[6] and rows[0] == 'X':
            print('You won!')
            tic_tac_toe_highscore+=1
            tic_tac_toe()
        elif rows[1] == rows[4] and rows[4] == rows[7] and rows[1] == 'X':
            print('You won!')
            tic_tac_toe_highscore+=1
            tic_tac_toe()
        elif rows[2] == rows[5] and rows[5] == rows[8] and rows[2] == 'X':
            print('You won!')
            tic_tac_toe_highscore+=1
            tic_tac_toe()
        elif rows[0] == rows[4] and rows[4] == rows[8] and rows[0] == 'X':
            print('You won!')
            tic_tac_toe_highscore+=1
            tic_tac_toe()
        elif rows[2] == rows[4] and rows[4] == rows[6] and rows[2] == 'X':
            print('You won!')
            tic_tac_toe_highscore+=1
            tic_tac_toe()
    
        computer_choice = random.choice(choice)
        print('Computer chose:', computer_choice)
        computer_count = 0

        if computer_choice == '1':
            for row in range(3):
                for column in range(3):
                    if computer_choice == '1':
                        if row == 0 and column == 0:
                            print('O', end=' ')
                            rows[computer_count] = 'O'
                            choice.remove('1')
                            computer_count += 1
                        else:
                            print(rows[computer_count], end=' ')
                            computer_count += 1
                print()

        if computer_choice == '2':
            for row in range(3):
                for column in range(3):
                    if computer_choice == '2':
                        if row == 0 and column == 1:
                            print('O', end=' ')
                            rows[computer_count] = 'O'
                            choice.remove('2')
                            computer_count += 1
                        else:
                            print(rows[computer_count], end=' ')
                            computer_count += 1
                print()

        if computer_choice == '3':
            for row in range(3):
                for column in range(3):
                    if computer_choice == '3':
                        if row == 0 and column == 2:
                            print('O', end=' ')
                            rows[computer_count] = 'O'
                            choice.remove('3')
                            computer_count += 1
                        else:
                            print(rows[computer_count], end=' ')
                            computer_count += 1
                print()

        if computer_choice == '4':
            for row in range(3):
                for column in range(3):
                    if computer_choice == '4':
                        if row == 1 and column == 0:
                            print('O', end=' ')
                            rows[computer_count] = 'O'
                            choice.remove('4')
                            computer_count += 1
                        else:
                            print(rows[computer_count], end=' ')
                            computer_count += 1
                print()

        if computer_choice == '5':
            for row in range(3):
                for column in range(3):
                    if computer_choice == '5':
                        if row == 1 and column == 1:
                            print('O', end=' ')
                            rows[computer_count] = 'O'
                            choice.remove('5')
                            computer_count += 1
                        else:
                            print(rows[computer_count], end=' ')
                            computer_count += 1
                print()

        if computer_choice == '6':
            for row in range(3):
                for column in range(3):
                    if computer_choice == '6':
                        if row == 1 and column == 2:
                            print('O', end=' ')
                            rows[computer_count] = 'O'
                            choice.remove('6')
                            computer_count += 1
                        else:
                            print(rows[computer_count], end=' ')
                            computer_count += 1
                print()

        if computer_choice == '7':
            for row in range(3):
                for column in range(3):
                    if computer_choice == '7':
                        if row == 2 and column == 0:
                            print('O', end=' ')
                            rows[computer_count] = 'O'
                            choice.remove('7')
                            computer_count += 1
                        else:
                            print(rows[computer_count], end=' ')
                            computer_count += 1
                print()

        if computer_choice == '8':
            for row in range(3):
                for column in range(3):
                    if computer_choice == '8':
                        if row == 2 and column == 1:
                            print('O', end=' ')
                            rows[computer_count] = 'O'
                            choice.remove('8')
                            computer_count += 1
                        else:
                            print(rows[computer_count], end=' ')
                            computer_count += 1
                print()

        if computer_choice == '9':
            for row in range(3):
                for column in range(3):
                    if computer_choice == '9':
                        if row == 2 and column == 2:
                            print('O', end=' ')
                            rows[computer_count] = 'O'
                            choice.remove('9')
                            computer_count += 1
                        else:
                            print(rows[computer_count], end=' ')
                            computer_count += 1
                print()
        print()


        if rows[0] == rows[1] and rows[1] == rows[2] and rows[0] == 'O':
            print('The computer won!')
            break
        elif rows[3] == rows[4] and rows[4] == rows[5] and rows[3] == 'O':
            print('The computer won!')
            break
        elif rows[6] == rows[7] and rows[7] == rows[8] and rows[6] == 'O':
            print('The computer won!')
            break
        elif rows[0] == rows[3] and rows[3] == rows[6] and rows[0] == 'O':
            print('The computer won!')
            break
        elif rows[1] == rows[4] and rows[4] == rows[7] and rows[1] == 'O':
            print('The computer won!')
            break
        elif rows[2] == rows[5] and rows[5] == rows[8] and rows[2] == 'O':
            print('The computer won!')
            break
        elif rows[0] == rows[4] and rows[4] == rows[8] and rows[0] == 'O':
            print('The computer won!')
            break
        elif rows[2] == rows[4] and rows[4] == rows[6] and rows[2] == 'O':
            print('The computer won!')
            break

        if str(len(choice)) == 0:
            print('The game was a draw!')
            break

#this is the number guessing game
def num_gussing_game():
    attempt_num = 5
    print("welcom to num buessing game terminal.")
    rand_num = random.randint(1, 1000000)
    print("you will have 5 apempts to guess the number it is between 1 and 1,000,000.")
        #adds loop to make it so that the user can only try a certain amount of times
    while attempt_num > 0:
        user_num = input("what is the number that you want? ")

        # tells user that their number is to large
        if rand_num > user_num:
            print("""yooooooooooooooooooooooooooooooo, your number is toooooo small.""")
            attempt_num -= 1
            place_holder_score=1000000-user_num
            num_gussing_score=1000000-place_holder_score


        #tells user that they got it right and that the odds of it were next to impossible
        elif rand_num == user_num:
            print("""you got it right! you realize the odds of the right? is is just as likly as you getting the Ucas Student Handbook number. there is a number inbetween 1 and 1,000,000 that will indeed print the .""")
            attempt_num -= 1
            place_holder_score=1000000-user_num
            num_gussing_score=1000000-place_holder_score

        #tells user that their number is to high.
        elif user_num > rand_num:
            print("so... umm... you number is a little high.")
            attempt_num -= 1
            place_holder_score=1000000-user_num
            num_gussing_score=1000000-place_holder_score

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
            main()
        else:
            print("give valid varible")

#Connor Pavicic, main function
#Main function to run the program:
def main():
     
	 #Introduce the program to the user:
	print('\nThis is a program where you can play some fun games and save your high scores. Have fun!')
	
	#Keep the program running in a loop:
	while True:
		
        #Ask the user if they want to play a game, display high scores, or exit the program:
		choice = input("""\nWhat would you like to do?:
1: Play a game
2: Display high scores
3: Exit the program

(1, 2, or 3): """)

		#If the user chooses to play a game:
		if choice == '1':
               
			#Run the play game function:
			game()
		
        #If the user chooses to display high scores:
		elif choice == '2':
			
			#Run the display highscores function:
			displayHighScores()
		
        #If the user chooses to exit the program:
		elif choice == '3':
			print('\nThanks for playing!\n')
			exit()
               
		#If the user does not choose a valid option:
		else:
               
			#Tell the user that they did not choose a valid option:
			print('\nIncorrect option, try again.')

#Start the program:
main()