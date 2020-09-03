# Simple implementation of Steven Wolfram's Elementary Cellular Automata using numpy and matplotlib
# More info can be found here: https://en.wikipedia.org/wiki/Elementary_cellular_automaton
# Steven Wolfram invented a schema, to label number the 2^8 = 256 elementary CA. This schema is heavily used here
# Interesting rules to test are: 30, 50, 54, 60, 62, 90, 94, 102, 110, 126, 150, 158, 182, 188, 190, 220, 222

import numpy as np
import matplotlib.pyplot as plt

# By default it creates images of 600x800 pixels
# Parameters can also be adjusted at execution time through console prompts
width = 600
rounds = 800

colorMap = plt.get_cmap("binary")


# Given an Array, the wolframNr and the number of the row, calculate the specified row
def calcRow(arr, rowNr, wolframNr):
    oldRow = arr[rowNr - 1]
    newRow = [0 for i in range(width)]

    for i in range(width):

        # Identifies what cell configuration is in above row, sum ranges between 0 and 7 by design
        # Playing field is shaped like a cylinder, so the sides wrap around each other
        # Interprets the three cells in the row above as a binary digit
        if i == 0:
            bit = oldRow[width - 1] * 4 + oldRow[i] * 2 + oldRow[i + 1]
        elif i == width - 1:
            bit = oldRow[i - 1] * 4 + oldRow[i] * 2 + oldRow[0]
        else:
            bit = oldRow[i - 1] * 4 + oldRow[i] * 2 + oldRow[i + 1]

        # If the wolframNr has a 1 at the bit specified by sum, then set the pixel in the next row
        if wolframNr & (2 ** bit) > 0:
            newRow[i] = 1
    return newRow


# calculates array containing the image
def calculateCA(wolframNr):

    # Create Numpy Array
    arr = np.zeros((rounds, width))

    # Init array with a single set cell at the middle of the first row
    arr[0][width // 2] = 1

    # picture of cellular automaton with number '
    for i in range(1, rounds):
        arr[i] = calcRow(arr, i, wolframNr)

    return arr


# Save all created images as .png in a special subfolder called png
def saveAllCA():
    for wolframNr in range(256):
        arr = calculateCA(wolframNr)
        plt.axis('off')
        plt.imsave("./png/ca_{}.png".format(wolframNr), arr, cmap=colorMap)


# Shows a pyplot windows of the CA of the specified number
def showCA(nr):
    arr = calculateCA(nr)
    plt.imshow(arr, cmap=colorMap)
    plt.axis('off')
    plt.show()


def main():
    global width, rounds

    width = int(input("Row width in pixels: "))
    rounds = int(input("Number of iterations: "))
    number = int(input("Wolfram rule number: "))

    showCA(number)
    #saveAllCa()

main()
