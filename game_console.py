
from Player.networkx import Player

class GameConsole:
	def __init__(self):
		self.player = Player()

	def game(self):
		actions = {"1": self.player.up, "2": self.player.down, "3": self.player.left, "4": self.player.right}

		while 1:
			get_maps_data = self.player.printmap()
			# Сделать карту текстовой. maps[0] - list
			maps = "".join(" ".join(i) + "\n" for i in get_maps_data[0])
			get_maps_data[0] = maps

			print(get_maps_data[0] + "\n" + f"Score: {self.player.score} | Ходов до еды - {maps[1]}\n")

			action = input("Выберите действие: \n1) Вверх\n2) Вниз\n3) Влево\n4) Вправо\n: ")


			if not action.isdigit() or action not in actions:
				print("Неверный ввод!")
				continue

			if not actions[action]():
				print("Вы не можете туда пойти!")
				continue


if __name__ == "__main__":
	game = GameConsole()
	game.game()




