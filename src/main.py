from zombie_simulator import *
import set_grid  
import helper  

# Sets up variables for simulator object
def setup(moveSequence, initialZombiePos, initialCreatures, gridSize):
    moves = [move.upper() for move in moveSequence]
    initialZombiePos = eval(initialZombiePos)
    initialCreatures = helper.tokenizeCreatures(initialCreatures)
    grid = set_grid.makeGrid(gridSize)
    return grid, initialCreatures, initialZombiePos, moves

# Retrieves user input and runs the simulation
def main():
    gridSize = int(input("What is the size of the Grid? "))
    initialZombiePos = input("The initial position of the zombie? ")
    initialCreatures = input("A list of initial positions of the creatures? ")
    moveSequence = input("A list of moves the zombies will make? ")
    grid, initialCreatures, initialZombiePos, moves = setup(moveSequence, initialZombiePos, initialCreatures, gridSize)
    filledGrid = set_grid.placeZombiesAndCreatures(grid, initialCreatures, initialZombiePos)
    simulator = zombieSimulator(filledGrid, gridSize, initialZombiePos, initialCreatures, moves, [["Zombie 0", list(initialZombiePos)]])
    simulator.moveZombies()
    print("Zombie Positions:")
    print(helper.printZombies(simulator.zombieList))
    print("Creature Positions:")
    print(simulator.creaturePosistions)

main()

