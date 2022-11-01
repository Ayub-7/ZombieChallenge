import unittest
import sys
sys.path.append("..")
from src import *

class testSimulator(unittest.TestCase):
    def test_move_right(self):
        testGrid = [[0, 0, 0], [0, 0, 0], [0, 'Z', 0]]
        simulator = zombieSimulator(testGrid, 3, (1,2), [], 'R', [["Zombie 0", [1,2]]])
        simulator.moveZombies()
        result = simulator.grid
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], [0, 0, 'Z']])

    def test_move_left(self):
        testGrid = [[0, 0, 0], [0, 0, 0], [0, 'Z', 0]]
        simulator = zombieSimulator(testGrid, 3, (1,2), [], 'L', [["Zombie 0", [1,2]]])
        simulator.moveZombies()
        result = simulator.grid
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], ['Z', 0, 0]])

    def test_move_up(self):
        testGrid = [[0, 0, 0], [0, 0, 0], [0, 'Z', 0]]
        simulator = zombieSimulator(testGrid, 3, (1,2), [], 'U', [["Zombie 0", [1,2]]])
        simulator.moveZombies()
        result = simulator.grid
        self.assertEqual(result, [[0, 0, 0], [0, 'Z', 0], [0, 0, 0]])

    def test_move_down(self):
        testGrid = [[0, 0, 0], [0, 'Z', 0], [0, 0, 0]]
        simulator = zombieSimulator(testGrid, 3, (1,1), [], 'D', [["Zombie 0", [1,1]]])
        simulator.moveZombies()
        result = simulator.grid
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], [0, 'Z', 0]])
       

    def test_move_off_side_edge(self):
        testGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 'Z']]
        simulator = zombieSimulator(testGrid, 3, (2,2), [], 'R', [["Zombie 0", [2,2]]])
        simulator.moveZombies()
        result = simulator.grid
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], ['Z', 0, 0]])

    def test_move_off_top_edge(self):
        testGrid = [['Z', 0, 0], [0, 0, 0], [0, 0, 0]]
        simulator = zombieSimulator(testGrid, 3, (0,0), [], 'U', [["Zombie 0", [0,0]]])
        simulator.moveZombies()
        result = simulator.grid
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], ['Z', 0, 0]])

    def test_move_sequence(self):
        testGrid = [['Z', 0, 0], [0, 0, 0], [0, 0, 0]]
        simulator = zombieSimulator(testGrid, 3, (0,0), [], 'RRDL', [["Zombie 0", [0,0]]])
        simulator.moveZombies()
        result = simulator.grid
        self.assertEqual(result, [[0, 0, 0], [0, 'Z', 0], [0, 0, 0]])

    def test_infect_creature(self):
        testGrid = [['Z', 0, 0], [0, 'C0', 0], [0, 0, 0]]
        simulator = zombieSimulator(testGrid, 3, (0,0), [(1,1)], 'DR', [["Zombie 0", [0,0]]])
        simulator.moveZombies()
        result = simulator.grid
        # new infected zombie follows sequence of previous zombie
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], [0, 0, 'Z']])
        # no more creatures alive
        self.assertEqual(simulator.creaturePosistions, [])
        #  infected creature added to zombie list
        self.assertEqual(simulator.zombieList, [["Zombie 0", [1,1]], ["Zombie 1", [2,2]]])
