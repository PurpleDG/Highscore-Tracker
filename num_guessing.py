import random


#this is the number guessing game
def num_gussing_game():
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
