lin = []
with open("input.txt") as f:
    lin = f.readlines()

programstr = lin[0]
program = programstr.split(',')

program[1] = 12
program[2] = 2


for x in range(len(program)):
    program[x] = int(program[x])

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
        print("End")
        break
    else:
        print("error")

print(program[0])
