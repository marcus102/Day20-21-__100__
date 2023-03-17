from turtle import Turtle

ALIGNMENT  = 'center'
FONT = ('bold', 15, 'normal')

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.penup()
    self.goto(0, 275)
    self.color('white')
    self.hideturtle()
    self.update_score_board()
    
  
  def update_score_board(self):
    self.write(f'Score = {self.score}',  align= ALIGNMENT, font= FONT)
    
  def scores (self):
    self.clear()
    self.score += 1
    self.update_score_board()
    
  def game_over(self):
    self.goto(0, 0)
    self.write('GAME OVER',  align= ALIGNMENT, font= FONT)