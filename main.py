#Connor Pavicic, main_function

def main(): #Main function
	print('This is a program where you can play some fun and cool games, and it saves our high score. Have fun!')
	
	while True:
		choice = input("""Which one do you want to do?:
1: Play a game
2: Display high scores
3: Exit the program
	
(1, 2, or 3): """).strip()

		if choice == '1':
			# Run Gavin's functions
			print('Run Gavins function.')
			pass
		elif choice == '2':
			# Run Asher's function
			print('Run Ashers function')
			pass
		elif choice == '3':
			print('Thanks for playing!')
			break
		else:
			print('Incorrect option, try again.')
			continue

main()