import turtle
from collections import deque

from . import tki


class TRenderBase:
    """Basic window for rendering an LSystem with turtle graphics."""

    def __init__(self, speed=0):
        self.screen = turtle.Screen()
        self.pen = turtle.Turtle()
        self.pen.speed(speed)
        self.pen.hideturtle()
        self.screen.bgcolor("#fffef2")

    def draw(self, lsystem, size=9, angle=90):
        raise NotImplementedError


class TkRenderBase(tki.Frame):
    """A render window with scroll and zoom."""

    def __init__(self, root, w=800, h=800, speed=0):
        super().__init__(root, w, h)

        self.screen = turtle.TurtleScreen(self.canvas)
        self.pen = turtle.RawTurtle(self.screen)
        self.pen.speed(speed)
        self.pen.hideturtle()
        self.screen.bgcolor("#fffef2")


class TRender(TkRenderBase):
    """Basic turtle renderer. For debugging purposes mainly."""

    def draw(self, lsystem, size=9, angle=90):

        pen = self.pen
        stack = deque()
        self.screen.tracer(0, 0)

        for cmd in lsystem.state:
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

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.screen.update()
