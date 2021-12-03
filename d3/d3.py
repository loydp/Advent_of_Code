
# bring data in
lines = []
with open('data.txt') as f:
   lines = f.read().splitlines()

num_lines = len(lines)

pos = [0] * 12
for line in lines:
   for count, val in enumerate(line):
      pos[count] += int(val)

gamma = [1 if x > (num_lines / 2) else 0 for x in pos]
epsilon = [0 if x == 1 else 1 for x in gamma]

gamma = "".join([str(x) for x in gamma])
epsilon = "".join([str(x) for x in epsilon])

x = int(gamma, 2)
y = int(epsilon, 2)

print(x * y)