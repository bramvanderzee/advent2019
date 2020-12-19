import Planet as pl
fn = 'input.txt'

def addDepthToMoons(planet, curDepth):
    for moons in planet.moons:
        addDepthToMoons(moon, curDepth+1)

def findIndirects(planets):
    totalSteps = 0
    for planet in planets:
        searchTop = True
        step = 0
        curPlanet = planet
        while searchTop:
            if curPlanet.hasParent:
                step += 1
                curPlanet = curPlanet.parent
            else:
                searchTop = False
        step -= 1
        totalSteps += step
    return totalSteps + 1
            

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

print('Finding depths...')
numDirects = len(orbitlist)
numIndirects = findIndirects(planets)

print(numDirects + numIndirects)
