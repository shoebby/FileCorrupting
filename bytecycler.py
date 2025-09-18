# script that shoves bytes up one spot in the array!
# Make sure that the file type of the input and output match
# Frankenstein'd together by Alexandria van Eekelen

import random

for y in range(1): #range = number of files
    with open('rawdog/rawdog1.data', "rb") as f:
        b = bytearray(f.read())

    for x in range(len(b)-1):
        if x > len(b) - 1:
            n = 0
        else:
            n = x+1

        b[x] = b[n]

    with open(f'rawdog/rawdog2.data', "wb") as f:
        f.write(bytes(b))