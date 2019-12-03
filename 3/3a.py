class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def coordsToCoord(self, x, y):
        if self.x == x and self.y != y:
            return [Coord(self.x, i) for i in range(self.y, y)]
        elif self.x != x and self.y == y:
            return [Coord(i, self.y) for i in range(self.x, x)]
        else:
            return []

def pathToCoords(path):
    origin = Coord(0,0)
    pointer = Coord(0,0)
    coords = []
    for instruction in path:
        direction = instruction[0]
        dist = int(instruction[1:])
        if direction == 'R':
            coords.append(pointer.coordsToCoord(pointer.x + dist, pointer.y))
        elif direction == 'L':
            coords.append(pointer.coordsToCoord(pointer.x - dist, pointer.y))
        elif direction == 'U':
            coords.append(pointer.coordsToCoord(pointer.x, pointer.y + dist))
        elif direction == 'D':
            coords.append(pointer.coordsToCoord(pointer.x, pointer.y - dist))

    return coords

lin = []
with open('input.txt') as f:
    lin = f.readlines()

path1 = lin[0].split(',')
path2 = lin[1].split(',')
intersects = []
coords1 = pathToCoords(path1)
coords2 = pathToCoords(path2)

print('Path to coords done')

for coord in coords1:
    if coord in coords2:
        intersects.append(coord)

print(intersects)
