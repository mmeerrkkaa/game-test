import sys

import pygame

from Player.networkx import Player

pygame.init()

class GamePygame:
	def __init__(self):
		self.player = Player()
		self.screen = pygame.display.set_mode((500, 500))
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont("Arial", 20)
		self.font2 = pygame.font.SysFont("Arial", 30)

	def game(self):
		while 1:
			self.clock.tick(10)
			self.screen.fill((0, 0, 0))

			maps = self.player.printmap()

			for i in range(len(maps[0])):
				for j in range(len(maps[0][i])):
					if maps[0][i][j] == "#":
						pygame.draw.rect(self.screen, (255, 255, 255), (j*50, i*50, 50, 50))
					elif maps[0][i][j] == "O":
						pygame.draw.rect(self.screen, (255, 255, 0), (j*50, i*50, 50, 50))
					elif maps[0][i][j] == "X":
						pygame.draw.rect(self.screen, (255, 0, 0), (j*50, i*50, 50, 50))
					elif maps[0][i][j] == "P":
						pygame.draw.rect(self.screen, (0, 255, 0), (j*50, i*50, 50, 50))

			text = self.font.render(f"Score: {self.player.score} | Ходов до еды - {maps[1]}", True, (0,0,0))

			self.screen.blit(text, (10, 10))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.player.up()
					elif event.key == pygame.K_DOWN:
						self.player.down()
					elif event.key == pygame.K_LEFT:
						self.player.left()
					elif event.key == pygame.K_RIGHT:
						self.player.right()

			pygame.display.flip()

if __name__ == "__main__":
	game = GamePygame()
	game.game()