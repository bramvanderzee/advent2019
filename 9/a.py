import Computer as cp

fn = 'input.txt'

with open(fn) as f:
    lin = f.readlines()

BOOST = [int(x) for x in lin[0].split(',')]
com = cp.Computer('BOOST', BOOST)

while com.running:
    com.next()


