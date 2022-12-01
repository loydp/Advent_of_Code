def intify(string):
    return int(string[:-1])

def get_added_depths(lines):
    sums = []
    for i in range(2, len(lines)):
        sums.append(intify(lines[i]) + intify(lines[i - 1]) + intify(lines[i - 2]))
    return sums


lines = ''
with open('resources/d1.txt') as f:
    lines = f.readlines()

summed_depths = get_added_depths(lines)

total = 0
last_depth = summed_depths[0]

for depth in summed_depths:
    if depth > last_depth:
        total += 1
    last_depth = depth

print(len(lines), len(summed_depths))
print(total)
