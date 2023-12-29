def get_input(path: str):
    with open(path) as f:
        lines = f.readlines()
        corrected = []

        for i, line in enumerate(lines):
            temp = line.strip().split(" ")
            temp = [item for item in temp if item != ""]
            temp = [int(item) if item != "|" else item for item in temp[2:]]
            divide_pos = temp.index("|")
            corrected.append((temp[:divide_pos], temp[divide_pos + 1 :]))

        return corrected


def sol1(data):
    finals = []
    for line in data:
        power = -1
        d = set()
        for entry in line[0]:
            d.add(entry)
        for entry in line[1]:
            if entry in d:
                power += 1
        if power == -1:
            finals.append(0)
        else:
            finals.append(2**power)
    return sum(finals)


def num_matches(data: tuple[list[int], list[int]]) -> int:
    set1 = set(data[0])
    set2 = set(data[1])
    ret_num = len(set1.intersection(set2))
    return ret_num


def process(data, i, memos) -> int:
    if memos[i] != -1:
        return memos[i]
    matches = num_matches(data[i])
    entry_sum = matches
    for j in range(i + 1, i + 1 + matches):
        entry_sum += process(data, j, memos)
    return entry_sum


def sol2(data):
    memos = [-1 for _ in range(len(data))]

    result = len(data)

    for i in range(len(data)):
        result += process(data, i, memos)
    return result


# input_path = "example.txt"
input_path = "input.txt"

data = get_input(input_path)

sol1_document = sol1(data)
sol2_document = sol2(data)

print(sol1_document)
print(sol2_document)
