class Planet:
    def __init__(self, name):
        self.name = name
        self.hasParent = False
        self.hasMoons = False
        self.moons = []
        self.depth = 0

    def addMoon(self, moon):
        moon.__setParent(self)
        self.moons.append(moon)
        self.hasMoons = True

    def __setParent(self, planet):
        self.hasParent = True
        self.parent = planet

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
