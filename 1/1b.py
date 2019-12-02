def recursiveFuelCalc(mass):
    fuel = (int(mass)//3)-2
    if fuel > 0:
        extraFuel = recursiveFuelCalc(fuel)
        if extraFuel > 0:
            fuel += extraFuel

    return fuel

lin = []
with open("in1.txt") as f:
    lin = f.readlines()

runtotal = 0
for mass in lin:
    fuel = recursiveFuelCalc(mass)
    runtotal += fuel

print(runtotal)
