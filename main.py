import csv
import numpy as np

from min_max_search import MinMaxSearch
"""
Author: Manasa Acharya 
Date: 10/12/2022
Class: CPSC 5610 AI - Milestone project 
This is the main class, it reads in 2048_in.txt, performs a MinMax Search with a depth of 3. 
To determine which of the 4 moves yields the max score.  

I  have  not  received  unauthorized  aid  on  this  assignment.  I  understand  the  answers  that  I  have 
submitted.  The  answers  submitted  have  not  been  directly  copied  from  another  source,  but 
instead are written in my own words.
"""

N = 3

def format_array(array):
    arr = np.array(array)
    print(arr)


def create_boards(input_file):
    total_boards = []
    row = []
    board = []
    count = 0
    with open(input_file) as my_file:
        n_boards = my_file.readline().strip()
        csv_reader = csv.reader(my_file)
        for line in csv_reader:
            if len(row) == 4:
                board.append(row)
                row = []
            if len(board) == 4:
                total_boards.append(board)
                board = []
            for x in line:
                row.append(int(x))
                count += 1
        board.append(row)
        total_boards.append(board)
    return total_boards


if __name__ == '__main__':
    all_boards = create_boards("2048_in.txt")
    # for Random search
    for x in all_boards:
        current_score = 0
        print("Printing empty board...", format_array(x))
        min_max = MinMaxSearch(x)
        min_max.start_board()
        print("Starting board:", x)
        while min_max.class_board.empty_space != 0:
            output = min_max.min_max_search(current_score, x)
            score, movement = output
            print("Playing minmax's round, moving ", movement)
            current_score += min_max.class_board.play_round(movement)
            format_array(x)
            print("Current score: ", current_score)
            print("Now randomly adding 2 or 4")
            min_max.class_board.add_two_or_four()
            format_array(x)
        if min_max.class_board.empty_space == 0:
            print("Max moves reached. Game terminated with high score of: ", current_score)





