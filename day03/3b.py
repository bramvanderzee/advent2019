fn = 'input.txt'
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pathToCoords(path):
    pointer = Coord(0,0)
    coords = []
    for instruction in path:
        direction = instruction[0]
        dist = int(instruction[1:])
        if direction == 'R':
            coords.extend([(x, pointer.y) for x in range(pointer.x, pointer.x+dist)])
            pointer = Coord(pointer.x+dist, pointer.y)
        elif direction == 'L':
            coords.extend([(x, pointer.y) for x in range(pointer.x, pointer.x-dist, -1)])
            pointer = Coord(pointer.x-dist, pointer.y)
        elif direction == 'U':
            coords.extend([(pointer.x, y) for y in range(pointer.y, pointer.y+dist)])
            pointer = Coord(pointer.x, pointer.y+dist)
        elif direction == 'D':
            coords.extend([(pointer.x, y) for y in range(pointer.y, pointer.y-dist, -1)])
            pointer = Coord(pointer.x, pointer.y-dist)

    return coords

lin = []
with open(fn) as f:
    lin = f.readlines()

path1 = lin[0].split(',')
path2 = lin[1].split(',')
intersects = []
coords1 = pathToCoords(path1)
coords2 = pathToCoords(path2)

print('Path to coords done')
print(len(coords1),len(coords2))

for i in range(len(coords1)):
    for o in range(len(coords2)):
        x1, y1 = coords1[i]
        x2, y2 = coords2[o]
        if x1 == x2 and y1 == y2:
            intersects.append([x1, y1, i, o])
            print(x1, y1, i + o)

print('Found intersections')

dists = []
origin = (0,0)
for data in intersects:
    dists.append(int(data[2]) + int(data[3]))

dists.sort()
print(dists)
