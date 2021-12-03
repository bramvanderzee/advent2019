import sys
import math

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

locs = []
xc, yc = 0, 0
with open(fn) as f:
    for l in f:
        for c in l.strip():
            if c == '#':
                locs.append((xc, yc))
            xc += 1
        yc += 1
        xc = 0

def find_angle(from_loc, to_loc):
    fromx, fromy = from_loc
    tox, toy = to_loc
    dx, dy = tox - fromx, toy - fromy
    angle = math.degrees(math.atan2(dy,dx)) + 90.0
    if angle < 0:
        angle += 360
    return angle

def is_visible_from(to_loc, from_loc, locs):
    tox, toy = to_loc
    fromx, fromy = from_loc
    dx, dy = tox - fromx, toy - fromy
    gcd = math.gcd(dx, dy)
    if gcd == 1:
        return True

    dx, dy = int(dx/gcd), int(dy/gcd)
    for d in range(1, gcd):
        cx = fromx + (dx * d)
        cy = fromy + (dy * d)
        if (cx, cy) in locs:
            return False
    return True

def count_visible(loc, locs):
    count = 0
    for to_check in locs:
        if not to_check == loc:
            if is_visible_from(to_check, loc, locs):
                count += 1
    return count

def get_visible(loc, locs):
    coords = []
    for to_check in locs:
        if not to_check == loc:
            if is_visible_from(to_check, loc, locs):
                coords.append(to_check)
    return coords

best_score = 0
best_coord = None
for loc in locs:
    score = count_visible(loc, locs)
    if score > best_score:
        best_score = score
        best_coord = loc

print(best_coord, best_score)

destroy_count = 0
nth = None
for i in sorted(get_visible(best_coord, locs), key=lambda l: find_angle(best_coord, l)):
    locs.remove(i)
    destroy_count += 1
    if destroy_count == 200:
        nth = i
        break

x, y = nth
print(x*100 + y)