# Implementation of Conway's Game of Life made with numpy and matplotlib

import numpy as np
from matplotlib import pyplot as plt, animation

rounds = 0
size = 100

world = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);#np.zeros((size, size))
figure = plt.figure()
image = plt.imshow(world, cmap='binary', vmin=0, vmax=1)


def updateWorld(n, world=world):
    nextWorld = world
    for i in range(size):
        for j in range(size):
            k = np.sum(world[i-1:i+2, j-1:j+2]) - world[i, j]#sumNeighborhood(i, j)

            if k == 3 and world[i][j] == 0:
                nextWorld[i][j] = 1
            if world[i][j] == 0 and (k < 2 or k > 4):
                nextWorld[i][j] = 0
            if world[i][j] == 1 and (2 <= k <= 3):
                nextWorld[i][j] = 0

    world = nextWorld
    image.set_data(world)
    return image


def sumNeighborhood(x, y):
    # The size x size matrix is torus-shapped,so the 'edge' cases need to be handled seperately
    # First check if the cell is in one of the quadrants
    if x == 0 and y == 0:#DONE
        sum = world[1][0] + world[0][1] + world[1][1] + world[size-1][size-1] + world[size-1][0] + world[size-1][1] + world[0][size-1] + world[1][size-1]
    elif x == size - 1 and y == size - 1:
        sum = world[1][0] + world[1][0] +world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0]
    elif x == 0 and y == size - 1:
        sum = world[1][0] + world[1][0] +world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0]
    elif x == size - 1 and y == 0:
        sum = world[1][0] + world[1][0] +world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0]
    else:
        #For cases that contain lies on just one edge
        if x == 0:
            sum = world[1][0] + world[1][0] +world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0]
        elif y == 0:
            sum = world[1][0] + world[1][0] +world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0]
        else: # 'Regular case' when it's on neither edge
            sum = world[1][0] + world[1][0] +world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0] + world[1][0]

    return sum



def main():
    anim = animation.FuncAnimation(figure, updateWorld, interval=20, blit=True)
    plt.show()


main()
