import random

def guess_the_number():
    """A simple number guessing game."""
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = 0

    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    # Main game loop
    while guess != secret_number:
        try:
            # Get user input
            guess = int(input("Take a guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Good job! You guessed the number in {attempts} attempts!")
        
        except ValueError:
            # Handle cases where input is not a number
            print("Invalid input. Please enter a number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
