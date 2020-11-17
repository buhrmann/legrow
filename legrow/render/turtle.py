import turtle


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
    """Basic turtle renderer."""

    def render(self, size=9, angle=90):

        self.screen.tracer(0, 0)
        for cmd in self.state:
            if cmd in ("F", "G"):
                self.pen.forward(size)
            elif cmd == "[":
                self.pen.push()
            elif cmd == "]":
                self.pen.pop()
            elif cmd == "+":
                self.pen.left(angle)
            elif cmd == "-":
                self.pen.right(angle)

        self.screen.update()
        self.screen.exitonclick()
