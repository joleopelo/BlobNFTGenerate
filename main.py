from PIL import Image
import os, glob

blob = []
coins = []
face = []
hat = []
sparkle = []

for filename in glob.glob('assets/blob*'):
    blob.append(Image.open(filename))

for filename in glob.glob('assets/coins*'):
    coins.append(Image.open(filename))

for filename in glob.glob('assets/face*'):
    face.append(Image.open(filename))

for filename in glob.glob('assets/hat*'):
    hat.append(Image.open(filename))

for filename in glob.glob('assets/sparkle*'):
    sparkle.append(Image.open(filename))

a = 0
b = 0
c = 0
d = 0
e = 0
n = 0

total_comb = len(blob) * len(coins) * len(face) * len(hat) * len(sparkle)

while n < total_comb:
    if e > (len(sparkle) - 1):
        d = d + 1
        e = 0
    if d > (len(hat) - 1):
        c = c + 1
        d = 0
        e = 0
    if c > (len(face) - 1):
        b = b + 1
        c = 0
        d = 0
        e = 0
    if b > (len(coins) - 1):
        a = a + 1
        b = 0
        c = 0
        d = 0
        e = 0
    if a > (len(face) - 1):
        break

    image_comp = Image.new('RGBA', sparkle[0].size, "WHITE")

    image_comp.paste(blob[a],(0,0),blob[a])
    image_comp.paste(coins[b],(0,0),coins[b])
    image_comp.paste(face[c],(0,0),face[c])
    image_comp.paste(hat[d],(0,0),hat[d])
    image_comp.paste(sparkle[e],(0,0),sparkle[e])

    image_comp.save('blobNFTPNG/combo' + str(n) + '.png', 'PNG')

    e = e + 1
    n = n + 1

#image_comp.show()