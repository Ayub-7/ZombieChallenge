class zombieSimulator:

    # init method or constructor
    def __init__(self, grid, n, zombiePos, creaturePosistions, movements, zombieList):
        self.grid = grid
        self.n = n
        self.zombiePos = zombiePos
        self.creaturePosistions = creaturePosistions
        self.movements = movements
        self.zombieList = zombieList

    def makeGrid(self):
        return [[0 for i in range(self.n)] for j in range(self.n)]
        

    def placeZombiesAndCreatures(self):
        self.grid = zombieSimulator.makeGrid(self)
        self.grid[self.zombiePos[1]][self.zombiePos[0]] = "Z"
        for i in range(len(self.creaturePosistions)):
            self.grid[self.creaturePosistions[i][1]][self.creaturePosistions[i][0]] = "C" + str(i)
        

    def moveZombies(self):
        currZombie = 0
        while currZombie <= len(self.zombieList):
            for move in self.movements:
                if move == "R":
                    zombieSimulator.move(self, "R", 0, currZombie)
                elif move == "L":
                    zombieSimulator.move(self, "L", 0, currZombie)
                elif move == "U":
                    zombieSimulator.move(self, "U", 1, currZombie)
                elif move == "D":
                    zombieSimulator.move(self, "D", 1, currZombie)
                else:
                    print("invalid move")
            currZombiePos = [self.zombiePos[0], self.zombiePos[1]]
            self.zombieList[currZombie][1] = currZombiePos
            if currZombie + 1 == len(self.zombieList):
                break
            else:
                currZombie += 1
                #set the zombiePos to the next infected zombie
                listPos = list(self.zombiePos)
                listPos = self.zombieList[currZombie][1]
                self.zombiePos = tuple(listPos)
                

    def move(self, direction, index, currZombie):
       # offTopEdge = 
        if (self.zombiePos[index] == self.n-1 and (direction == "R" or direction == "D")) or (self.zombiePos[index] == 0 and (direction == "U" or direction == "L")):
            self.grid[self.zombiePos[1]][self.zombiePos[0]] = 0
            listPos = list(self.zombiePos)
            if direction == "R" or direction == "D":
                listPos[index] -= self.n-1
            else:
                listPos[index] += self.n-1
            self.zombiePos = tuple(listPos)
            print("Zombie " + str(currZombie) + " moved to " + str(self.zombiePos))
            if "C" in str(self.grid[self.zombiePos[1]][self.zombiePos[0]]):
                zombieSimulator.infectCreature(self, currZombie)
            self.grid[self.zombiePos[1]][self.zombiePos[0]] = "Z"
        else:
            self.grid[self.zombiePos[1]][self.zombiePos[0]] = 0
            listPos = list(self.zombiePos)
            if direction == "R" or direction == "D":
                listPos[index] += 1
            else:
                listPos[index] -= 1
            self.zombiePos = tuple(listPos)
            print("Zombie " + str(currZombie) + " moved to " + str(self.zombiePos))
            if "C" in str(self.grid[self.zombiePos[1]][self.zombiePos[0]]):
                zombieSimulator.infectCreature(self, currZombie)
            self.grid[self.zombiePos[1]][self.zombiePos[0]] = "Z"

    def infectCreature(self, currZombie):
        print("Zombie " + str(currZombie) + " infected creature at " + str(self.zombiePos))
        newZombie = ["Zombie " + str(len(self.zombieList)), [self.zombiePos[0], self.zombiePos[1]]]
        self.zombieList.append(newZombie)
        self.creaturePosistions.remove(self.zombiePos)