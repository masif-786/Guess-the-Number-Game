import random

def get_feedback(guess, target):
    if abs(guess - target) >= 30:
        return "Way off! Try a much higher or lower number."
    elif abs(guess - target) >= 15:
        return "Getting warmer! You're on the right track."
    elif abs(guess - target) >= 5:
        return "Very close! Just a little more!"
    else:
        return "So close! Just one more guess!"

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the user's guess
            if user_guess < number_to_guess:
                print(get_feedback(user_guess, number_to_guess) + " It's higher.")
            elif user_guess > number_to_guess:
                print(get_feedback(user_guess, number_to_guess) + " It's lower.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
