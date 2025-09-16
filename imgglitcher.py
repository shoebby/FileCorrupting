import random

for y in range(9):
    with open('mosh/mosh.gif', "rb") as f:
        b = bytearray(f.read())

    for x in range(random.randint(100,1000)):
        b[random.randint(0,len(b)-1)] = random.randint(0,1)

    with open(f'mosh/mosh{y+1}.gif', "wb") as f:
        f.write(bytes(b))