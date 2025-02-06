from actor import Actor
import random
import ipdb

class Computer(Actor):
  

  def move(self, board):
    offensive_move = self.offense(board)
    # defensive_move = self.defense(board)
    # determine if we need to make an offense move
    if offensive_move:
      return offensive_move
    # otherwise we need to defend
    elif False:
      return defensive_move
    # otherwise just make a move
    else:
      return self.random_move(board)

  def random_move(self, board):
    random_move = random.choice(board.available_cells())
    return str(random_move + 1)

  def offense(self, board):
    from game import Game
    Game.WIN_COMBINATIONS