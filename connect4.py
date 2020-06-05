import numpy as np

player1 = input("Enter your name: ")
print(player1,"you are Player 1")
player2 = input("Enter your name: ")
print(player2,"you are Player 2")

row_count = 6
column_count  = 7

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board,row,col,piece):
    board[row][col] = piece

def is_valid_location(board,col):
    return board[5][col] == 0

def get_next_open_row(board,col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board,0))

def winning_move(board,piece):
    #check horizontal location
    for c in range(column_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #Check virticle location
    for c in range(column_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    #Check positive slope diagonal location
    for c in range(column_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    
    #Check negative slope diagonal location
    for c in range(column_count-3):
        for r in range(3,row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    #Ask for player 1 input
    if turn == 0:
        print(player1,end=" ")
        col = int(input("make your move (0-6): "))

        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,1)

            if winning_move(board,1):
                print("Congratulations",player1,"Wins!!!")
                game_over = True

        turn = 1

    else:
        print(player2,end=" ")
        col = int(input("make your move (0-6): "))
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,2)

            if winning_move(board,2):
                print("Congratulations",player2,"Wins!!!")
                game_over = True

        turn = 0
    
    print_board(board)
