

src = "source.txt"

def get_raw_data() -> list:
    with open(src) as f:
        return f.readlines()


def process_to_int_lists(data):
    first_row = []
    second_row = []
    for line in data:
        first, second = line.split()
        first_row.append(int(first))
        second_row.append(int(second))
    return first_row, second_row

def find_diffs(data):
    return [abs(datum[0] - datum[1]) for datum in zip(data[0], data[1])]

data = get_raw_data()
data = process_to_int_lists(data)

data1 = [sorted(lst) for lst in data]
res1 = find_diffs(data1)
print(sum(res1))

# done part 1

def matching(data):
    right = {}
    for num in data[1]:
        if num in right:
            right[num] += 1
        else:
            right[num] = 1
    print(right)
    return [num * right[num] if num in right else 0 for num in data[0]]

data2 = matching(data)

print(sum(data2))