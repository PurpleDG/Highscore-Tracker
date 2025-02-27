#Connor Pavicic, main_function

def main(): #Main function
	print('This is a program where you can play some fun and cool games, and it saves our high score. Have fun!')
	
	while True:
		
        #Ask the user if they want to play a game, display high scores, or exit the program:
		choice = input("""\nWhich one do you want to do?:
1: Play a game
2: Display high scores
3: Exit the program
	
(1, 2, or 3): """).strip()

		if choice == '1':
			# Run Gavin's functions
			print('\nRun Gavins function.')
			pass
		
        #If the user chose to display high scores:
		elif choice == '2':
			# Run Asher's function
			print('\nRun Ashers function')
			pass
		
        #If the user chose to exit the program:
		elif choice == '3':
			print('\nThanks for playing!')
			break
		else:
			print('\nIncorrect option, try again.')
			continue

main()