
lines = ''

with open('resources/d1.txt') as f:
    lines = f.readlines()

total = 0
last = int(lines[0][:-1])

for line in lines:
    num = int(line[0:-1])
    if last < num:
        total += 1
    last = num

print(total)
