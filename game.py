import turtle
import random
from player import Player
from bullet import Bullet
from invader import Invader
class Game:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor('black')
        self.wn.bgpic("imagem/fundo.gif")
        self.wn.title("Space Invader")
        turtle.register_shape('imagem/invader.gif')
        turtle.register_shape('imagem/player.gif')

        self.border = turtle.Turtle()
        self.border.speed(0)
        self.border.color('black')
        self.border.up()
        self.border.setposition(-300, -300)
        self.border.down()
        self.border.pensize(4)
        for side in range(4):
            self.border.fd(600)
            self.border.lt(90)
        self.border.hideturtle()

        self.score = 0
        self.score_pen = turtle.Turtle()
        self.score_pen.speed(0)
        self.score_pen.color('red')
        self.score_pen.up()
        self.score_pen.setposition(-290, 270)
        self.score_pen.write('SCORE: %s' % self.score, align="left", font=("Arial", 14, "normal"))
        self.score_pen.hideturtle()
        self.player = Player()
        self.bullet = Bullet(self)
        self.invaders = [Invader() for _ in range(5)]

    def update_score(self, points=1):
        self.score += points
        scorestring = "SCORE: %s" % self.score
        self.score_pen.clear()
        self.score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    def init_pos(self):
        x_positions = [invader.xcor() for invader in self.invaders]
        y_positions = [invader.ycor() for invader in self.invaders]

        left_pos = min(x_positions)
        right_pos = max(x_positions)
        down_pos = min(y_positions)

        left_id = x_positions.index(left_pos)
        right_id = x_positions.index(right_pos)
        down_id = y_positions.index(down_pos)

        return left_id, right_id, down_id
