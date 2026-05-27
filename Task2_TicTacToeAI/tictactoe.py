import random

board = [" " for i in range(9)]

# Display board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True

    return False

# Check draw
def board_full():
    return " " not in board

# AI move logic
def computer_move():

    # First try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            if check_winner("O"):
                return

            board[i] = " "

    # Block player winning move
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            if check_winner("X"):
                board[i] = "O"
                return

            board[i] = " "

    # Take center if free
    if board[4] == " ":
        board[4] = "O"
        return

    # Otherwise random move
    while True:
        move = random.randint(0, 8)

        if board[move] == " ":
            board[move] = "O"
            return


print("****TIC TAC TOE AI******")


print("Youre sign is  X")
print("Computer sign is O")

print_board()

while True:

    # Player move
    try:
        user_move = int(input("Enter position (1-9): ")) - 1

        if user_move < 0 or user_move > 8:
            print("Invalid position!")
            continue

        if board[user_move] != " ":
            print("Position already taken!")
            continue

        board[user_move] = "X"

    except:
        print("Please enter a valid number!")
        continue

    print_board()

    # Player wins
    if check_winner("X"):
        print("Congratulations! You win!")
        break

    # Draw
    if board_full():
        print("Match Draw!")
        break

    # Computer turn
    print("Computer's turn...")

    computer_move()

    print_board()

    # Computer wins
    if check_winner("O"):
        print("Computer wins!")
        break

    # Draw
    if board_full():
        print("Match Draw!")
        break