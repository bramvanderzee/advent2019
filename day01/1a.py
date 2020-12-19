lin = []
with open("in1.txt") as f:
    lin = f.readlines()

runtotal = 0
for mass in lin:
    mass = int(mass)
    fuel = (mass//3)-2
    runtotal += fuel

print(runtotal)
