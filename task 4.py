import math

# Board initialization
board = [' ' for _ in range(9)]  # Flattened 3x3 board

def print_board(board):
    for i in range(3):
        print(board[i*3:(i+1)*3])
    print()

def is_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def is_draw(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'X'):
        return 1
    if is_winner(board, 'O'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth+1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth+1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board, is_max_player=True):
    move = -1
    best_score = -math.inf if is_max_player else math.inf

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X' if is_max_player else 'O'
            score = minimax(board, 0, not is_max_player)
            board[i] = ' '

            if is_max_player:
                if score > best_score:
                    best_score = score
                    move = i
            else:
                if score < best_score:
                    best_score = score
                    move = i
    return move

# Main Game Loop
print("Tic Tac Toe: AI is X (Max), You are O (Min)")
while True:
    print_board(board)

    # Human O move (Min)
    o_move = int(input("Enter your move (0-8): "))
    if board[o_move] != ' ':
        print("Invalid move! Try again.")
        continue
    board[o_move] = 'O'
    print(f"Min player (O) moved to {o_move}")

    if is_winner(board, 'O'):
        print_board(board)
        print("Min player (O) wins!")
        break
    if is_draw(board):
        print_board(board)
        print("Draw!")
        break

    # AI X move (Max)
    x_move = best_move(board, True)
    board[x_move] = 'X'
    print(f"Max player (X) moved to {x_move}")

    if is_winner(board, 'X'):
        print_board(board)
        print("Max player (X) wins!")
        break
    if is_draw(board):
        print_board(board)
        print("Draw!")
        break
