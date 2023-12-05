# Import modules
import turtle
import time
import random
import winsound

# Functions
player_dx = 15

def move_left():
    x = player.xcor() - player_dx
    if x < -190:
        x = -190
    player.setx(x)

def move_right():
    x = player.xcor() + player_dx
    if x > 190:
        x = 190
    player.setx(x) 


# set up window
wn = turtle.Screen()
#wn.setup(width = 600,height = 600)
wn.bgcolor('black')
wn.bgpic("imagem/fundo.gif") 
wn.title("Space invader")

# register shapes
turtle.register_shape('imagem/invader.gif')
turtle.register_shape('imagem/player.gif')

border = turtle.Turtle()
border.speed(0) 
border.color('black')
border.up()
border.setposition(-300,-300)
border.down()
border.pensize(4)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

score = 0

# Draw score board
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('red')
score_pen.up()
score_pen.setposition(-290, 270)
score_pen.write('SCORE: %s' % score, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.shape('imagem/player.gif')
player.up()
player.speed(0)
player.setposition(0,-200)
player.setheading(90)

# Create player's bullet​
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.up()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

firespeed = 40
playerspeed = 15
fire_on = False
x_fire = 0
y_fire = 0

def update_score(points=1):
    global score
    score += points
    scorestring = "SCORE: %s" % score
    score_pen.clear()
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


# create invader turtle
numbers_of_invaders = 5
invaders = []

for i in range(numbers_of_invaders):
    invaders.append(turtle.Turtle())

for enemy in invaders:
    enemy.shape("imagem/invader.gif")
    enemy.penup()
    enemy.speed(0)
    pos_x = random.randint(-200, 200)
    pos_y = random.randint(100, 250)
    enemy.setposition(pos_x, pos_y)

enemy.hideturtle()

def move_fire():
    global fire_on, bullet
    if not fire_on:
        fire_on = True
        bullet.showturtle()
        bullet.setposition(player.xcor(), -180)  # Ajuste aqui para seguir o jogador
        y_fire = bullet.ycor()
        while y_fire < 300:
            for inimigo in invaders:
                x_ini = inimigo.xcor()
                y_ini = inimigo.ycor()
                if bullet.distance(inimigo) < 20:
                    inimigo.setx(random.randint(max(-280, x_ini - 20), min(280, x_ini + 20)))
                    inimigo.sety(random.randint(100, 250))
                    y_fire = 400
                    update_score()
                    # Atualizar pontuação ou fazer outras ações aqui
                    break
            y_fire += firespeed
            bullet.sety(y_fire)

        bullet.hideturtle()
        fire_on = False

    #bullet.hideturtle()
    #bullet.sety(-185)
    #fire_on = False
    #bullet.setx(player.xcor())
    #bullet.showturtle()

#invader = turtle.Turtle()
#invader.shape('imagem/invader.gif')
#invader.up()
#invader.speed(0)
#invader.setposition(-180,180)

# Create keyboard binding
turtle.listen()
turtle.onkey(move_left,'Left')
turtle.onkey(move_right,'Right')
turtle.onkey(move_fire,'space')

def init_pos():
    x_positions = []
    y_positions = []
    for pos_invaders in invaders:
        x_position = pos_invaders.xcor()
        y_position = pos_invaders.ycor()
        x_positions.append(x_position)
        y_positions.append(y_position)

    left_pos = min(x_positions)
    right_pos = max(x_positions)
    down_pos = min(y_positions)

    left_id = x_positions.index(left_pos)
    right_id = x_positions.index(right_pos)
    down_id = y_positions.index(down_pos)

    return left_id, right_id, down_id

left_index, right_index, down_index = init_pos()

speedinvaders = 10
direction = "left"

while True:
    if direction == "left":
        x_left = invaders[left_index].xcor()
        y = invaders[left_index].ycor()
        if x_left >= -280:
            for pos_invaders in invaders:
                position = pos_invaders.xcor()
                position -= speedinvaders
                pos_invaders.setx(position)
            x_left -= speedinvaders
        else:
            y -= 40
            direction = "right"
            for pos_invaders in invaders:
                position = pos_invaders.ycor()
                position -= 40
                pos_invaders.sety(position)
    elif direction == "right":
        x_right = invaders[right_index].xcor()
        if x_right < 280:
            for pos_invaders in invaders:
                position = pos_invaders.xcor()
                position += speedinvaders
                pos_invaders.setx(position)
            x_right += speedinvaders
        else:
            y -= 40
            direction = "left"
            for pos_invaders in invaders:
                position = pos_invaders.ycor()
                position -= 40
                pos_invaders.sety(position)

    y_down = invaders[down_index].ycor()
    if y_down <= -280:
        break
    
    for inimigo in invaders:
        if inimigo.ycor() < player.ycor() + 20 and inimigo.ycor() > player.ycor() - 20 and inimigo.xcor() < player.xcor() + 20 and inimigo.xcor() > player.xcor() - 20:
            # Se sim, exibir "GAME OVER"
            game_over = turtle.Turtle()
            game_over.speed(0)
            game_over.color("red")
            game_over.penup()
            game_over.setposition(0, 0)
            game_over.write("GAME OVER", False, align="center", font=("Arial", 30, "normal"))
            game_over.hideturtle()
            turtle.done()

