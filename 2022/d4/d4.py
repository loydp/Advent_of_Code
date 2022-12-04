def get_input():
   ret = None
   with open('resources/res.txt') as f:
      ret = f.read().split("\n")
   return ret

def process_input(input):
   def splitter(item):
      item = item.split(',')
      item = [x.split('-') for x in item]
      item = [[int(x[0]), int(x[1])] for x in item]
      return item

   input = [splitter(line) for line in input]
   return input


def d4_1(input):
   count = 0
   for pair in input:
      if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
         count += 1
      elif pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
         count += 1
   return count
   
def d4_2(input):
   count = 0
   for pair in input:
      if pair[0][0] <= pair[1][1] and pair[0][1] >= pair[1][0]:
         count += 1
   return count

if __name__ == "__main__":
   input = get_input()
   input = process_input(input)

   res1 = d4_1(input)
   print(res1)

   res2 = d4_2(input)
   print(res2)