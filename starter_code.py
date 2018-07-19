#!/usr/bin/env python3

import random
import sys

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass

    def __str__(self):
        return self.name

class RandomPlayer(Player):
    def move(self):
        return moves[random.randint(0, 2)]

class HumanPlayer(Player):
    def move(self):
        m = input("What would you like to throw?")
        while m not in moves:
            if m.lower() == 'z':
                print("Thanks for playing!")
                sys.exit(0)
            m = input("Please enter a valid throw: rock, paper, scissors, or z.")

        return m

class ReflectPlayer(Player):
    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move

class RepeatPlayer(Player):
    def move(self):
        try:
            return self.my_move
        except AttributeError:
            # throw a random with the very first move
            return moves[random.randint(0, 2)]

    def learn(self, my_move, their_move):
        self.my_move = my_move

class CyclePlayer(Player):
    def move(self):
        try:
            # get the next move
            return moves[(moves.index(self.my_move) + 1) % 3]
        except AttributeError:
            # throw a random with the very first move
            return moves[random.randint(0, 2)]
    
    def learn(self, my_move, their_move):
        self.my_move = my_move

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))            


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_of_p1 = 0
        self.score_of_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"The {self.p2} throw {move2}")
        if beats(move1, move2):
            self.score_of_p1 += 1
            print(f"{self.p1} won!")
        elif beats(move2, move1):
            self.score_of_p2 += 1
            print(f"{self.p2} won!")
        else:
            print("It's a tie!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(4):
            print(f"Round {round}:")
            self.play_round()

        # the final score
        print(f"{self.p1} get {self.score_of_p1}. {self.p2} get {self.score_of_p2}")
        if self.score_of_p1 > self.score_of_p2:
            print(f"{self.p1} won the game!")
        elif self.score_of_p1 < self.score_of_p2:
            print(f"{self.p2} won the game!")
        else:
            try_again = input("It's a tie! Do you want to try again?[yes|no]")
            if try_again.lower() == "yes":
                self.play_game() # use a recursion to try again



if __name__ == '__main__':
    mode = input("""
Here are the rules of the game: scissor cuts paper,paper covers rock, and rock crushes scissors.
Play either "rock", "paper", or "scissors"
If you want to stop playing, enter a "z" anytime.
Who would you like to play with? Please enter "random", "reflect", "repeat", or "cycle"
    """)
    while True:
        if mode == "z":
            print("Thanks for playing!")
            sys.exit(0)
        elif mode.lower() == "random":
            game = Game(HumanPlayer("You"), RandomPlayer("Computer"))
            game.play_game()
            break
        elif mode.lower() == "reflect":
            game = Game(HumanPlayer("You"), ReflectPlayer("Computer"))
            game.play_game()
            break
        elif mode.lower() == "repeat":
            game = Game(HumanPlayer("You"), RepeatPlayer("Computer"))
            game.play_game()
            break
        elif mode.lower() == "cycle":
            game = Game(HumanPlayer("You"), CyclePlayer("Computer"))
            game.play_game()
            break
        else:
            mode = input('Please select a valid player, "random", "reflect", "repeat", or "cycle"')