#Connor Pavicic, main function

#Main function to run the program:
def main():
	
    #Keep the program running in a loop:
	while True:
		
        #Ask the user if they want to play a game, display high scores, or exit the program:
		choice = input("""Which one do you want to do?:
1: Play a game
2: Display high scores
3: Exit the program
""")

        #If the user chose to play a game:
		if choice == '1':
			# Run Gavin's functions
			pass
		
        #If the user chose to display high scores:
		elif choice == '2':
			# Run Asher's function
			pass
		
        #If the user chose to exit the program:
		elif choice == '3':
			print('Thanks for playing!\n')
			exit()