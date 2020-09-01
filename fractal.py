import numpy as np
import matplotlib.pyplot as plt

#Constants
MAX_ITER = 25
WIDTH = 400
HEIGHT = 400
RE_START = -2
RE_END = 2
IM_START = -1.5
IM_END = 1.5

#c = complex(-0.7269, 0.1889)    #c = complex(-0.7269, 0.1889), complex(-0.8, 0.156), complex(-0.4, 0.6), complex(0.285, 0.01)

def julia(c:complex, z0 : complex, thresh:int = 3) -> int:
    z = z0
    counter = 0

    while(abs(z) <= thresh and counter < MAX_ITER):
        z = (z * z) + c
        counter += 1

    if counter == MAX_ITER:
        return MAX_ITER * 2
    return counter

def mandelbrot(c:complex, thresh:int = 2) -> int:
    z = c
    counter = 0

    while counter <  MAX_ITER and abs(z) < thresh:
        z = (z * z) + c        # Z_(n) = (Z_(n-1))^2 + c
        counter += 1
    return counter

def drawJulia(c):
    img=np.full((WIDTH,HEIGHT), 0)
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            z0 = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            m = julia(c, z0)    # Compute the number of iterations
            img[y][x] = m
    return img

def drawMandelbrot():
    img=np.full((WIDTH,HEIGHT), 0)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            z = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            it = mandelbrot(z, thresh = 2)
            img[y][x] = 255 - it
    return img

def main():
    colorMap = plt.get_cmap("Spectral")
    #img = drawMandelbrot()
    img = drawJulia(complex(-0.7269, 0.1889))
    plt.imshow(img, cmap = colorMap)
    plt.show()

def bunchOJulia():
    colorMap = plt.get_cmap("Spectral")
    for i in range(0,20):
        for j in range(0,20):
            comp = complex(i*0.05, j*0.05)
            img = drawJulia(comp)
            plt.imsave("./png/julia_{}_{}.png".format(i,j), img, cmap = colorMap )

#main()
#bunchOJulia()
