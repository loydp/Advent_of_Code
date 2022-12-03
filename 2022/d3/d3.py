def get_input():
   input = []
   with open('resources/res.txt') as f:
      input = f.readlines()
   return input

def find_common(lines):
   return [max(set(line[:len(line)//2]).intersection(set(line[len(line)//2:]))) for line in lines]

def get_values(values):
   def value(char:str):
      if char.islower():
         return ord(char) - 96
      else:
         return ord(char) - 38
   return [value(x) for x in values]

def d3_1():
   lines = get_input()
   common = find_common(lines)
   values = get_values(common)
   return sum(values)

#   ---

def find_3_common(lines):
   ret = []
   for i in range(len(lines)//3):
      start = i * 3
      first = lines[start]
      second = lines[start + 1]
      third = lines[start + 2]
      common = set(first).intersection(second).intersection(third)
      ret.append(max(common))
   return ret

def d3_2():
   lines = get_input()
   common = find_3_common(lines)
   values = get_values(common)
   return sum(values)

#   ---

if __name__ == '__main__':
   pr1 = d3_1()
   pr2 = d3_2()
   print(pr1)
   print(pr2)