import numpy as np
import random as rand
import time
import os

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def draw(world, h, w):
    screen_clear()
    for row in world:
        print(row)

def evolotion(world, w, h):
    time.sleep(1)
    new = np.empty([h, w], dtype=object)
    for x in range(w):
        for y in range(h):
            lives = 0
            for xd in range(x-1, x+2):
                for yd in range(y-1, y+2):
                    if(world[(yd) % h][(xd) % w] == 'X'):
                        lives += 1

            if(world[y][x] == 'X'):
                lives -= 1

            if(lives == 3 and world[x][y] == ' '):
                new[x][y] = 'X'
            elif(lives == 2 or lives == 3 and world[x][y] == 'X'):
                new[x][y] = 'X'
            else:
                new[x][y] = ' '

    for x in range(h):
        for y in range(w):
            world[y][x] = new[y][x]

h = w = 15
world = np.empty([h, w], dtype=object)
for x in range(h):
    for y in range(w):
        world[x][y] = rand.uniform(0.0, 1.0) < 4/10
        if(world[x][y]):
            world[x][y] = 'X'
        else:
            world[x][y] = ' '

n = 0
while(True):
    draw(world, h, w)
    evolotion(world, h, w)
