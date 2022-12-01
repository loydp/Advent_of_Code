def trim(data, index, command):
   '''Takes in a list and number, does stuff'''
   total = 0
   length = len(data)
   for i in range(len(data)):
      total += int(data[i][index])
   if command == "oxygen":
      vital_bit = 1 if total >= length/2 else 0
      data = [x for x in data if int(x[index]) == vital_bit]
   elif command == 'scrubber':
      vital_bit = 0 if total >= length/2 else 1
      data = [x for x in data if int(x[index]) == vital_bit]
   
   return data

def get_it(data, command):
   '''Send out data repeatedly, until length is 1
   then return that'''
   for i in range(len(data[0])):
      data = trim(data, i, command)
      if len(data) <= 1:
         return data[0]

def get_values(data):
   oxygen = get_it(data, 'oxygen')
   scrubber_rating = get_it(data, 'scrubber')
   return oxygen, scrubber_rating

def get_data():
   lines = []
   with open('data.txt') as f:
      lines = f.read().splitlines()
   return lines

if __name__ == '__main__':
   data = get_data()
   # returns an integer
   oxygen, scrubber_rating = get_values(data)
   total = int(oxygen, 2) * int(scrubber_rating, 2)
   print(total)
