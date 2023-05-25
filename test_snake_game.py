# to run tests use this command in the terminal
# python3 -m unittest test_snake_game.py

import unittest
import pygame

#target = __import__("main.py")
#gameLoop = target.gameLoop
from main import gameLoop

class TestSnakeGame(unittest.TestCase):
    def test_gameLoop(self):
        # Initialize Pygame
        pygame.init()

        # Set up the game window
        dis_width = 600
        dis_height = 400
        dis = pygame.display.set_mode((dis_width, dis_height))

        # Call the gameLoop function
        gameLoop()

        # Verify that the game window has been closed
        self.assertEqual(pygame.display.get_init(), False)

if __name__ == '__main__':
    unittest.main()