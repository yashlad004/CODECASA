import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    # Generate a random number within the specified range
    target_number = random.randint(lower_bound, upper_bound)
    num_guesses = 0

    while True:
        guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        num_guesses += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {target_number} in {num_guesses} guesses.")
            break

guessing_game()
