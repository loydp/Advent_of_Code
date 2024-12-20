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
    return height + 1


def process(data):
    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            total += check(data, i, j)
    return total


filepath = "source.txt"
data = get_data(filepath)
res = process(data)
print(res)