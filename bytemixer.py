# script that shuffles random bytes!
# Frankenstein'd together by Alexandria van Eekelen

import random

for y in range(1): #range = number of files
    with open('LCG/first.gif', "rb") as f:
        b = bytearray(f.read())

    for x in range(random.randint(20,100)): #range = number of bytes shuffled
        b[random.randint(0,len(b)-1)] = random.randint(0,255)

    with open(f'LCG/first{y+1}.gif', "wb") as f:
        f.write(bytes(b))
