from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Snake game')
screen.tracer(0)

scoreboard = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
 
game_start = True
while game_start:
  screen.update()
  time.sleep(0.2)
  
  snake.move()
  
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.scores()
    
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
    scoreboard.game_over()
    game_start = False
    
  for element in snake.turtle_list[1:]:
    if snake.head.distance(element) < 10: 
        game_start = False
        scoreboard.game_over()   
    
screen.exitonclick()