import random



#this is the number guessing game
def num_gussing_game():
    attempt_num = 5
    print("welcom to num buessing game terminal.")
    rand_num = random.randint(1, 1000000)
    print("you will have 5 apempts to guess the number it is between 1 and 1,000,000.")
        #adds loop to make it so that the user can only try a certain amount of times
    while attempt_num > 0:
        try:
            user_num = int(input("what is the number that you want? "))

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

        except ValueError:
            print('Incorrect input, try again.')