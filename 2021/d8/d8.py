with open("data.txt") as f:
   data = f.readlines()

patterns = []
entries = []
for line in data:
   p, e = line.split("|")
   patterns.append(p)
   entries.append(e)

def sol1(data):
   count = 0
   for row in data:
      row = map(lambda num: 1 if len(num) != 5 and len(num) != 6 else 0, row.split())
      count += sum(row)
   return count

sol1 = sol1(entries)

print(f"Solution 1: {sol1}")

num_dict_og = {
   (0, 1, 2, 4, 5, 6) : 0,
   (2, 5) : 1,
   (0, 2, 3, 4, 6) : 2,
   (0, 2, 3, 5, 6) : 3,
   (1, 2, 3, 5) : 4,
   (0, 1, 3, 5, 6) : 5,
   (0, 1, 3, 4, 5, 6) : 6,
   (0, 2, 5) : 7,
   (0, 1, 2, 3, 4, 5, 6) : 8,
   (0, 1, 2, 3, 5, 6) : 9,
}

def get_num_dicts(data:list) -> list[dict]: 
   dicts = []
   for line in data:
      line = line.split()
      line = sorted(line, key=lambda l: len(l))
      line = map(set, line)
      one, seven, four, *others, eight = line
      
      mapping = {}
      
      # 0
      mapping[(seven - one).pop()] = 0

      # 4, 6
      sevenfour = seven.union(four)
      subtracted_list = [(item - sevenfour) for item in others]
      bottom = [item for item in subtracted_list if len(item) == 1][0]
      bottom_left = [item - bottom for item in subtracted_list if len(item) == 2][0]
      bottom_left2 = bottom_left.copy()
      mapping[bottom.pop()] = 6
      mapping[bottom_left.pop()] = 4

      # 1, 2, 5
      sub_from_eight_list = [eight - item for item in others if len(item) == 5]

      sub_bl_from_sub_eight = [item - bottom_left2 for item in sub_from_eight_list]
      singles = [item for item in sub_bl_from_sub_eight if len(item) == 1]
      doubles = [item for item in sub_bl_from_sub_eight if len(item) == 2]
      double = doubles[0] # only one in there
      subtracted_list = [double - item for item in singles]

      bottom_right = [item for item in subtracted_list if len(item) == 1][0]
      top_left = [item - bottom_right for item in subtracted_list if len(item) == 2][0]
      top_right = [item for item in singles if item != top_left][0]
      
      mapping[bottom_right.pop()] = 5
      mapping[top_left.pop()] = 1
      mapping[top_right.pop()] = 2

      # 3
      for char in "abcdefg":
         if char not in mapping:
            mapping[char] = 3
      dicts.append(mapping)
   return dicts

def sol2(patterns, entries):
   num_dicts = get_num_dicts(patterns)

   sum = 0
   for key, entry in zip(num_dicts, entries):
      entry = entry.split()
      digits = []
      for word in entry:
         decoded = [key[letter] for letter in word]
         digit = num_dict_og[tuple(sorted(decoded))]
         digits.append(digit)
      digits = map(str, digits)
      digit = "".join(digits)
      sum += int(digit)

   

   return sum

sol2 = sol2(patterns, entries)
print(f"Solution 2: {sol2}")