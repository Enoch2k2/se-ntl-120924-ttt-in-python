from helpers import *
from player import Player
from computer import Computer
from game import Game
from board import Board

class Cli:
  def start(self):
    clear()
    print("Welcome to Tic Tac Toe!")
    line_space()
    pause()
    self.menu()

  def menu(self):
    clear()
    print("Please make a selection")
    print("===========================")
    print("Type '0' to play 0 players")
    print("Type '1' to play 1 player")
    print("Type '2' to play 2 players")
    print("Type 'exit' to exit program")
    print("===========================")
    self.menu_selection()

  def menu_selection(self):
    line_space()
    user_input = input("Input Here: ")
    if user_input == "0":
      clear()
      self.setup_zero_player_game()
      self.menu()
    elif user_input == "1":
      self.setup_one_player_game()
      self.menu()
    elif user_input == "2":
      self.setup_two_player_game()
      self.menu()
    elif user_input == "exit":
      clear()
      print("Exiting Program...See you again soon!")
      line_space()
      pause()
      clear()
      exit()
    else:
      clear()
      print("Incorrect Input, please try again...")
      line_space()
      pause()
      self.menu()

  def setup_zero_player_game(self):
    player_1 = Computer(token="X")
    player_2 = Computer(token="O")
    board = Board()
    game = Game(player_1=player_1, player_2=player_2, board=board)
    game.play()

  def setup_one_player_game(self):
    player_1 = Player(token="X")
    player_2 = Computer(token="O")
    board = Board()
    game = Game(player_1=player_1, player_2=player_2, board=board)
    game.play()

  def setup_two_player_game(self):
    player_1 = Player(token="X")
    player_2 = Player(token="O")
    board = Board()
    game = Game(player_1=player_1, player_2=player_2, board=board)
    game.play()