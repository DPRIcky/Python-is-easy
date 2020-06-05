import numpy as np
import pygame
import sys
import math

blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

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

def draw_board(board):
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.rect(screen,blue, (c*squaresize, r*squaresize+squaresize, squaresize, squaresize))
            pygame.draw.circle(screen, black, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), radius)
    
    for c in range(column_count):
        for r in range(row_count):
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c*squaresize+squaresize/2), height - int(r*squaresize+squaresize/2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, yellow, (int(c*squaresize+squaresize/2), height - int(r*squaresize+squaresize/2)), radius)    
    pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

squaresize = 100

width = column_count*squaresize
height = (row_count+1)*squaresize

size = (width,height)

radius = int((squaresize/2)-5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace",75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,black, (0, 0, width, squaresize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, red, (posx, int(squaresize/2)), radius)
            else:
                pygame.draw.circle(screen, yellow, (posx, int(squaresize/2)), radius)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,black, (0, 0, width, squaresize))
            
            #Ask for player 1 input
            if turn == 0:
                posx = event.pos[0]
                # print(player1,end=" ")
                col = int(math.floor(posx/squaresize))

                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,1)

                    if winning_move(board,1):
                        label = myfont.render("Player 1 wins!!!",1,red)
                        screen.blit(label, (40,10))
                        print("Congratulations",player1,"Wins!!!")
                        game_over = True

                turn = 1

            else:
                posx = event.pos[0]
                # print(player2,end=" ")
                col = int(math.floor(posx/squaresize))

                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,2)

                    if winning_move(board,2):
                        label = myfont.render("player2 wins!!!",2,yellow)
                        screen.blit(label, (40,10))
                        print("Congratulations",player2,"Wins!!!")
                        game_over = True

                turn = 0
            
            print_board(board)
            draw_board(board)

            if game_over:
                pygame.time.wait(3000)