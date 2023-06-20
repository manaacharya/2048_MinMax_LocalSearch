"""
Author: Manasa Acharya
Date: 11/04/2022
Class: CPSC 5610 AI - Milestone project
This is the board class, to create the board for 2048 and implement its moves. It is the board class from my Milestone 1
with additions. Now adds a random 2 or 4 at any open spot. Also adds 2 random 2's to the board to start the game.
"""
import random


class Board:

    def __init__(self, board):
        self.board = board
        self.empty_space = self.count_empty_spaces()

    def direction(self, direction):
        if direction == 'U':
            return self.up()
        if direction == 'D':
            return self.down()
        if direction == "R":
            return self.right()
        if direction == 'L':
            return self.left()

    # moves board, resets and adds random 2
    def play_round(self, direction):
        x = self.direction(direction)
        self.empty_space = self.count_empty_spaces()
        return x

    def up(self):
        score = 0
        # combine any same numbers starting at row 0
        for i in range(1, 4):
            for j in range(0, 4):
                if self.board[i - 1][j] == self.board[i][j]:
                    score = score + self.board[i - 1][j] * 2
                    self.board[i - 1][j] = self.board[i - 1][j] * 2
                    self.board[i][j] = 0
        self.reset_up()
        return score

    def down(self):
        score = 0
        # combine any same numbers starting at row 3
        for i in reversed(range(1, 4)):
            for j in range(0, 4):
                if self.board[i][j] == self.board[i - 1][j]:
                    score = score + self.board[i][j] * 2
                    self.board[i][j] = self.board[i][j] * 2
                    self.board[i - 1][j] = 0
        self.reset_down()
        return score

    def right(self):
        score = 0
        # combine any same number starting with column 3
        for i in range(0, 4):
            for j in reversed(range(1, 4)):
                if self.board[i][j] == self.board[i][j - 1]:
                    score = score + self.board[i][j] * 2
                    self.board[i][j] = self.board[i][j] * 2
                    self.board[i][j - 1] = 0
        self.reset_right()
        return score

    def left(self):
        score = 0
        # combine any same number starting with column 0
        for i in range(0, 4):
            for j in range(1, 4):
                if self.board[i][j - 1] == self.board[i][j]:
                    score = score + self.board[i][j - 1] * 2
                    self.board[i][j - 1] = self.board[i][j - 1] * 2
                    self.board[i][j] = 0
        self.reset_left()
        return score

    def reset_up(self):
        for x in range(0, 3):
            for i in range(x + 1, 4):
                for j in range(0, 4):
                    if 0 in self.board[x]:
                        if self.board[x][j] == 0 and self.board[i][j] != 0:
                            self.board[x][j] = self.board[i][j]
                            self.board[i][j] = 0

    def reset_down(self):
        for x in reversed(range(1, 4)):
            for i in reversed(range(0, x)):
                for j in range(0, 4):
                    if 0 in self.board[x]:
                        if self.board[x][j] == 0 and self.board[i][j] != 0:
                            self.board[x][j] = self.board[i][j]
                            self.board[i][j] = 0

    def reset_left(self):
        for x in range(0, 3):
            for i in range(0, 4):
                for j in range(x + 1, 4):
                    if self.board[i][x] == 0 and self.board[i][j] != 0:
                        self.board[i][x] = self.board[i][j]
                        self.board[i][j] = 0

    def reset_right(self):
        for x in reversed(range(1, 4)):
            for i in range(0, 4):
                for j in reversed(range(0, x)):
                    if self.board[i][x] == 0 and self.board[i][j] != 0:
                        self.board[i][x] = self.board[i][j]
                        self.board[i][j] = 0

    # choose a random row & check for 0. If yes, place 2 or 4 in that spot
    def add_two_or_four(self):
        row = self.choose_random_row()
        new_int = self.choose_4_or_2()
        done = False
        counter = 0
        while done is False or counter == 3:
            if 0 in self.board[row]:
                for i in range(0, 4):
                    if self.board[row][i] == 0:
                        self.board[row][i] = new_int
                        break
                done = True
            else:
                row = self.choose_random_row()
                counter += 1

    def start_board(self):
        i = self.choose_random_row()
        j = self.choose_random_column()
        k = self.choose_random_row()
        l = self.choose_random_column()
        if self.board[i][j] == 0:
            self.board[i][j] = 2
        if self.board[k][l] == 0:
            self.board[k][l] = 2

    @staticmethod
    def choose_4_or_2():
        return random.choice([2, 4])

    @staticmethod
    def choose_random_row():
        return random.randint(0, 3)

    @staticmethod
    def choose_random_column():
        return random.randint(0, 3)

    def count_empty_spaces(self):
        counter = 0
        for i in range(0,4):
            for j in range(0,4):
                if self.board[i][j] == 0:
                    counter += 1
        return counter

