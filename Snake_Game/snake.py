from turtle import Turtle, Screen

# Make this a constant, so you don't have to dig thru code
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    # This init determines what happens when you initialize the Snake class to create an object
    def __init__(self):
        # Create a new attribute that has the list
        # Make sure to reference self when working within class
        self.snake_chain = []
        self.screen = Screen()
        # Create a method that creates the snake
        self.create_snake()
        self.head = self.snake_chain[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
        self.screen.update()

    # Whenever you do something to the object, reference with self.attribute

    def add_segment(self, position):
        x_pos = 0
        snake = Turtle(shape="square")  # Can specify shape when create Turtle
        snake.penup()
        snake.setposition(x_pos, 0)  # You can also create a list with positions and use goto(position)
        snake.color("white")
        x_pos -= 20
        self.snake_chain.append(snake)

    def extend(self):
        self.add_segment(self.snake_chain[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_chain) - 1, 0, -1):
            position = self.snake_chain[seg_num - 1].position()
            self.snake_chain[seg_num].setposition(position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
