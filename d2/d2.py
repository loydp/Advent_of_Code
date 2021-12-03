def directed(line, x, y):
    first_char = line[0]
    amt = int(line[-1])

    if first_char == 'f':
        x += amt
        return (x, y)
    elif first_char == 'd':
        y += amt
        return (x, y)
    else:
        y -= amt
        return (x, y)


lines = []
with open("directions.txt") as f:
    lines = f.read().splitlines()

x = 0
y = 0

for line in lines:
    x, y = directed(line, x, y)

print(x * y)

