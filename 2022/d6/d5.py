def get_input():
   input = None
   with open('res.txt') as f:
      input = f.readlines()
   return input[0]

def d5_1(input, length):
   for i in range(len(input)):
      if len(set(input[i:i+length])) == length:
         return i + length

if __name__ == '__main__':
   input = get_input()
   index = d5_1(input, 4)
   index = d5_1(input, 14)
   print(index)