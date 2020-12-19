fn = 'input.txt'
imageWidth = 25
imageHeight = 6

def printLayer(layer):
    for row in layer:
        for pixel in row:
            if pixel == 0:
                print(' ', end='')
            elif pixel == 1:
                print('#', end='')
        print('')

with open(fn) as f:
    allLayers = list(f.readlines()[0])
    allLayers.pop() #removes newline

image = []
while len(allLayers) > 0:
    layer = []
    for y in range(imageHeight):
        row = []
        for x in range(imageWidth):
            num = int(allLayers.pop(0))
            row.append(num)
        layer.append(row)
    image.append(layer)

finalImage = image[0][:]
for y in range(imageHeight):
    for x in range(imageWidth):
        if finalImage[y][x] == 2:
            foundPixel = False
            index = 0
            while not foundPixel:
                index += 1
                if image[index][y][x] != 2:
                    finalImage[y][x] = image[index][y][x]
                    foundPixel = True

printLayer(finalImage)
