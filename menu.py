import turtle
from pathlib import Path

from game import Game

def choose_difficulty(difficulty, game_instance):
    try:
        path = Path(__file__).parent / f"fase_{difficulty}.py"
        exec(path.read_text(), {"game_instance": game_instance})
    except FileNotFoundError:
        print(f"Fase {difficulty} não encontrada.")

def main_menu():
    game = turtle.Screen()
    game.bgcolor('black')
    game.bgpic("imagem/fundo.gif")
    game.title("Space Invader")

    # Restante do código para configurar a tela inicial

    def on_key_press(key):
        try:
            difficulty = int(key)
            choose_difficulty(difficulty, game)
        except ValueError:
            print("Por favor, digite um número válido.")

    turtle.listen()
    turtle.onkey(lambda: on_key_press(1), '1')
    turtle.onkey(lambda: on_key_press(2), '2')
    turtle.onkey(lambda: on_key_press(3), '3')

    turtle.mainloop()

if __name__ == "__main__":
    main_menu()
