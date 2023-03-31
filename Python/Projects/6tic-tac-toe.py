def print_board(board):
    print("  1 2 3")
    for i in range(3):
        row = " ".join(board[i])
        print(f"{i+1} {row}")

def check_win(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return True
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != "-":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return True
    return False

def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                return False
    return True

def play_game():
    board = [["-" for j in range(3)] for i in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row number (1-3): ")) - 1
        col = int(input("Enter column number (1-3): ")) - 1
        if board[row][col] == "-":
            board[row][col] = current_player
            if check_win(board):
                print(f"Player {current_player} wins!")
                print_board(board)
                break
            elif check_draw(board):
                print("Draw!")
                print_board(board)
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already occupied")

if __name__ == "__main__":
    play_game()
