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

colorMap = plt.get_cmap("cool")

save_path = "./png/"
soup = True


def init_array(is_soup: bool):
    arr = np.zeros((rounds, width))
    if is_soup:
        # Souping means init first row with random configuration of 0,1
        arr[0] = np.random.randint(0, 2, width)
    else:
        # Init array with a single set cell at the middle of the first row
        arr[0][width // 2] = 1
    return arr


# Given an Array, the wolframNr and the number of the row, calculate the specified row
def calc_row(arr, row_nr, wolfram_nr):
    if row_nr >= rounds:
        return

    old_row = arr[row_nr - 1]
    new_row = arr[row_nr]

    for i in range(width):

        # Identifies what cell configuration is in above row, sum ranges between 0 and 7 by design
        # Playing field is shaped like a cylinder, so the sides wrap around each other
        # Interprets the three cells in the row above as a binary digit
        if i == 0:
            bit = int(old_row[width - 1] * 4 + old_row[i] * 2 + old_row[i + 1])
        elif i == width - 1:
            bit = int(old_row[i - 1] * 4 + old_row[i] * 2 + old_row[0])
        else:
            bit = int(old_row[i - 1] * 4 + old_row[i] * 2 + old_row[i + 1])

        # If the wolframNr has a 1 at the bit specified by sum, then set the pixel in the next row
        if (wolfram_nr & (2 ** bit)) > 0:
            new_row[i] = 1
    # return new_row


# calculates array containing the image
def calculate_ca(wolfram_nr, is_soup=soup):
    arr = init_array(is_soup=is_soup)

    for i in range(1, rounds):
        calc_row(arr, i, wolfram_nr)

    return arr


# Save all created images as .png in a special folder called png
def save_all_ca():
    for wolframNr in range(256):
        arr = calculate_ca(wolframNr)
        plt.axis('off')
        plt.imsave(save_path + "ca_{}.png".format(wolframNr), arr, cmap=colorMap)
        print("Nr. {} done.".format(wolframNr))


# Shows a pyplot windows of the CA of the specified number
def show_ca(nr):
    arr = calculate_ca(nr)
    plt.imshow(arr, cmap=colorMap)
    plt.axis('off')
    plt.show()


def main():
    global width, rounds
    # width = int(input("Row width in pixels: "))
    # rounds = int(input("Number of iterations: "))
    number = int(input("Wolfram rule number: "))

    show_ca(number)
    # saveAllCA()


if __name__ == "__main__":
    main()
