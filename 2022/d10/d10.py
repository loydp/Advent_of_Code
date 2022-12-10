
def get_input(path):
   data = None
   with open(path) as f:
      data = f.readlines()
   data = [datum.split() for datum in data]
   data = [int(item[1]) if len(item) > 1 else 'n' for item in data]
   return data

def cycle_check(i):
   start_num = 20
   check_num = 40
   if (start_num + i) % check_num == 0:
      return True
   return False

def d10_1(data):
   cycle = 0
   X = 1
   sig_strength = []

   for i, item in enumerate(data):
      if item == 'n':
         cycle += 1
         if cycle_check(cycle):
            sig_strength.append(X * cycle)
      else:
         cycle += 1
         if cycle_check(cycle):
            sig_strength.append(X * cycle)
         cycle += 1
         if cycle_check(cycle):
            sig_strength.append(X * cycle)
         X += item
   return sum(sig_strength)

def draw(cycle, pos, display):
   index = cycle % 40
   row  = cycle // 40
   if pos < index + 2 and pos > index - 2:
      display[row][index] = 'X'
   else:
      display[row][index] = " "

def d10_2(data):
   cycle = 0
   X = 1
   display = [['-' for y in range(40)] for x in range(6)]

   for item in data:
      if item == 'n':
         draw(cycle, X, display)
         cycle += 1
      else:
         draw(cycle, X, display)
         cycle += 1
         draw(cycle, X, display)
         cycle += 1
         X += item
   display = ["".join(row) for row in display]
   return display

if __name__ == '__main__':
   p1 = 'res.txt'
   p2 = 'sample.txt'
   data = get_input(p1)
   res1 = d10_1(data)
   res2 = d10_2(data)
   print(res1)
   for row in res2:
      print(row)