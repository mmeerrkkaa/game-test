from random import randint

SIZE = 10

mapss = []

[mapss.append(["#"] * SIZE) for i in range(SIZE)]


class Player:
	def __init__(self):
		self.maps = mapss.copy()
		self.coord = [[int(len(self.maps)//2), int(len(self.maps)**2%2)]]
		self.coord.append([])
		self.score = 0
		Player.spawnfood(self)


	def spawnfood(self):

		while 1:
			x = randint(0, SIZE-1)
			y = randint(0, SIZE-1)
			if x != self.coord[0][0] and y != self.coord[0][1]:
				self.coord[1] = x,y

				break

	def isFood(self):
		if self.coord[1][0] == self.coord[0][0] and self.coord[1][1] == self.coord[0][1]:
			self.score += 1
			print(self.score)
			Player.spawnfood(self)


	def up(self):
		if self.coord[0][0] != 0:
			self.coord[0][0] -= 1
		else:
			print("Невозможный ход")

	def down(self):
		if self.coord[0][0] != SIZE-1:
			self.coord[0][0] += 1
		else:
			print("Невозможный ход")

	def left(self):
		if self.coord[0][1] != 0:
			self.coord[0][1] -= 1
		else:
			print("Невозможный ход")

	def right(self):
		if self.coord[0][1] != SIZE-1:
			self.coord[0][1] += 1
		else:
			print("Невозможный ход")

	def updatemap(self):
		self.maps = []
		[self.maps.append(["#"] * SIZE) for i in range(SIZE)]

		self.maps[self.coord[1][0]][self.coord[1][1]] = "F"
		self.maps[self.coord[0][0]][self.coord[0][1]] = "P"

	def printmap(self):
		Player.isFood(self)
		Player.updatemap(self)
		for i in self.maps:
			print(*i)
		print()


	def menu(self):
		while 1:
			a = int(input())

			if a == 1:
				player.up()
			elif a == 2:
				player.down()
			elif a == 3:
				player.left()
			else:
				player.right()

			player.printmap()

player = Player()
player.printmap()
player.menu()
