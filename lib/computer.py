from actor import Actor
import random
import ipdb

class Computer(Actor):
  

  def move(self, board):
    offensive_move = self.offense(board)
    defensive_move = self.defense(board)
    # determine if we need to make an offense move
    if offensive_move:
      return offensive_move
    # otherwise we need to defend
    elif defensive_move:
      return defensive_move
    # otherwise just make a move
    else:
      return self.random_move(board)

  def random_move(self, board):
    random_move = random.choice(board.available_cells())
    return str(random_move + 1)

  def offense(self, board):
    from game import Game
    
    for win_combo in Game.WIN_COMBINATIONS:
      win_index_1 = win_combo[0]
      win_index_2 = win_combo[1]
      win_index_3 = win_combo[2]

      token_1 = board.cells[win_index_1]
      token_2 = board.cells[win_index_2]
      token_3 = board.cells[win_index_3]

      if token_1 == self.token and token_2 == self.token and token_3 == " ":
        return str(win_index_3 + 1)
      elif token_1 == self.token and token_2 == " " and token_3 == self.token:
        return str(win_index_2 + 1)
      elif token_1 == " " and token_2 == self.token and token_3 == self.token:
        return str(win_index_1 + 1)
      
  def defense(self, board):
    enemy_token = "X" if self.token == "O" else "O"
    from game import Game
    
    for win_combo in Game.WIN_COMBINATIONS:
      win_index_1 = win_combo[0]
      win_index_2 = win_combo[1]
      win_index_3 = win_combo[2]

      token_1 = board.cells[win_index_1]
      token_2 = board.cells[win_index_2]
      token_3 = board.cells[win_index_3]

      if token_1 == enemy_token and token_2 == enemy_token and token_3 == " ":
        return str(win_index_3 + 1)
      elif token_1 == enemy_token and token_2 == " " and token_3 == enemy_token:
        return str(win_index_2 + 1)
      elif token_1 == " " and token_2 == enemy_token and token_3 == enemy_token:
        return str(win_index_1 + 1)