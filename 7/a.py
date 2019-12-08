import Computer as cp
from itertools import permutations

def generateInputs():
    settings = range(5)
    perms = permutations(settings)
    return list(perms)

fn = 'input.txt'
lin = []
with open(fn) as f:
    lin = f.readlines()

ACS = [int(x) for x in lin[0].split(',')]
ampA = cp.Computer('Amp 0', ACS)
ampB = cp.Computer('Amp 1', ACS)
ampC = cp.Computer('Amp 2', ACS)
ampD = cp.Computer('Amp 3', ACS)
ampE = cp.Computer('Amp 4', ACS)


amps = [ampA, ampB, ampC, ampD, ampE]

outputs = []
allInputs = generateInputs()
for inp in allInputs:
    prevOut = 0
    for i, amp in enumerate(amps):
        ampInputs = [inp[i], prevOut]
        while amp.running:
            if amp.nextIsInput:
                amp.next(ampInputs.pop(0))
            elif amp.nextIsOutput:
                prevOut = amp.next()
            else:
                amp.next()
        amps[i] = cp.Computer('Amp %d' % i, ACS)

    outputs.append([prevOut, inp])
    print(prevOut, inp)

maxScore = 0
maxSettings = []
for i in outputs:
    if i[0] > maxScore:
        maxScore = i[0]
        maxSettings = i[1]

print(maxScore, maxSettings)
