# This one was rough, had too look manually through this list of values there.

'''
def get_data(addr):
   with open(addr) as f:
      return list(map(int, f.read().split(',')))

def get_median(data):
   return data[(len(data) // 2)]

def get_abs(median, x):
   return abs(x - median)

def get_fuel(median, data):
   return sum([get_abs(median, x) for x in data])

# part II

def get_triangle(pos, x):
   return (abs(pos - x) * (abs(pos - x) + 1)) / 2

def get_sum(data, pos):
   return sum([get_triangle(pos, x) for x in data])

def find_val(data):
   return min([get_sum(x, data) for x in data])

def get_fuel(data, loc):
   return get_sum(data, loc)

def get_min_loc(data):
   sums = [get_sum(data, x) for x in data]
   print(sums)
   printable = sums.index(min(sums))
   return sums.index(min(sums))

def get_min_fuel(data):
   loc = get_min_loc(data)
   print(loc)
   fuel = get_fuel(data, loc)
   return fuel

if __name__ == '__main__':
   addr = 'test.txt'
   data = get_data(addr)
   data.sort()
   median = get_median(data)
   #print(median)
   pos = get_fuel(data, median)
   #print(pos)


   k = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

   min_fuel = get_min_fuel(data)
   print(int(min_fuel))


#   total = 0
#   for i in range(len(data)):
#      total += get_triangle(data[i], 5)
   # loc = find_val(data)
#   print(total)



# 137261 is incorrect

'''


def __get_triangle(pos, x):
   return int((abs(pos - x) * (abs(pos - x) + 1)) / 2)


def __get_fuel_at(data, pos):
   return sum([__get_triangle(pos, x) for x in data])


def my_min(arr):
   min = 10000000
   for i in range(len(arr)):
      if arr[i] < min:
         min = arr[i]
   return min

def find_min_fuel(data):
   for i in range(len(data)):
      print(__get_fuel_at(data, i))

   min = my_min([__get_fuel_at(data, x) for x in range(len(data))])
   return min


def get_data(addr):
   with open(addr) as f:
      return list(map(int, f.read().split(',')))

if __name__ == '__main__':
   addr = "data.txt"
   
   data = get_data(addr)

   fuel = find_min_fuel(data)
   #fuel = __get_fuel_at(data, loc)
   print(fuel)
