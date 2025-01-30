class Player:
  def __init__(self, token):
    self.token = token


  def move(self):
    user_input = input("Type (1-9): ")
    return user_input