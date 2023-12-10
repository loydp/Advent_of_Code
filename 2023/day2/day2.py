from functools import reduce


def get_input(path: str):
    res = []
    with open(path) as f:
        res = f.readlines()
    return res


def condense(game):
    ret = []
    for round in game:
        round = round.replace(",", "")
        round.strip()
        round = round.split()
        round = [int(item) if item.isdigit() else item[0] for item in round]
        ret.append(round)
    return ret


def format_data(raw_data):
    # strip lines
    final_line = raw_data[-1]
    final_line = final_line[8:]
    data = [line[8:-1] for line in raw_data[:-1]]
    data.append(final_line)
    data = [line.split(";") for line in data]
    data = list(map(condense, data))

    ret_list = []
    for game in data:
        game_list = []
        for round in game:
            round_dict = {}
            for i, item in enumerate(round):
                if type(item) == int:
                    char = round[i + 1]
                    round_dict[char] = item
            game_list.append(round_dict)
        ret_list.append(game_list)
    return ret_list


def check_games(games: list[list[dict]], requirements: dict) -> list[int]:
    def check(game: list[dict], requirements: dict):
        maxes = {"r": -1, "g": -1, "b": -1}
        skip = False
        for round in game:
            for k in round.keys():
                if round[k] > requirements[k]:
                    return False
        return True

    ret = []

    for i, game in enumerate(games):
        if check(game, requirements):
            ret.append(i + 1)
    return ret


def get_power_games(games: list[list[dict]]) -> list[int]:
    results = []
    for game in games:
        maxes = {"r": -1, "g": -1, "b": -1}
        for round in game:
            for k in round.keys():
                maxes[k] = max(maxes[k], round[k])
        results.append(reduce(lambda x, y: x * y, [val for val in maxes.values()]))

    return results


sample = "sample.txt"
input = "input.txt"
requirements = {"r": 12, "g": 13, "b": 14}

# get the data
raw_data = get_input(input)

# format data such that what is returned is a dictionary for each round of each game
formatted_data = format_data(raw_data)

# for each game check if the game meets the requirements
passing_games = check_games(formatted_data, requirements)
power_games = get_power_games(formatted_data)

sol1_printable = sum(passing_games)

print(sol1_printable)

sol2_printable = sum(power_games)
print(sol2_printable)
