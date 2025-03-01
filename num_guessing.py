import random

# This is the number guessing game
def num_guessing_game():
    game = "Number Guessing Game"
    attempt_num = 5
    print("\nWelcome to the Number Guessing Game!")

    # Generate a random number between 1 and 1,000,000
    rand_num = random.randint(1, 1000000)
    print("You have 5 attempts to guess the number. It is between 1 and 1,000,000.")

    # Loop until the user runs out of attempts
    while attempt_num > 0:
        try:
            user_num = int(input("\nEnter your guess: "))

            # If the guess is too low
            if user_num < rand_num:
                print("Your guess is too low. Try again!")
            
            # If the guess is too high
            elif user_num > rand_num:
                print("Your guess is too high. Try again!")

            # If the user guesses correctly
            else:
                print("\nYou got it right! Do you realize how lucky that is? The odds are 1 in 1,000,000!")
                break  # Exit the loop if guessed correctly

            # Update attempts and calculate score
            attempt_num -= 1
            num_guessing_score = 1000000 - abs(rand_num - user_num)
        
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nGame Over!")
    return game
