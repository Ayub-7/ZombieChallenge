# Builds the grid based on dimension user inputs
def makeGrid(n):
        return [[0 for i in range(n)] for j in range(n)]

# Places zombie and creatures on the grid
def placeZombiesAndCreatures(grid, creaturePosistions, zombiePos):
    grid[zombiePos[1]][zombiePos[0]] = "Z"
    for i in range(len(creaturePosistions)):
        grid[creaturePosistions[i][1]][creaturePosistions[i][0]] = "C" + str(i)
    return grid