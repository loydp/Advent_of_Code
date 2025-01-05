def get_data(input_path):
    with open(input_path) as f:
        return f.readlines()


input_path = "data.txt"

def treat(line):
    line = str.strip(line)
    line = line.split(" ")
    return [int(num) for num in line]

def check(line):
    if line[1] > line[0]:
        for i in range(len(line) - 1):
            diff = line[i + 1] - line[i]
            if diff < 1 or diff > 3:
                return 0
        return 1

    if line[1] < line[0]:
        for i in range(len(line) - 1):
            diff = line[i] - line[i + 1]
            if diff < 1 or diff > 3:
                return 0
        return 1
    return 0


def process1(input_path):
    data = get_data(input_path)
    data = [treat(line) for line in data]
    print(data)
    data = [check(line) for line in data]
    
    return sum(data)

sol1 = process1(input_path)