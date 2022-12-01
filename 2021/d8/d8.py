'''

def get_letters(digits):
   # convert 
   digits = [set(x) for x in digits]
   num_dict = {}

   one = [x for x in digits if len(x) == 2][0]
   eight = [x for x in digits if len(x) == 7][0]
   seven = [x for x in digits if len(x) == 3][0]
   four = [x for x in digits if len(x) == 4][0] 
   two = [x for x in digits if (len(x) == 5 and len(four.union(x)) == 7)][0]
   three = [x for x in digits if len(x) == 5 and len(one.difference(x)) == 0][0]
   five = [x for x in digits if len(x) == 5 and three != x and two != x][0]
   six = [x for x in digits if len(x) == 6 and len(one.union(x)) == 7][0]
   zero = [x for x in digits if len(x) == 6 and x != six and len(three.union(x)) == 7][0]
   nine = [x for x in digits if len(x) == 6 and x != six and x != zero][0]

   num_dict[0] = zero
   num_dict[1] = one
   num_dict[2] = two
   num_dict[3] = three
   num_dict[4] = four
   num_dict[5] = five
   num_dict[6] = six
   num_dict[7] = seven
   num_dict[8] = eight
   num_dict[9] = nine
   return num_dict

def get_sum(dict, msg):
   return []

def get_amount_all(data):
   #letter_dict = get_letters(data[0])
   sums = sum([get_sum(get_letters(x[0]), x[1]) for x in data])
   return sum


'''
def get_amount1(msg):
   letter_sum = len([x for x in msg[1] if len(x) == 2 or len(x) == 4 or len(x) == 7 or len(x) == 3])
   return letter_sum

def get_data(text):
   with open(text) as f:
      raw_data = [x.strip('\n').split() for x in f.readlines()]
      return [(x[:10], x[11:]) for x in raw_data]

if __name__ == "__main__":
   addr = "test.txt"
   data = get_data(addr)
   print(data)
   totals = [get_amount1(x) for x in data]
   print(sum(totals))

   
