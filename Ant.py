import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random as rand
import math


ON = 255
OFF = 0
ANTS = 20
states = [ON, OFF]
N = 100
ants = []
for i in range(0,ANTS):
    ant = {'x': rand.randrange(0, 100), 'y': rand.randrange(0, 100), 'orientation': [1, 0]}
    ants.append(ant)
truegrid = np.random.choice(states, N*N, p=[0.01,0.99]).reshape(N, N)


def update(data):
    LEFT = False
    RIGHT = True
    global truegrid
    grid = truegrid.copy()
    def turn(direction, orientation):
        LeftFrom = [[1,0],[0,1],[-1,0],[0,-1]]
        LeftTo = [[0,1],[-1,0], [0,-1],[1,0]]
        print "        Direction : " + str(direction)
        if direction == LEFT:
            index = LeftFrom.index(orientation)
            return LeftTo[index]
        else:
            index = LeftTo.index(orientation)
            return LeftFrom[index]




    for ant in ants:
        turnLeft = False
        print "     Grid: " + str(grid[ant['x'], ant['y']])

        if grid[ant['x'], ant['y']] == ON:
            grid[ant['x'], ant['y']] = OFF
        else:
            turnLeft = True
            grid[ant['x'], ant['y']] = ON

        ant['orientation'] = turn(turnLeft, ant['orientation'])
        ant['x'] += ant['orientation'][0]
        ant['y'] += ant['orientation'][1]

        if(ant['x'] > N-1):
            ant['x'] = 0
        if(ant['y'] > N-1):
            ant['y'] = 0
        if(ant['x'] < 0):
            ant['x'] = N-1
        if(ant['y'] < 0):
            ant['y'] = N-1


    mat.set_data(grid)
    truegrid = grid
    return [mat]


fig, ax = plt.subplots()
mat = ax.matshow(truegrid)
ani = anim.FuncAnimation(fig, update, interval=150,
                              save_count=150)
plt.show()





