def get_data(filepath):
    with open(filepath) as f:
        data = f.readlines()
    return [[int(num) for num in row.strip()] for row in data]

def check(data, row, col):
    height = data[row][col]
    max_col = len(data[row])

    if row != 0:
        if data[row - 1][col] <= height:
            return 0
    if row != len(data) - 1:
        if data[row + 1][col] <= height:
            return 0
    if col != 0:
        if data[row][col - 1] <= height:
            return 0
    if col != max_col - 1:
        if data[row][col + 1] <= height:
            return 0
    return 1

from collections import deque

def get_basin(data, row, col):
    visited = set()
    search = deque()
    search.append(complex(row, col))

    while search:
        current = search.popleft()
        visited.add(current)
        neighbors = []
        if current.real > 0:
            neighbors.append(complex(-1, 0))
        if current.real < (len(data) - 1):
            neighbors.append(complex(1, 0))
        if current.imag > 0:
            neighbors.append(complex(0, -1))
        if current.imag < len(data[0]) - 1:
            neighbors.append(complex(0, 1))

        for neighbor in neighbors:
            potential = neighbor + current
            if potential not in visited and \
                data[int(potential.real)][int(potential.imag)] != 9:
                search.append(potential)
 
    return len(visited)

from functools import reduce

def process(data):
    total = 0
    low_points = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            low_point = check(data, i, j)
            if low_point:
                low_points.append(get_basin(data, i, j))
                total += data[i][j] + 1
    total2 = reduce(lambda a, b: a * b, sorted(low_points)[-3:])
    return (total, total2)

# 5915
filepath = "source.txt"
data = get_data(filepath)
res1, res2 = process(data)
print(res1)
print(res2)