import unittest
import sys
sys.path.append("..")
from src import *

class testGrid(unittest.TestCase):
    def test_make_grid(self):
         result = set_grid.makeGrid(3)
         self.assertEqual(result, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_place_zombies_creatures(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        result = set_grid.placeZombiesAndCreatures(grid, [(1,1), (2,2), (1,0)], (2,1))
        self.assertEqual(result, [[0, 'C2', 0], [0, 'C0', 'Z'], [0, 0, 'C1']])