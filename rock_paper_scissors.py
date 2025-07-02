import random

def rock_paper_scissors():
    """A classic game of Rock, Paper, Scissors against the computer."""
    
    options = ["rock", "paper", "scissors"]
    
    print("--- Welcome to Rock, Paper, Scissors! ---")

    while True:
        # Get user's choice
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

        if user_choice == "quit":
            print("Thanks for playing!")
            break

        if user_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Get computer's choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win! 🎉")
        else:
            print("You lose! 😢")

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()
