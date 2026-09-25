# CodSoft Artificial Intelligence Internship
# Task 2 - Tic-Tac-Toe AI using Minimax

import math

# Display the board
def print_board(board):
    print()
    print("-------------")

    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("-------------")

# Check whether a player has won
def check_winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Main diagonal
    if (
        board[0][0] == player
        and board[1][1] == player
        and board[2][2] == player
    ):
        return True

    # Other diagonal
    if (
        board[0][2] == player
        and board[1][1] == player
        and board[2][0] == player
    ):
        return True

    return False

# Check whether the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    # AI wins
    if check_winner(board, "O"):
        return 10 - depth

    # Human wins
    if check_winner(board, "X"):
        return depth - 10

    # Draw
    if is_board_full(board):
        return 0

    # Maximizing player - AI
    if is_maximizing:
        best_score = -math.inf

        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"

                    score = minimax(board, depth + 1, False)

                    # Undo the move
                    board[row][col] = " "

                    best_score = max(best_score, score)

        return best_score

    # Minimizing player - Human
    else:
        best_score = math.inf

        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"

                    score = minimax(board, depth + 1, True)

                    # Undo the move
                    board[row][col] = " "

                    best_score = min(best_score, score)

        return best_score

# Find the best move for the AI
def find_best_move(board):
    best_score = -math.inf
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"

                score = minimax(board, 0, False)

                # Undo the move
                board[row][col] = " "

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

# Get a valid move from the player
def get_player_move(board):
    while True:
        try:
            position = int(input("Enter your position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            row = (position - 1) // 3
            col = (position - 1) % 3

            if board[row][col] != " ":
                print("That position is already occupied. Try again.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")


# Play one game
def play_game():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print("=" * 45)
    print("        TIC-TAC-TOE AI")
    print("=" * 45)
    print("You are X")
    print("AI is O")
    print()
    print("Board positions:")
    print()
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()

    while True:
        # Player's turn
        print_board(board)
        print("\nYour turn (X).")

        row, col = get_player_move(board)
        board[row][col] = "X"

        # Check if player won
        if check_winner(board, "X"):
            print_board(board)
            print("\n🎉 Congratulations! You won!")
            return

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("\nIt's a draw!")
            return

        # AI's turn
        print("\n🤖 AI is thinking...")

        ai_move = find_best_move(board)

        if ai_move:
            row, col = ai_move
            board[row][col] = "O"

        # Check if AI won
        if check_winner(board, "O"):
            print_board(board)
            print("\n🤖 AI wins! Better luck next time.")
            return

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("\nIt's a draw!")
            return

# Main program
def main():
    while True:
        play_game()

        while True:
            play_again = input(
                "\nDo you want to play again? (yes/no): "
            ).strip().lower()

            if play_again in ["yes", "y"]:
                print("\nStarting a new game...\n")
                break

            elif play_again in ["no", "n"]:
                print("\nThanks for playing Tic-Tac-Toe AI! 👋")
                return

            else:
                print("Please enter yes or no.")

# Start the program
if __name__ == "__main__":
    main()