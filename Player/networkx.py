from random import randint
import networkx as nx

G = nx.Graph()


SIZE = 10

mapss = []

[mapss.append(["#"] * SIZE) for _ in range(SIZE)]


class Player:
	def __init__(self):
		self.maps = mapss.copy()
		self.coord = [[int(len(self.maps)//2), int(len(self.maps)**2%2)], []]
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
			return True
		return False

	def down(self):
		if self.coord[0][0] != SIZE-1:
			self.coord[0][0] += 1
			return True
		return False

	def left(self):
		if self.coord[0][1] != 0:
			self.coord[0][1] -= 1
			return True
		return False

	def right(self):
		if self.coord[0][1] != SIZE-1:
			self.coord[0][1] += 1
			return True
		return False

	def updatemap(self):
		self.maps = []
		[self.maps.append(["#"] * SIZE) for _ in range(SIZE)]

		G = nx.grid_2d_graph(SIZE,SIZE)
		moves_before_food = (len(nx.bidirectional_shortest_path(G, source=(self.coord[0][0], (self.coord[0][1])), target=(self.coord[1][0], (self.coord[1][0])))) - 1)

		self.maps[self.coord[1][0]][self.coord[1][1]] = "F"
		self.maps[self.coord[0][0]][self.coord[0][1]] = "P"

		return moves_before_food

	def printmap(self):
		Player.isFood(self)
		moves_before_food = Player.updatemap(self)
		return [self.maps, moves_before_food]

