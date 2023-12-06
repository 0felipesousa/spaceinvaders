import turtle
import random
from main import main
class Invader:
    def __init__(self, game):
        self.invader = turtle.Turtle()
        self.invader.shape("imagem/invader.gif")
        self.invader.penup()
        self.invader.speed(0)
        pos_x = random.randint(-200, 200)
        pos_y = random.randint(100, 250)
        self.invader.setposition(pos_x, pos_y)
        self.adjust_parameters(game.level)
        
    def xcor(self):
        return self.invader.xcor()

    def ycor(self):
        return self.invader.ycor()

    def setx(self, x):
        self.invader.setx(x)

    def sety(self, y):
        self.invader.sety(y)

    def adjust_parameters(self, level):
        if level == 1:
            self.invader.speed(5)
            pass
        elif level == 2:
            # Ajustes para o nível normal
            pass
        elif level == 3:
            # Ajustes para o nível difícil
            pass
        # Adicione ajustes adicionais conforme necessário
