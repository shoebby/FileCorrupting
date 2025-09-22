# script that shoves bytes up one spot in the array!
# Make sure that the file type of the input and output match
# Frankenstein'd together by Alexandria van Eekelen

for y in range(1): #range = number of files
    with open('example.data', "rb") as f:
        b = bytearray(f.read())
        firstByte = b[0]

    for x in range(len(b)-1): #iterate through the entire byte array
        if x == len(b) - 1:
            b[x] = firstByte
            break
        else:
            n = x+1

        b[x] = b[n]

    with open(f'example{y+1}.data', "wb") as f:
        f.write(bytes(b))