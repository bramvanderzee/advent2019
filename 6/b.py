import Planet as pl
fn = 'input.txt'

def findParents(planet):
    parents = []
    searching = True
    curPlanet = planet
    while searching:
        if curPlanet.hasParent:
            parents.append(curPlanet.parent)
            curPlanet = curPlanet.parent
        else:
            searching = False
    return parents

lin = []
print('Reading file...')
with open(fn) as f:
    lin = f.readlines()

print('Splitting lines...')
orbitlist = [x.rstrip('\n').split(')') for x in lin]
allPlanetNames = []
for p in orbitlist:
    allPlanetNames.extend(p)
allPlanetNames = set(allPlanetNames)

planets = []
for name in allPlanetNames:
    planets.append(pl.Planet(name))
planets = list(set(planets))

print('Mapping orbits...')
for pair in [(pl.Planet(p[0]), pl.Planet(p[1])) for p in orbitlist]:
    planet, moon = pair
    if planet in planets and moon in planets:
        planets[planets.index(planet)].addMoon(planets[planets.index(moon)])

print('Finding common orbit...')
for p in planets:
    if p.name == 'YOU':
        you = p
    elif p.name == 'SAN':
        san = p

youParents = findParents(you)
sanParents = findParents(san)

while youParents[-1] == sanParents[-1]:
    youParents.pop()
    sanParents.pop()

path = []
path.extend(youParents)
path.extend(sanParents)
print(len(path))
