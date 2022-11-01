# Zombie Apocalypse v4.6.1
Zombie Apocalypse v4.6.1 is an application that simulates a grid with zombies and creature. A set of movements is carried out by the zombie to infect the creatures
## Design
The application is split into two parts. One creates the grid and places the zombie and the creatures in their positions, the other takes care of the zombies movments on the board, creature infections and logging moves/infections. I have taken this approach because splitting the grid creation and simulation functionality allows the application to be easily evolved in the future. For example, if you wanted to add more obstacles to the grid it can be easily added in the grid creation side of the application, or if you wanted to add diagonal moves this can be added in the simulator side of the application. Setting it up in this way simplifies the application and gives it lots of room for growth.

## Highlight
One highlight of my solution which I think is great is they way I implemented my ```move``` function. It takes care of edge falls and regular movments all in one small easy to understand funtion. I was able to make this work by understanding that grid wise, ```Right``` and ```Down``` moves are identical and ```Up``` and ```Left``` moves are identical. This allowed me to create simple solution.
 

## Requirements
- Python3 or higher

## Example Input
```
What is the size of the Grid? 4
The initial position of the zombie? (3,1)
A list of initial positions of the creatures? (0,1) (1,2) (1,1)
A list of moves the zombies will make? RDRU
```

## Example Output
```
Zombie Positions:
[1, 1] [2, 1] [3, 2] [3, 1] 
Creature Positions:
[]
```

## How to run
```bash
cd src
python3 main.py
```
## How to run tests
```
python3 -m unittest discover -p 'test_*.py'
```