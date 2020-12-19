import Computer as cp
from itertools import permutations

def generateInputs():
    settings = range(5,10)
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
    lastAmpRunning = True
    inps = list(inp)
    inps.insert(-1, 0)
    while lastAmpRunning:
        for i, amp in enumerate(amps):
            ampBusy = True
            while ampBusy:
                if not amp.running:
                    if amp.name == 'Amp 4':
                        lastAmpRunning = False
                    ampBusy = False
                elif amp.nextIsInput:
                    amp.next(inps.pop())
                elif amp.nextIsOutput:
                    prevOut = amp.next()
                    ampBusy = False
                else:
                    amp.next()
            inps.insert(-1, prevOut)


    for i in range(len(amps)):
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
