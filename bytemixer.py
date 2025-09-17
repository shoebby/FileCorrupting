# script that shuffles random bytes!

import random

for y in range(9): #range = number of files
    with open('example.bmp', "rb") as f:
        b = bytearray(f.read())

    for x in range(5000): #range = number of bytes shuffled
        b[random.randint(0,len(b)-1)] = random.randint(0,255)

    with open(f'example{y+1}.bmp', "wb") as f:
        f.write(bytes(b))