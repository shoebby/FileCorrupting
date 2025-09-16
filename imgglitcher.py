import random

for y in range(9):
    with open('cuppystamp/cuppystamp.gif', "rb") as f:
        b = bytearray(f.read())

    for x in range(1000):
        b[random.randint(0,len(b))] = random.randint(0,9)

    with open(f'cuppystamp/cuppystamp{y+1}.gif', "wb") as f:
        f.write(bytes(b))