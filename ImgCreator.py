import png
import math
import winsound
import random
import numpy as np
from scipy.fft import fft2, ifft2
#from noise import snoise2
#from tqdm import tqdm


width = 400
height = 10

img = []

pinknoise = [max(0, round(math.sin(i*10)*90)) for i in range(width+height)]
print(pinknoise)
#print(max(0, 250 - round(pinknoise[1])))
#whitenoise = np.random.uniform(0,1,(256,256,3))
#fouriertransformed = np.fft.fftshift(fft2(whitenoise))
#pinktransformed = fouriertransformed / 24 ** 2
#pinknoise = ifft2(np.fft.ifftshift(pinktransformed)).real


for y in range(height):
    row = ()
    for x in range(width):
        row = row + (pinknoise[x+y], pinknoise[x], pinknoise[y])
    print(y)
    img.append(row)
with open('gradient6.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)
