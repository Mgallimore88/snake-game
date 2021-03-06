# this code takes the raw output of the snake body and food array,
# and packages them into a format ready for sending to the raspberry pi

import numpy as np
import os


def output(body, food):
    # makes a numpy array containing n elements, 
    # first n-1 elements are body, the final element
    # is the food. 
    # Each element contains three numbers corresponding to x, y, z coordinates
    # in the range from 0 to res

    # convert food from p5.Vector to np.array
    np_food = np.array([food.x, food.y, 0])
    lights = np.append(body, food)
    lights = np.reshape(lights, (len(body)+1, 1, 3))

    # os.system('cls' if os.name == 'nt' else 'clear')
    print(lights)
    for light in lights:
        light = np.append(light, 1)
    # print(np_food)
