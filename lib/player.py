from actor import Actor

class Player(Actor):

  def move(self, board):
    return input("Type (1-9): ")