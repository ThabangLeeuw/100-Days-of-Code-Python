from turtle import Turtle

# from main import segment

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__ (self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake (self):
        for i in STARTING_POSITION:
            self.addSegnment(i)

    def addSegnment(self, i):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(i)
        self.segments.append(new_segment)

    def extend(self):
        self.addSegnment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(900, 900)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





