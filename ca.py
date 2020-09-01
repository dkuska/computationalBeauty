import numpy as np
import matplotlib.pyplot as plt

width = 600
rounds = 800

def calcNextRow(arr, n, nr, width):
    oldRow = arr[n]
    newRow = [0 for i in range(width)]

    for i in range(width):

        #Identifies what cell configuration is in above row, sum ranges between 0 and 7 by design
        if i == 0:
            sum = oldRow[width-1]*4 + oldRow[i]*2 + oldRow[i+1]
        elif i == width - 1:
            sum = oldRow[i-1]*4 + oldRow[i]*2 + oldRow[0]
        else:
            sum = oldRow[i-1]*4 + oldRow[i]*2 + oldRow[i+1]

        if sum < 8: #This check shouldnt be necessary (As the array should consist of only 0 and 1, but it's there anyway :)
            if (nr & 2**sum) > 0 :
                newRow[i] = 1
    return newRow

def calculateCA(nr):
    # Create Numpy Array
    arr = np.full((rounds, width), 0)

    #Init array with starting state
    arr[0][width//2] = 1

    # picture of cellular automaton with number '
    for i in range(1, rounds):
            arr[i] = calcNextRow(arr, i-1, nr, width)

    return arr

def saveAllCA():
    for nr in range(256):
        arr = calculateCA(nr)

        #Call MatPlotLib to show and save Image
        colorMap = plt.get_cmap("binary")
        #plt.imshow(arr, cmap = colorMap)
        plt.axis('off')
        #plt.show()
        plt.imsave("./png/ca_{}.png".format(nr), arr, cmap = colorMap )

def showCA(nr):
    arr = calculateCA(nr)

    colorMap = plt.get_cmap("binary")
    plt.imshow(arr, cmap = colorMap)
    plt.axis('off')
    plt.show()

def main():

    #width = #int(input("Width: "))
    #rounds = #int(input("Number of rounds: "))
    number = 150#int(input("Rule number: "))

    saveAllCA()
    #showCA(number)

main()
