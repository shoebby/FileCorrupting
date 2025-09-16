import random

for y in range(1):
    with open('zeldacdi/zeldacdi.mp4', "rb") as f:
        b = bytearray(f.read())

    for x in range(250):
        b[random.randint(0,len(b)-1)] = random.randint(0,1)

    with open(f'zeldacdi/zeldacdi{y+1}.mp4', "wb") as f:
        f.write(bytes(b))