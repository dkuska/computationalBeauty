# Simple implementation of Mandelbrot and Julia Sets with numpy as matplotlib
# More info about the topic can be found here: https://en.wikipedia.org/wiki/Mandelbrot_set
# and here: https://en.wikipedia.org/wiki/Julia_set

import numpy as np
import matplotlib.pyplot as plt

# Constants
# Number of iterations used to check, whether the sequence is bounded
MAX_ITER = 50
# Size of the image created. Complexity is strongly determined both by size and MAX_ITER
WIDTH = 400
HEIGHT = 400

# sector of the complex plane, that is being displayed
RE_START = -2
RE_END = 2
IM_START = -1.5
IM_END = 1.5

# Julia sets require a constant c to be set, some interesting examples are: complex(-0.7269, 0.1889), complex(-0.8, 0.156), complex(-0.4, 0.6), complex(0.285, 0.01)
juliaConstant = complex(-0.7269, 0.1889)

# Colormap for displaying data in color
# For more info check reference here: https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
colorMap = plt.get_cmap("Spectral")


# Computes the amount of iteration steps needed, for the julia sequence at z0 for the constant c to diverge (i.e not be bounded by a given threshold anymore)
def julia(c: complex, z0: complex, thresh: int = 3) -> int:
    z = z0
    counter = 0

    while abs(z) <= thresh and counter < MAX_ITER:
        z = (z * z) + c
        counter += 1

    if counter == MAX_ITER:
        return MAX_ITER * 2
    return counter


# Given a point on the complex plane, calculates after how many steps, the sequence diverges
def mandelbrot(c: complex, thresh: int = 2) -> int:
    z = c
    counter = 0

    while counter < MAX_ITER and abs(z) < thresh:
        z = (z * z) + c  # Z_(n) = (Z_(n-1))^2 + c
        counter += 1
    return counter


# Returns a (WIDTH x HEIGHT) Array of integers in range of (1...MAX_ITER)
# The higher the value, the later does the julia series for constant c at position z0 diverge
def draw_julia(c):
    img = np.zeros((WIDTH, HEIGHT))
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            z = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))

            img[y][x] = julia(c, z)
    return img


# Returns a (WIDTH x HEIGHT) Array of integers in range of (1...MAX_ITER)
# The higher the value, the later does the mandelbrot sequence for the point diverge
def draw_mandelbrot():
    img = np.full((WIDTH, HEIGHT), 0)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Convert pixel coordinate to complex number
            z = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            img[y][x] = mandelbrot(z, thresh=2)
    return img


def main():
    img = draw_mandelbrot()
    # img = drawJulia(juliaConstant)
    plt.imshow(img, cmap=colorMap)
    plt.show()


main()
# bunchOJulia()
