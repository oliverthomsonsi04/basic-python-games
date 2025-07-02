def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("\n" + " | ".join(board[0:3]))
    print("--+---+--")
    print(" | ".join(board[3:6]))
    print("--+---+--")
    print(" | ".join(board[6:9]) + "\n")

def check_winner(board, player):
    """Checks if a player has won."""
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def tic_tac_toe():
    """A command-line Tic-Tac-Toe game."""
    board = [str(i + 1) for i in range(9)]
    current_player = "X"
    game_over = False
    moves = 0

    print("--- Welcome to Tic-Tac-Toe! ---")

    while not game_over:
        print_board(board)
        
        try:
            # Get player move
            move = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
            
            # Check if the move is valid
            if 0 <= move <= 8 and board[move].isdigit():
                board[move] = current_player
                moves += 1
                
                # Check for a winner
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"🎉 Player {current_player} wins! Congratulations!")
                    game_over = True
                # Check for a tie
                elif moves == 9:
                    print_board(board)
                    print("It's a tie! 🤝")
                    game_over = True
                else:
                    # Switch players
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move. That spot is already taken or out of range.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
