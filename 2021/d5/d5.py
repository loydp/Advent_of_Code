

def load_data(addr):
   with open(addr) as f:
      return f.read().splitlines()

def isolate_points(line):
   split = line.split()
   tuple1 = split[0].split(",")
   tuple1 = int(tuple1[0]), int(tuple1[1])
   tuple2 = split[2].split(",")
   tuple2 = int(tuple2[0]), int(tuple2[1])
   return tuple1, tuple2

def list_between_straights(loc):
   '''takes a tuple of tuples representing two points
   returns all locations between them in a line, inclusive'''
   # find if x or y axis is the common axis:
   ret_list = []
   common_axis = 'x' if loc[0][0] == loc[1][0] else 'y'
   
   if common_axis == 'x':
      x_val = loc[0][0]
      start = loc[0][1]
      stop = loc[1][1]
      stepping = 1 if start < stop else -1
      if stepping == 1:
         stop += 1
      else:
         stop -= 1
      for i in range(start, stop, stepping):
         ret_list.append((x_val, i))
   else:
      y_val = loc[0][1]
      start = loc[0][0]
      stop = loc[1][0]
      stepping = 1 if start < stop else -1
      if stepping == 1:
         stop += 1
      else:
         stop -= 1
      for i in range(start, stop, stepping):
         ret_list.append((i, y_val))
   return ret_list

def list_between_diagonals(loc):
   '''takes a tuple of tuples representing two points
   returns all locations between them in a line, inclusive'''

   ret_list = []
   # find num of increase/decrease between points
   raw_range_x = loc[0][0] - loc[1][0]
   raw_range_y = loc[0][1] - loc[1][1]

   # establish up/down, range
   x_increment = 1 if raw_range_x < 0 else -1
   y_increment = 1 if raw_range_y < 0 else -1
   final_range = abs(raw_range_x) + 1

   # enact
   for i in range(final_range):
      x = loc[0][0] + (i * x_increment)
      y = loc[0][1] + (i * y_increment)
      ret_list.append((x, y))

   return ret_list


def place_loc(loc, loc_dict):
   '''take in a location and a dict
   store the location in the dict, or if the dict already has the location
   increment the counter by 1'''
   if loc in loc_dict:
      counter = loc_dict[loc] + 1
      loc_dict[loc] = counter
   else:
      loc_dict[loc] = 1

def apply_data(straights, diagonals):
   '''For each tuple, get all between those two inclusive.
   take each and enter them into a provided hashmap'''
   loc_dict = {}
   for item in straights:
      # find each between
      loc_list = list_between_straights(item)
      # enter into the dict list
      for loc in loc_list:
         place_loc(loc, loc_dict)
   for item in diagonals:
      loc_list = list_between_diagonals(item)
      for loc in loc_list:
         place_loc(loc, loc_dict)
   
   return loc_dict

def separate_diagonals(data):
   ret_list1 = []
   ret_list2 = []
   for item in data:
      if item[0][0] == item[1][0] or item[0][1] == item[1][1]:
         ret_list1.append(item)
      else:
         ret_list2.append(item)


   return ret_list1, ret_list2


if __name__ == "__main__":
   '''
   Takes in a list of point tuples. Each tuple indicates the 
   start and end of a segment.
   Returns the number of points at which two or more segments
   cover that point.
   '''

   addr = "data.txt"
   
   # acquire data
   data = load_data(addr)

   # structure the data into this form: ((x0, y0), (x1, y1))
   data = [isolate_points(x) for x in data]

   # remove invalid data
   straight, diagonal = separate_diagonals(data)

   # move data into a hashmap
   loc_dict = apply_data(straight, diagonal)

   #evaluate hashmap
   total = [x for x in loc_dict.values() if x > 1]
   
   print(len(total))