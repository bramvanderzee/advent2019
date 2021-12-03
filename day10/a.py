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

best_score = 0
best_coord = None
for loc in locs:
    score = count_visible(loc, locs)
    if score > best_score:
        best_score = score
        best_coord = loc

print(best_coord, best_score)