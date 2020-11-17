import turtle
from collections import deque


class TRenderBase:
    """Base for rendering an LSystem with turtle graphics."""

    def __init__(self, lsystem, speed=0):
        self.state = lsystem.state
        self.screen = turtle.Screen()
        self.pen = turtle.Turtle()
        self.pen.speed(speed)
        self.pen.hideturtle()

    def render(self):
        raise NotImplementedError


class TRender(TRenderBase):
    """Basic turtle renderer. For debugging purposes mainly."""

    def render(self, size=9, angle=90):

        pen = self.pen
        stack = deque()
        self.screen.tracer(0, 0)

        for cmd in self.state:
            if cmd in ("F", "G"):
                pen.forward(size)
            if cmd == "J":
                pen.up()
                pen.forward(size)
                pen.down()
            elif cmd == "+":
                pen.left(angle)
            elif cmd == "-":
                pen.right(angle)
            elif cmd == "[":
                stack.append((pen.heading(), pen.position()))
            elif cmd == "]":
                heading, pos = stack.pop()
                pen.up()
                pen.setheading(heading)
                pen.setposition(pos)
                pen.down()

        self.screen.update()
        self.screen.exitonclick()
