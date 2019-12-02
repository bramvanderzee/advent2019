def computer(program):
    for x in range(0, len(program), 4):
        if program[x] == 1:
            val1 = program[program[x+1]]
            val2 = program[program[x+2]]
            program[program[x+3]] = val1 + val2
        elif program[x] == 2:
            val1 = program[program[x+1]]
            val2 = program[program[x+2]]
            program[program[x+3]] = val1 * val2
        elif program[x] == 99:
            break
    return program

def readInput():
    lin = []
    with open("input.txt") as f:
        lin = f.readlines()

    programstr = lin[0]
    program = programstr.split(',')
    for x in range(len(program)):
        program[x] = int(program[x])
    return program

requiredOut = 19690720

for noun in range(0, 100):
    for verb in range(0, 100):
        program = readInput()
        program[1] = noun
        program[2] = verb
        out = computer(program)
        if out[0] == requiredOut:
            print((noun*100)+verb)
            break
