

#██████╗  ██████╗ ███╗   ██╗████████╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗
#██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝
#██║  ██║██║   ██║██╔██╗ ██║   ██║       ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  
#██║  ██║██║   ██║██║╚██╗██║   ██║       ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  
#██████╔╝╚██████╔╝██║ ╚████║   ██║       ██████╔╝███████╗███████╗███████╗   ██║   ███████╗
#╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝

likeToPlay = "yes"   

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