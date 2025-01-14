import random

# Constants
PLAYER = 'X'
AI = 'O'
EMPTY = ' '

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if the game has ended (win or draw)
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != EMPTY for row in board for cell in row])

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, AI):
        return 1  # AI wins
    if check_win(board, PLAYER):
        return -1  # Player wins
    if is_full(board):
        return 0  # Draw

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Function to handle human move
def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER
                break
            else:
                print("Cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter row and column values between 0 and 2.")

# Main function to play the game
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe Game! You are 'X' and AI is 'O'.")
    print_board(board)

    while True:
        # Player's move
        player_move(board)
        print_board(board)
        if check_win(board, PLAYER):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI's move:")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = AI
        print_board(board)
        if check_win(board, AI):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Start the game
play_game()
