from turtle import Turtle
POSITIONS = [(0, 0), (0, -20),( 0, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.turtle_list = []
    self.create_snake()
    self.head = self.turtle_list[0]
    
  def create_snake(self):
    for turtle in POSITIONS:
      self.add_segement(turtle)
      
  def add_segement(self, position):
      my_turtle = Turtle(shape='square')
      my_turtle.penup()
      my_turtle.color('white')
      my_turtle.goto(position)
      self.turtle_list.append(my_turtle)
        
  def extend(self):
    self.add_segement(self.turtle_list[-1].position())

  def move(self):
    for turtle_num in range(len(self.turtle_list) -1 , 0, -1):
      x_cor = self.turtle_list[turtle_num -1].xcor() 
      y_cor = self.turtle_list[turtle_num -1].ycor()
      self.turtle_list[turtle_num].goto(x_cor, y_cor)
    
    self.head.forward(MOVE_DISTANCE)
     
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
    
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
    
  def left (self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
    
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
      