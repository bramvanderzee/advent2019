lower = 353096
upper = 843213

def check(num, lower, upper):
    numList = sorted([int(x) for x in str(num)])
    for i, x in enumerate(numList):
        if int(num[i]) != int(x):
            return False
    foundAdjacent = False
    for i, x in enumerate(num):
        if i == 5:
            break
        if int(num[i+1]) == int(x) and num.count(x) == 2:
            foundAdjacent = True
            break
    if not foundAdjacent:
        return False

    if int(num) < lower or int(num) > upper:
        return False

    return True

passwords = []
for i in range(lower, upper+1):
    if check(str(i), lower, upper):
        passwords.append(i)

print(len(passwords))
