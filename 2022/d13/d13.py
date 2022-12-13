def get_input(path):
   data = None
   with open(path) as f:
      data = f.readlines()
   data = [line for line in data if line[0] != '\n']
   data = [eval(line) for line in data]
   return data

def rec_process(left, right):
   '''Returns are -1, 0, 1 in order to pass this as an argument for sorted()'''
   #print(f"left= {left} right = {right}")
   
   # if two ints:
   if type(left) == int and type(right) == int:
      if left == right:
         return False
      elif left < right:
         return 1
      else:
         return -1

   # if one int and one list
   if type(left) == int and type(right) == list:
      return rec_process([left], right)
   if type(left) == list and type(right) == int:
      return rec_process(left, [right])

   # if two lists, recurse
   count = 0
   while count < min([len(left), len(right)]):
      check = rec_process(left[count], right[count])
      if check == 0:
         pass
      elif check == 1:
         return 1
      else:
         return -1
      count += 1
   
   # then if one list shorter than the other
   if len(left) < len(right):
      return 1
   elif len(right) < len(left):
      return -1
   else:
      return 0

# to make part 2 dead easy, we use cmp_to_key for the sorted method
import functools

def d13_1(data):
   pairs = []
   for i in range(0, len(data), 2):
      pairs.append((data[i], data[i+1]))
   
   pairs = [rec_process(pair[0], pair[1]) for pair in pairs]
   addends = []
   for i in range(len(pairs)):
      if pairs[i] == 1:
         addends.append(i + 1)
   return sum(addends)

def d13_2(data:list):
   data.append([[2]])
   data.append([[6]])
   # this is where the magic happens
   data = sorted(data, key=functools.cmp_to_key(rec_process), reverse=True)
   ret = (data.index([[2]]) + 1) * (data.index([[6]]) + 1)
   return ret

if __name__ == "__main__":
   p1 = "res.txt"
   p2 = "sample.txt"
   data = get_input(p1)
   r1 = d13_1(data)
   r2 = d13_2(data)
   print("answer 1:", r1)
   print("answer:", r2)