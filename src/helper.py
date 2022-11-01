# Converts tuple strings to tuples
def tokenizeCreatures(initialCreatures):
    creaturesList = initialCreatures.split(" ")
    creatures = [eval(ele) for ele in creaturesList]
    return creatures

# Prints zombie positions
def printZombies(zombieList):
    zombieString = ''
    for i in zombieList:
        zombieString += str(i[1]) + " "
    return zombieString