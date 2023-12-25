def get_input(input_src):
    ret = []
    with open(input_src) as f:
        ret = f.readlines()
    return ret


def get_coords_from_line(line: str, line_num):
    coords = []

    i = 0
    while i < len(line):
        if line[i].isdigit():
            start = i
            digits = []
            j = i
            while j < len(line) and line[j].isdigit():
                digits += line[j]
                j += 1
            end = start + len(digits)
            i = end
            digits = int("".join(digits))
            coords.append((line_num, start, end, digits))
        i += 1
    return coords if coords else None


def find_num_coords(schematic):
    coords = []

    for i, line in enumerate(schematic):
        coord = get_coords_from_line(line, i)
        if coord:
            for item in coord:
                coords.append(item)

    return coords


def is_mechanism(char):
    if char.isdigit():
        return False
    if char == ".":
        return False
    return True


def find_connected_coords(schematic, coords):
    ret_coords = []

    for coord in coords:
        skip = False
        row_start = max(0, coord[0] - 1)
        row_end = min(len(schematic) - 1, coord[0] + 1)
        col_start = max(0, coord[1] - 1)
        col_end = min(len(schematic[0]) - 1, coord[2] + 1)
        for i in range(row_start, row_end + 1):
            if skip == True:
                break
            for j in range(col_start, col_end):
                if skip == True:
                    break
                if is_mechanism(schematic[i][j]):
                    ret_coords.append(coord)
                    skip = True

    return ret_coords


def sol1(schematic):
    number_coordinates = find_num_coords(schematic)
    # print("num coordinates: -> \n", number_coordinates)
    connected_coords = find_connected_coords(schematic, number_coordinates)
    # print("connected coordinates: -> \n", connected_coords)
    connected_nums = [x[3] for x in connected_coords]
    # print("connected nums: -> \n", connected_nums)
    return sum(connected_nums)


def find_num_gear_pairs(schematic, coords):
    mapping = {}

    for coord in coords:
        skip = False
        row_start = max(0, coord[0] - 1)
        row_end = min(len(schematic) - 1, coord[0] + 1)
        col_start = max(0, coord[1] - 1)
        col_end = min(len(schematic[0]) - 1, coord[2] + 1)
        for i in range(row_start, row_end + 1):
            if skip == True:
                break
            for j in range(col_start, col_end):
                if skip == True:
                    break
                if schematic[i][j] == "*":
                    mapping[coord] = (i, j)
                    skip = True
    return mapping


def map_gears_to_numbers(numbers_to_gears_map: dict):
    gears_to_numbers_map = {}

    for k, v in numbers_to_gears_map.items():
        if v not in gears_to_numbers_map:
            gears_to_numbers_map[v] = [k[-1]]
        else:
            gears_to_numbers_map[v].append(k[-1])
    return gears_to_numbers_map


def sol2(schematic):
    number_coordinates = find_num_coords(schematic)
    # print(number_coordinates)
    numbers_mapped_to_gears = find_num_gear_pairs(schematic, number_coordinates)
    # print(numbers_mapped_to_gears)
    gears_to_numbers = map_gears_to_numbers(numbers_mapped_to_gears)
    # every number that shares a gear gets multiplied
    products = [
        item[0] * item[1] for item in gears_to_numbers.values() if len(item) > 1
    ]
    return sum(products)


# input_src = "example.txt"
input_src = "input.txt"


def main():
    schematic = get_input(input_src)
    res1 = sol1(schematic)
    res2 = sol2(schematic)

    print(res1)
    print(res2)


main()
