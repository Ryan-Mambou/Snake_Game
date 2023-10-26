from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # Notice it is placed after the creation of the snake
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape('square')
            new_turtle.color('white')
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(SNAKE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
