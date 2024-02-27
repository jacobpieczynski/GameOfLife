import os
from random import random
from time import sleep
import cursor

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
    print('Welcome to Conway\'s Game of Life.')
    dec = ''
    board = []
    while dec == '':
        choice = input('Would you like to load a file (1), or choose a random board? (2): ')
        if choice == '1' or choice == '2':
            dec = int(choice)
    if dec == 1:
        filename = input('What is the filepath? ')
        try:
            with open(filename) as file:
                h, w = 0, 0
                for line in file:
                    newln = []
                    w = 0
                    for char in line:
                        print(line)
                        if char != '\n' : newln.append(int(char))
                        w += 1
                    board.append(newln)
                    h += 1
        except:
            print(f'File {filename} not found!')
            return 0
    else:
        board = init_board(50, 50)

    # Constant loop to update game
    cursor.hide()
    while True:
        os.system('clear')
        render(board)
        board = next_board_state(board)
        sleep()
    
main()