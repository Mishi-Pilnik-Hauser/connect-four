def print_board(board):
    print("-----------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-----------------")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(4):
        if all([board[row][col] == player for row in range(4)]):
            return True
    if all([board[i][i] == player for i in range(4)]) or all([board[i][2-i] == player for i in range(4)]):
        return True
    return False

def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def get_move(board):
    while True:
        try:
            move = int(input("Enter a position (1-16): ")) - 1
            if move < 0 or move >= 16:
                print("Invalid position. Please try again.")
                continue
            row, col = divmod(move, 4)
            if board[row][col] != ' ':
                print("Position already taken. Please try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 16.")

def tic_tac_toe():
    board = [[' ' for _ in range(4)] for _ in range(4)]
    players = ['X', 'O']
    current_player = 0

    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn.")
        row, col = get_move(board)
        board[row][col] = players[current_player]

        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player
if __name__ == "__main__":
    tic_tac_toe()
