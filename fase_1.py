import turtle
import time
import random
from game import Game
#firespeed = 40
#playerspeed = 15
#fire_on = False
#x_fire = 0
#y_fire = 0

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

def main(game_instance):
    game = Game()

    turtle.listen()
    turtle.onkey(game.player.move_left, 'Left')
    turtle.onkey(game.player.move_right, 'Right')
    turtle.onkey(game.bullet.move_fire, 'space')

    left_index, right_index, down_index = game.init_pos()

    speedinvaders = 5
    direction = "left"

    while True:
        if direction == "left":
            x_left = game.invaders[left_index].xcor()
            y = game.invaders[left_index].ycor()
            if x_left >= -280:
                for pos_invaders in game.invaders:
                    position = pos_invaders.xcor()
                    position -= speedinvaders
                    pos_invaders.setx(position)
                x_left -= speedinvaders
            else:
                y -= 40
                direction = "right"
                for pos_invaders in game.invaders:
                    position = pos_invaders.ycor()
                    position -= 40
                    pos_invaders.sety(position)
        elif direction == "right":
            x_right = game.invaders[right_index].xcor()
            if x_right < 280:
                for pos_invaders in game.invaders:
                    position = pos_invaders.xcor()
                    position += speedinvaders
                    pos_invaders.setx(position)
                x_right += speedinvaders
            else:
                y -= 40
                direction = "left"
                for pos_invaders in game.invaders:
                    position = pos_invaders.ycor()
                    position -= 40
                    pos_invaders.sety(position)

        y_down = game.invaders[down_index].ycor()
        if y_down <= -280:
            break

        for inimigo in game.invaders:
            if (
                inimigo.ycor() < game.player.player.ycor() + 20
                and inimigo.ycor() > game.player.player.ycor() - 20
                and inimigo.xcor() < game.player.player.xcor() + 20
                and inimigo.xcor() > game.player.player.xcor() - 20
            ):
                game_over = turtle.Turtle()
                game_over.speed(0)
                game_over.color("red")
                game_over.penup()
                game_over.setposition(0, 0)
                game_over.write("GAME OVER", False, align="center", font=("Arial", 30, "normal"))
                game_over.hideturtle()
                turtle.done()

if __name__ == "__main__":
    game_instance = None  # Substitua isso pela instância real de Game
    main(game_instance)
