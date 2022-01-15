#!C:\Users\yangm\Anaconda3\python.exe
import os
from PIL import Image
import numpy as np

'''image = Image.open('textures/test_map.png')

image = image.resize((6000,6000))

image.save('textures/test_map_sm.png','PNG')'''


image = Image.new('RGBA',(400,400))

array = np.asarray(image)

for i in range(400):
    for j in range(400):
        a = abs(1-min((i/200-1)**2+(j/200-1)**2,1))
        array[i,j] += np.array((255,255,255,int(round(a*255,0))),dtype='uint8')

image = Image.fromarray(array)

image.save('textures/glow_circle.png','PNG')


image = Image.new('RGBA',(400,400))

array = np.asarray(image)

for i in range(400):
    for j in range(400):
        a = 1-abs(j-200)/200
        array[i,j] += np.array((255,255,255,int(round(a*255,0))),dtype='uint8')

image = Image.fromarray(array)

image.save('textures/glow_wall.png','PNG')