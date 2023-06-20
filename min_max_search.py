import random
from random import choice
from board import Board
import copy

"""
Author: Manasa Acharya 
Date: 11/4/2022
Class: CPSC 5610 AI - Milestone project 
This is the MinMax Search algorithm. The algorithm checks with a d = 3, which movve will yield the max result. 
"""


class MinMaxSearch:
    def __init__(self, board):
        self.board = board
        self.class_board = Board(board)
        self.complete_moves = []
        self.moves = ["L", "D", "U", "R"]

    def start_board(self):
        self.class_board.start_board()

    def min_max_search(self, current_score, board):
        max_states = []
        new_board = copy.deepcopy(board)
        current_board = Board(new_board)
        # maximizer determines max move so far
        for x in self.moves:
            current_score = current_board.play_round(x)
            # with now updated board, determine min board + new current score
            min_movement, updated_board = self.min_search(current_score, new_board)
            # figure out what is the max movement next & yields the highest score
            final_score, movement = self.max_search(current_score, updated_board)
            max_states.append((final_score, x))
        return(max(max_states))



    def min_search(self, current_score, max_board):
        # find the spot to put 2 or 4 that returns minimum score and return that board
        min_states = []
        for x in self.moves:
            for i in range(0, 4):
                for j in range(0, 4):
                    new_board = copy.deepcopy(max_board)
                    current_board = Board(new_board)
                    if current_board.board[i][j] == 0:
                        current_board.board[i][j] = 2
                        next_score, board = self.search_states(x, current_board, current_score)
                        min_states.append((next_score, x, board))
        for x in self.moves:
            for i in range(0, 4):
                for j in range(0, 4):
                    new_board = copy.deepcopy(max_board)
                    current_board = Board(new_board)
                    if current_board.board[i][j] == 0:
                        current_board.board[i][j] = 4
                        next_score, board = self.search_states(x, current_board, current_score)
                        min_states.append((next_score, x, board))
        return self.determine_min_move(min_states)


    def determine_min_move(self, min_states):
        movement, score, board = min(min_states)
        return score, board


    def search_states(self, movement, board, total_score):
        total_score += board.play_round(movement)
        return total_score, board.board

    @staticmethod
    def choose_state(states):
        movement, score = max(states)
        return movement

    def max_search(self, current_score, updated_board):
        max_states = []
        for x in self.moves:
            new_board = copy.deepcopy(updated_board)
            current_board = Board(new_board)
            score = current_board.play_round(x)
            next_score = score + current_score
            max_states.append((next_score, x))
        return self.determine_max_move(max_states)

    def determine_max_move(self, max_states):
        score, movement = max(max_states)
        return score, movement

    def write_output(self, file_name, total_score: int):
        pass
