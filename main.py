import os

# Define the initial board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Define the functions

def draw_board():
    os.system("cls")
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("\n")

def play_move(player):
    position = int(input("Enter the position to play (1-9): ")) - 1
    if board[position] == " ":
        board[position] = player
    else:
        print("Position already played!")
        play_move(player)

def check_winner():
    for i in range(0, 9, 3):
        if board[i] == board[i+1] and board[i+1] == board[i+2] and board[i] != " ":
            return board[i]
    for i in range(0, 3):
        if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] != " ":
            return board[i]
    if board[0] == board[4] and board[4] == board[8] and board[0] != " ":
        return board[0]
    if board[2] == board[4] and board[4] == board[6] and board[2] != " ":
        return board[2]
    if " " not in board:
        return "Draw"
    return None

# Define the current player variable
current_player = "X"

# Start the game
while True:
    draw_board()
    play_move(current_player)
    winner = check_winner()
    if winner is not None:
        draw_board()
        if winner == "Draw":
            print("It's a draw!")
        else:
            print(winner + " wins!")
        break
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
