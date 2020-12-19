class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def coordsToCoord(self, x, y):
        coords = []
        if self.x == x and self.y != y:
            coords = [Coord(x, i) for i in range(self.y, y)]
        elif self.x != x and self.y == y:
            coords = [Coord(i, y) for i in range(self.x, x)]
        coord = Coord(x,y)
        coords.append(coord)
        return coords

    def manhattanDistance(self, coord):
        distx = abs(self.x - coord.x)
        disty = abs(self.y - coord.y)
        return distx + disty

def pathToCoords(path):
    origin = Coord(0,0)
    pointer = Coord(0,0)
    coords = []
    for instruction in path:
        direction = instruction[0]
        dist = int(instruction[1:])
        if direction == 'R':
            coords.extend(pointer.coordsToCoord(pointer.x + dist, pointer.y))
        elif direction == 'L':
            coords.extend(pointer.coordsToCoord(pointer.x - dist, pointer.y))
        elif direction == 'U':
            coords.extend(pointer.coordsToCoord(pointer.x, pointer.y + dist))
        elif direction == 'D':
            coords.extend(pointer.coordsToCoord(pointer.x, pointer.y - dist))
        pointer = coords[-1]

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
print(len(coords1),len(coords2))

for coord in coords1:
    for coord2 in coords2:
        if coord.x == coord2.x and coord.y == coord2.y:
            intersects.append(coord)
            print(coord.x, coord.y)

print('Found intersections')

dists = []
origin = Coord(0,0)
for coord in intersects:
    dists.append(coord.manhattanDistance(origin))

dists.sort()
print(dists)
