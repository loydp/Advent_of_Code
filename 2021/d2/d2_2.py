def get_directions(address):
    with open(address) as f:
        return f.read().splitlines()


x = 0
y = 0
address = "directions.txt"

lines = get_directions(address)

aim = 0

for line in lines:
    direction, amt = line[0], int(line[-1])
    
    if direction == 'f':
        x += amt
        y += aim * amt
    else:
        if direction == 'd':
            aim += amt
        else:
            aim -= amt

print(x * y)


