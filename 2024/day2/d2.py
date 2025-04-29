def get_data(input_path):
    with open(input_path) as f:
        return f.readlines()

def treat(data):
    ret = []
    for line in data:
        line = str.strip(line)
        line = line.split(" ")
        ret.append([int(num) for num in line])
    return ret

# confirmed works
def safe_diff(input_1: int, input_2: int) -> int:
    """
    If input 1 is 1 to 3 greater than input 2, return 1
    If input 1 is 1 to 3 less than input 2, return -1
    else return 0
    """
    if 1 <= (input_2 - input_1) <= 3:
        return 1
    if 1 <= (input_1 - input_2) <= 3:
        return -1
    return 0

def process_1(reactor_levels):
    total_count = 0
    for levels in reactor_levels:
        level_check = []
        i = 0
        while i < len(levels) - 1:
            level_check.append(safe_diff(levels[i], levels[i + 1]))
            i += 1
        if all(map(lambda x: x == + 1, level_check)):
            total_count += 1
        if all(map(lambda x: x == - 1, level_check)):
            total_count += 1
        continue
    return total_count
        

def process_2(reactor_levels):
    total_count = 0
    for level in reactor_levels:
        if process_1([level]):
            total_count += 1
        else:
            i = 0
            while i < len(level):
                new_level = level[:i] + level[i + 1:]
                if process_1([new_level]):
                    total_count += 1
                    break
                i += 1

    return total_count

input_path = "data.txt"
data = get_data(input_path)
reactor_levels = treat(data)
sol1 = process_1(reactor_levels)
sol2 = process_2(reactor_levels)

print(sol1)
print(sol2)