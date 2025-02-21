# Evan McCabe, Asher Wangia, Connor Pavicic, Gavin Pierce Highscore Tracker


#██████╗  ██████╗ ███╗   ██╗████████╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗
#██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝
#██║  ██║██║   ██║██╔██╗ ██║   ██║       ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  
#██║  ██║██║   ██║██║╚██╗██║   ██║       ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  
#██████╔╝╚██████╔╝██║ ╚████║   ██║       ██████╔╝███████╗███████╗███████╗   ██║   ███████╗
#╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝
                                                                                                                                                                                                       
likeToPlay = "yes"                                                                                                                                          

import random

#tic tac toe function to for game one
def tic_tac_toe():
    gameBoard = [[" " for _ in range(3)] for _ in range(3)]
    def printBoard():
        for row in gameBoard:
            print("|".join(row))
            print("-" * 5)

    def checkWinner():
        for row in gameBoard:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        for col in range(3):
            if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col] and gameBoard[0][col] != " ":
                return gameBoard[0][col]
        if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] and gameBoard[0][0] != " ":
            return gameBoard[0][0]
        if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] and gameBoard[0][2] != " ":
            return gameBoard[0][2]
        return None

    def isBoardFull():
        for row in gameBoard:
            if " " in row:
                return False
        return True

    if likeToPlay == "yes":
        print("You are X and the computer is O.")
        print("Enter your move as row and column numbers separated by a space (e.g., '1 1' for the top-left corner).")
        printBoard()

        gameOver = False
        while not gameOver:
            moveValid = False
            while not moveValid:
                try:
                    userMove = input("Your turn! Enter your move: ")
                    row, col = map(int, userMove.split())
                    if gameBoard[row][col] == " ":
                        gameBoard[row][col] = "X"
                        moveValid = True
                    else:
                        print("That space is already taken. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter two numbers between 0 and 2 separated by a space.")

            printBoard()

            winner = checkWinner()
            if winner:
                print(f"{winner} wins!")
                gameOver = True
                break
            if isBoardFull():
                print("It's a tie!")
                gameOver = True
                break

            print("Computer's turn...")
            moveValid = False
            while not moveValid:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if gameBoard[row][col] == " ":
                    gameBoard[row][col] = "O"
                    moveValid = True

            printBoard()

            winner = checkWinner()
            if winner:
                print(f"{winner} wins!")
                gameOver = True
                break
            if isBoardFull():
                print("It's a tie!")
                gameOver = True

def num_gussing_game():
    print("welcom to num buessing game terminal.")
    rand_num = random.randint(1, 1000000)
    user_num = int("what is the number that you want? ")
    
    print(user_num)
    print(rand_num)

    #if user_num > rand_num: 

def game():
    while "3":
        game_to_play=input("""what game do you want to play?
                    1. tic tak toe.
                    2. number guessing game.
                    3. Home screen
                    (example choise 1. Use intager number).
                    """)
        
        if game_to_play == "1":
            tic_tac_toe()
        elif game_to_play == "2":
            num_gussing_game()
        else:
            print("give valid varible")

#    elif game_to_play == "3":
#        break

#        back to main

game()