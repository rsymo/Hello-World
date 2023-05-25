# run tests with:
# python -m unittest snake_game/test_snake_game.py

import unittest
from snake_game.snake_game import gameLoop

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_x1_change(self):
        self.game.x1_change = 10
        self.game.gameLoop()
        self.assertEqual(self.game.x1_change, 10)

    def test_y1_change(self):
        self.game.y1_change = 10
        self.game.gameLoop()
        self.assertEqual(self.game.y1_change, 10)

    def test_x1(self):
        self.game.x1 = 10
        self.game.gameLoop()
        self.assertEqual(self.game.x1, 10)

    def test_y1(self):
        self.game.y1 = 10
        self.game.gameLoop()
        self.assertEqual(self.game.y1, 10)

    def test_dis_width(self):
        self.game.dis_width = 10
        self.game.gameLoop()
        self.assertEqual(self.game.dis_width, 10)

    def test_dis_height(self):
        self.game.dis_height = 10
        self.game.gameLoop()
        self.assertEqual(self.game.dis_height, 10)

    def test_snake_block(self):
        self.game.snake_block = 10
        self.game.gameLoop()
        self.assertEqual(self.game.snake_block, 10)

    def test_snake_speed(self):
        self.game.snake_speed = 10
        self.game.gameLoop()
        self.assertEqual(self.game.snake_speed, 10)

    def test_snake_List(self):
        self.game.snake_List = 10
        self.game.gameLoop()
        self.assertEqual(self.game.snake_List, 10)

    def test_foodx(self):
        self.game.foodx = 10
        self.game.gameLoop()
        self.assertEqual(self.game.foodx, 10)

    def test_foody(self):
        self.game.foody = 10
        self.game.gameLoop()
        self.assertEqual(self.game.foody, 10)

    def test_snake_Head_position(self):
        self.game.snake_Head = 10
        self.game.gameLoop()
        self.assertEqual(self.game.snake_Head, 10)
    
if __name__ == '__main__':
    unittest.main()
