import unittest
import sys
sys.path.append("..")
from src import *

class testHelper(unittest.TestCase):
    def test_tokenize_creatures(self):
        input = '(1,2) (3,2) (1,1)'
        tokenizedCreatures = helper.tokenizeCreatures(input)
        expectedOutput = [(1,2), (3,2), (1,1)]
        self.assertEqual(tokenizedCreatures, expectedOutput)

    def test_print_zombies(self):
        mockZombieList = [['Zombie 0', [1, 1]], ['Zombie 1', [2, 1]], ['Zombie 2', [3, 2]], ['Zombie 3', [3, 1]]]
        zombieOutput = helper.printZombies(mockZombieList)
        expectedOutput = '[1, 1] [2, 1] [3, 2] [3, 1] '
        self.assertEqual(zombieOutput, expectedOutput)