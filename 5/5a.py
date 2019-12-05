import Computer as c
fileIn = 'input.txt'

def readInput():
    lin = []
    with open(fileIn) as f:
        lin = f.readlines()

    programstr = lin[0]
    program = programstr.split(',')
    for x in range(len(program)):
        program[x] = int(program[x])
    return program

program = readInput()
#program = [102,3,1,0,4,0,99]
computer = c.Computer(program)

while computer.running:
    computer.next()

