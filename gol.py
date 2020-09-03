# Simple Implementation of Conway's Game of Life made with numpy and matplotlib
# Info can be found here: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

import numpy as np
from matplotlib import pyplot, animation

# size of the 2d playing field. keep in mind, that it's torus shaped
size = 100

# world is the playing field. it gets initialized with 0 or 1 at random
world = np.random.randint(0,2,(size,size))

figure = pyplot.figure()
image = pyplot.imshow(world, cmap='binary', vmin=0, vmax=1)

#function gets called repeatedly to update the playing field
def updateWorld(n):
    global world
    nextWorld = np.zeros((size, size))

    #Update each cell of the new world
    for i in range(size):
        for j in range(size):
            #calculates amount of neighbors of a given cell in a torus shaped world
            neighbors = (world[i, (j - 1) % size] + world[i, (j + 1) % size] +
                         world[(i - 1) % size, j] + world[(i + 1) % size, j] +
                         world[(i - 1) % size, (j - 1) % size] + world[(i - 1) % size, (j + 1) % size] +
                         world[(i + 1) % size, (j - 1) % size] + world[(i + 1) % size, (j + 1) % size])

            if world[i,j] == 1:
                if (neighbors < 2) or (neighbors > 3):
                    nextWorld[i, j] = 0
                else:
                    nextWorld[i, j] = 1
            else:
                if neighbors == 3:
                    nextWorld[i, j] = 1
                else:
                    nextWorld[i, j] = 0

    #Update world and animation with newly calculated data
    world = nextWorld
    image.set_data(world)

    return image


def main():
    #Create the figure in a matplotlib animation
    #Interval determines how often this graphics is updated, unit is milliseconds
    anim = animation.FuncAnimation(figure, updateWorld, interval=200)
    pyplot.axis('off')
    pyplot.show()


main()
