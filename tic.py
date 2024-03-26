def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        row = int(input(f"Player {player}, choose row (0, 1, 2): "))
        col = int(input(f"Player {player}, choose column (0, 1, 2): "))
        
        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue
        
        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break
        
        player = "O" if player == "X" else "X"

tic_tac_toe()
