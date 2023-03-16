from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Snake game')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
 
game_start = True
while game_start:
  screen.update()
  time.sleep(0.1)
  
  snake.move()

screen.exitonclick()