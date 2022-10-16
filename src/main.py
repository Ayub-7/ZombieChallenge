from ZombieSimulator import *

def tokenizeCreatures(initialCreatures):
    creaturesList = initialCreatures.split(" ")
    creatures = [eval(ele) for ele in creaturesList]
    return creatures

def main():
    gridSize = int(input("What is the size of the Grid? "))
    initialZombiePos = input("The initial position of the zombie? ")
    initialCreatures = input("A list of initial positions of the creatures? ")
    moveSequence = input("A list of moves the zombies will make? ")
    moves = [move.upper() for move in moveSequence]
    initialZombiePos = eval(initialZombiePos)
    initialCreatures = tokenizeCreatures(initialCreatures)
    simulator = zombieSimulator([], gridSize, initialZombiePos, initialCreatures, moves, [["Zombie 0", list(initialZombiePos)]])
    simulator.placeZombiesAndCreatures()
    simulator.moveZombies()
    print("Zombie Positions:")
    print(simulator.zombieList)
    print("Creature Positions:")
    print(simulator.creaturePosistions)

main()

