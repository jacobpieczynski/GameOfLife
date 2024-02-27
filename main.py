import os
from random import random
from time import sleep
import cursor
cursor.hide()

THRESHOLD = 0.5

# Randomly generates a board with given height and width variables
def init_board(width, height):
    board = [[0 for _ in range(width)] for _ in range(height)]

    for h in range(height):
        for w in range(width):
            if random() >= THRESHOLD:
                board[h][w] = 1
    return board

# Renders the board based on the alive/dead state of the cell
def render(board):
    for h in range(len(board)):
        for w in range(len(board[h])):
            if board[h][w] == 1:
                print('█', end='')
            else:
                print('  ',end='')
        print()

# Finds the next board based off the game of life rules
def next_board_state(board):
    new_board = board.copy()
    for h in range(len(board)):
        for w in range(len(board[h])):
            neighbors = 0
            points = [(h-1, w), (h+1, w), (h-1, w-1), (h, w-1),
            (h+1, w-1), (h-1, w+1), (h, w+1), (h+1, w+1)]
            # Gets the list of valid checkable points
            neighbor_points = [neighbor for neighbor in points if validate_cell(neighbor, len(board), len(board[0]))]
            # A living neighbor is represented by a 1
            for pt in neighbor_points:
                neighbors += board[pt[0]][pt[1]]
            
            # Basic game of life rules for whether a cell is alive or dead
            if (neighbors == 0 or neighbors == 1) and board[h][w] == 1:
                new_board[h][w] = 0
            elif (neighbors == 2 or neighbors == 3) and board[h][w] == 1:
                new_board[h][w] = 1
            elif neighbors > 3 and board[h][w] == 1:
                new_board[h][w] = 0
            elif neighbors == 3 and board[h][w] == 0:
                new_board[h][w] = 1

    return new_board

# Verifies that a given set of coordinates is valid
def validate_cell(coordinate, height, width):
    if coordinate[0] < 0 or coordinate[1] < 0:
        return False
    elif coordinate[0] >= height or coordinate[1] >= width:
        return False
    else:
        return True

def main():
    board = init_board(50, 50)
    # Constant loop to update game
    while True:
        os.system('clear')
        render(board)
        board = next_board_state(board)
        sleep(0.3)
    
main()