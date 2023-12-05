import turtle
from game import Game
def main():
    game = Game()

    turtle.listen()
    turtle.onkey(game.player.move_left, 'Left')
    turtle.onkey(game.player.move_right, 'Right')
    turtle.onkey(game.bullet.move_fire, 'space')

    left_index, right_index, down_index = game.init_pos()

    speedinvaders = 10
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
    main()