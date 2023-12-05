import turtle
import random
class Invader:
    def __init__(self):
        self.invader = turtle.Turtle()
        self.invader.shape("imagem/invader.gif")
        self.invader.penup()
        self.invader.speed(0)
        pos_x = random.randint(-200, 200)
        pos_y = random.randint(100, 250)
        self.invader.setposition(pos_x, pos_y)
        
    def xcor(self):
        return self.invader.xcor()

    def ycor(self):
        return self.invader.ycor()

    def setx(self, x):
        self.invader.setx(x)

    def sety(self, y):
        self.invader.sety(y)