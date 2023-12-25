def get_input(path: str):
    with open(path) as f:
        lines = f.readlines()
        corrected = []

        for i, line in enumerate(lines):
            temp = line.strip().split(" ")[2:]
            temp = [item for item in temp if item != ""]
            temp = [int(item) if item != "|" else item for item in temp]
            divide_pos = temp.index("|")
            corrected.append((temp[:divide_pos], temp[divide_pos + 1 :]))

        return corrected


def sol1(data):
    pass


def sol2(data):
    pass


input_path = "example.txt"
# input_path = "input.txt"

data = get_input(input_path)

sol1_document = sol1(data)
sol2_document = sol2(data)

print(sol1_document)
print(sol2_document)
