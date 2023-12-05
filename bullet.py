import turtle
import random
class Bullet:
    def __init__(self, game):
        self.game = game
        self.firespeed = 40
        self.bullet = turtle.Turtle()
        self.bullet.color('yellow')
        self.bullet.shape('triangle')
        self.bullet.up()
        self.bullet.speed(0)
        self.bullet.setheading(90)
        self.bullet.shapesize(0.5, 0.5)
        self.bullet.hideturtle()
        self.fire_on = False
        self.x_fire = 0
        self.y_fire = 0

    def move_fire(self):
        global fire_on, bullet
        if not self.fire_on:
            fire_on = True
            self.bullet.showturtle()
            self.bullet.setposition(self.game.player.player.xcor(), -180)  # Ajuste aqui para seguir o jogador
            y_fire = self.bullet.ycor()

            while y_fire < 300:
                for inimigo in self.game.invaders:
                    x_ini = inimigo.xcor()
                    y_ini = inimigo.ycor()
                    if self.bullet.distance(inimigo.invader) < 20 and y_ini > -200:
                        inimigo.setx(random.randint(max(-280, x_ini - 20), min(280, x_ini + 20)))
                        inimigo.sety(random.randint(100, 250))
                        y_fire = 400
                        self.game.update_score()
                        
                        break
                y_fire += self.firespeed
                self.bullet.sety(y_fire)
            self.bullet.hideturtle()
            fire_on = False