import turtle
class Player:
    def __init__(self):
        self.player_dx = 15
        self.player = turtle.Turtle()
        self.player.shape('imagem/player.gif')
        self.player.up()
        self.player.speed(0)
        self.player.setposition(0, -200)
        self.player.setheading(90)

    def move_left(self):
        x = self.player.xcor() - self.player_dx
        if x < -190:
            x = -190
        self.player.setx(x)

    def move_right(self):
        x = self.player.xcor() + self.player_dx
        if x > 190:
            x = 190
        self.player.setx(x)
