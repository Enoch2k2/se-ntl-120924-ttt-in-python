class Board:
  def __init__(self):
    self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

  def display(self):
    print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
    print("-----------")
    print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
    print("-----------")
    print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")

  def update(self, input, token):
    idx = int(input) - 1
    self.cells[idx] = token

  def valid_move(self, input):
    try:
      idx = int(input) - 1
      if (idx >= 0 and idx < 9) and not self.position_taken(idx):
        return True
      else:
        return False
    except:
      return False
    
  def position_taken(self, idx):
    return True if self.cells[idx] != " " else False
  
  def full(self):
    return True if self.cells.count(" ") == 0 else False
  
  def available_cells(self):
    idx = 0
    available_cells = []
    for cell in self.cells:
      if cell == " ":
        available_cells.append(idx)
      idx += 1
    return available_cells