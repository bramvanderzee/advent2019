fn = 'input.txt'
imageWidth = 25
imageHeight = 6

with open(fn) as f:
    allLayers = list(f.readlines()[0])
    allLayers.pop() #removes newline

image = []
metadata = []
while len(allLayers) > 0:
    nums = [0, 0, 0]
    columns = []
    for y in range(imageHeight):
        row = []
        for x in range(imageWidth):
            num = int(allLayers.pop(0))
            nums[num] += 1
            row.append(num)
        columns.append(row)
    image.append(columns)
    metadata.append(nums)

leastZeroLayerIndex = 0
minZeros = 25*6
for i, data in enumerate(metadata):
    if data[0] < minZeros:
        minZeros = data[0]
        leastZeroLayerIndex = i

print(metadata[leastZeroLayerIndex][1] * metadata[leastZeroLayerIndex][2])
