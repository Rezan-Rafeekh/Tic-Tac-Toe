import random

board = [" " for _ in range(9)]


def print_board():
    print()
    for row in range(3):
        print(
            f" {board[row*3]} | {board[row*3+1]} | {board[row*3+2]} "
        )
        if row < 2:
            print("---|---|---")
    print()


def print_positions():
    print("\nBoard Positions:\n")

    positions = [str(i + 1) for i in range(9)]

    for row in range(3):
        print(
            f" {positions[row*3]} | {positions[row*3+1]} | {positions[row*3+2]}"
        )
        if row < 2:
            print("---|---|---")


def check_winner(player):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True

    return False


def board_full():
    return " " not in board


def player_move():

    while True:
        try:
            move = int(
                input("Choose position (1-9): ")
            ) - 1

            if move < 0 or move > 8:
                print("Invalid position.")
                continue

            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Position already occupied.")

        except ValueError:
            print("Enter a number between 1 and 9.")


def ai_move():

    # Win if possible
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "

    # Block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "

    # Take center
    if board[4] == " ":
        board[4] = "O"
        return

    # Random move
    available = [
        i for i in range(9)
        if board[i] == " "
    ]

    board[random.choice(available)] = "O"


def play_game():

    global board
    board = [" " for _ in range(9)]

    print("\n=== TIC TAC TOE AI ===")

    print_positions()

    while True:

        print_board()

        player_move()

        if check_winner("X"):
            print_board()
            print("🎉 You Win!")
            break

        if board_full():
            print_board()
            print("🤝 It's a Draw!")
            break

        print("\nAI is thinking...\n")

        ai_move()

        if check_winner("O"):
            print_board()
            print("🤖 AI Wins!")
            break

        if board_full():
            print_board()
            print("🤝 It's a Draw!")
            break


while True:

    play_game()

    again = input(
        "\nPlay Again? (y/n): "
    ).lower()

    if again != "y":
        print("Thanks for playing!")
        break
