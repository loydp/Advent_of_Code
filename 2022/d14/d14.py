def get_input(path):
    data = None
    with open(path) as f:
        data= f.readlines()

    coords = []

    for line in data:
        line = [x for x in line.split() if x != '->']
        line = [x.split(',') for x in line]
        line = [(int((x[0])), int(x[1])) for x in line]
        coords.append(line)
    return coords

def offset_coord(offset, coord):
    return (coord[0] + offset[0], coord[1] + offset[1])

def get_coord_line(coord1, coord2) -> list:
    '''draw a line with coordinates, non-inclusive of the first coord
    input: (1, 1), (5, 1)
    return: (2, 1) through (5, 1)
    '''
    if coord1 == None:
        return [coord2]
    x1, y1 = coord1
    x2, y2 = coord2
    line = []
    x_len = abs(x1 - x2) + 1
    y_len = abs(y1 - y2) + 1
    x_source = x1 if x1 < x2 else x2
    y_source = y1 if y1 < y2 else y2

    for x in range(x_source, x_source + x_len):
        for y in range(y_source, y_source + y_len):
            line.append((x, y))

    return line

def create_world(coords, source, part=1):
    '''Takes in the coords, returns an array'''
    minx = maxx = source[0]
    miny = maxy = source[1]

    for line in data:
        for coord in line:
            x, y = coord
            if x > maxx:
                maxx = x
            elif x < minx:
                minx = x
            if y > maxy:
                maxy = y
            elif y < miny:
                miny = y
    length = maxx - minx + 1
    height = maxy - miny + 1

    offset = (-minx, 0)

    world = [["." for square in range(length)] for line in range(height)]

    # populate world
    for line in data:
        # previous point, that a line may be drawn from
        prev = None
        for coord in line:
            # translate each point into a new point
            offset_point = offset_coord(offset, coord)
            # get a line from the previous point to this point
            coords = get_coord_line(prev, offset_point)
            prev = offset_point
            for point in coords:
                col, row = point
                world[row][col] = '#'
    return world, offset

def create_world2(coords, source, part=1):
    '''Takes in the coords, returns an array'''
    minx = maxx = source[0]
    miny = maxy = source[1]

    for line in data:
        for coord in line:
            x, y = coord
            if x > maxx:
                maxx = x
            elif x < minx:
                minx = x
            if y > maxy:
                maxy = y
            elif y < miny:
                miny = y
    length = maxx - minx + 1
    height = maxy - miny + 1
    height += 2
    length += height * 2
    offset = (-minx + height, 0)

    world = [["." for square in range(length)] for line in range(height)]
    for i in range(len(world[-1])):
        world[-1][i] = '#'

    # populate world
    for line in data:
        # previous point, that a line may be drawn from
        prev = None
        for coord in line:
            # translate each point into a new point
            offset_point = offset_coord(offset, coord)
            # get a line from the previous point to this point
            coords = get_coord_line(prev, offset_point)
            prev = offset_point
            for point in coords:
                col, row = point
                world[row][col] = '#'
    return world, offset

def in_bounds(world, row, col):
    y = len(world)
    x = len(world[0])
    return True if 0 <= row < y and 0 <= col < x else False

def print_world(world):
    ret_world = []
    for line in world:
        ret_world.append("".join(line))
        ret_world.append("\n")

    print("".join(ret_world))

def add_sand(world, offset, source):
    col, row = offset_coord(offset, source)

    # if source has sand, return false
    if world[row][col] == 'O':
        return False


    prev_col = None
    prev_row = None
    # settle the sand until it can't move
    while col != prev_col and row != prev_row:
        prev_col = col
        prev_row = row
        # try dropping it
        while in_bounds(world, row + 1, col) and world[row + 1][col] == '.':
            row += 1
        # try settling it
        if in_bounds(world, row + 1, col - 1) and world[row + 1][col - 1] == '.':
            row += 1
            col -= 1
        elif in_bounds(world, row + 1, col + 1) and world[row + 1][col + 1] == '.':
            row += 1
            col += 1

    # determine why the sand can't move
    # if it's falling into void, return false
    if row -1 == len(world):
        return False       
    # if it's got void on either side, return false
    if col == len(world[0]) - 1 or col == 0:
        return False
    world[row][col] = 'O'

    return True

def d14_1(data):

    source = (500, 0)
    # make world


    world, offset = create_world(data, source)

    go = True
    while go:
        go = add_sand(world, offset, source)
    
    count = sum([line.count('O') for line in world])
    #print_world(world)
    return count

def d14_2(data):

    source = (500, 0)

    world, offset = create_world2(data, source, 2)

    go = True
    while go:
        go = add_sand(world, offset, source)
    count = sum([line.count('O') for line in world])
    #print_world(world)
    return count



if __name__ == '__main__':
    path1 = "res.txt"
    path2 = "sample.txt"
    data = get_input(path1)
    
    ans1 = d14_1(data)
    print(ans1)

    ans2 = d14_2(data)
    print(ans2)
