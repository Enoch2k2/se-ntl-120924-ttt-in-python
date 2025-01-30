from helpers import *
class Game:
  WIN_COMBINATIONS=(
    (0,1,2), # top horizontal row
    (3,4,5), # middle horizontal row
    (6,7,8), # bottom horizontal row
    (0,3,6), # left vertical row
    (1,4,7), # middle vertical row
    (2,5,8), # right vertical row
    (0,4,8), # top left to bottom right diagonal
    (2,4,6)  # top right to bottom left diagonal
  )

  def __init__(self, player_1, player_2, board):
    self.player_1 = player_1
    self.player_2 = player_2
    self.board = board

  def turn(self):
    clear()
    print(f"  Player {self.current_player().token}")
    print("============")
    line_space()
    self.board.display()
    line_space()
    user_input = self.current_player().move()
    if self.board.valid_move(user_input):
      self.board.update(user_input, self.current_player().token)
    else:
      clear()
      print("Incorrect Input... Please try again!")
      line_space()
      pause()
      self.turn()

  def current_player(self):
    return self.player_1 if self.turn_count() % 2 == 0 else self.player_2

  def turn_count(self):
    count_x = self.board.cells.count("X")
    count_o = self.board.cells.count("O")
    return count_x + count_o
  
  def won(self):
  #   WIN_COMBINATIONS=(
  #   (0,1,2), # top horizontal row
  #   (3,4,5), # middle horizontal row
  #   (6,7,8), # bottom horizontal row
  #   (0,3,6), # left vertical row
  #   (1,4,7), # middle vertical row
  #   (2,5,8), # right vertical row
  #   (0,4,8), # top left to bottom right diagonal
  #   (2,4,6)  # top right to bottom left diagonal
  # )
    for win_combo in Game.WIN_COMBINATIONS:
      win_idx_1 = win_combo[0] # win_combo is (3,4,5)
      win_idx_2 = win_combo[1]
      win_idx_3 = win_combo[2]

      token_1 = self.board.cells[win_idx_1]
      token_2 = self.board.cells[win_idx_2]
      token_3 = self.board.cells[win_idx_3]

      if token_1 == token_2 and token_2 == token_3 and token_1 != " ":
        return token_1
    
    return False

  
  def draw(self):
    # every position is taken and there isn't a winner
    return True if self.board.full() and not self.won() else False
  
  def over(self):
    return self.won() or self.draw()

  def play(self):
    while not self.over():
      self.turn()
    clear()
    self.board.display()
    line_space()
    winner = self.won()
    if winner:
      print(f'{winner} wins!')
    else:
      print("Cat's Game!")
    line_space()
    pause()
