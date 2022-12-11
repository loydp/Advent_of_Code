
class Monkey:
   
   def times(self, item):
      return item * self.operation_value

   def times_old(self, item):
      return item * item

   def add(self, item):
      return item + self.operation_value

   def test(self, item):
      if item % self.divisor == 0:
         return self.mtrue
      else:
         return self.mfalse

   def give(self, item):
      self.holding.append(item)


   def __init__(self, data) -> None:
      self.monkeys = []
      self.holding = None
      self.operation = None
      self.operation_value = None
      self.divisor = None
      self.mtrue = None
      self.mfalse = None
      self.inspected = 0
      self.lcm = None

      self.holding = list(map(int, data[0].replace(',', ' ').split(":")[1].split()))
      
      # get operation
      op_string = data[1]
      operator = '+' if '+' in op_string else '*'
      op_value = op_string.split()[-1]
      if op_value == 'old':
         self.operation = self.times_old
      else:
         self.operation_value = int(op_value)
         self.operation = self.times if operator == '*' else self.add

      # get Test
      test_strings = data[2:5]
      self.divisor = int(test_strings[0].split()[-1])
      self.mtrue = int(test_strings[1].split()[-1])
      self.mfalse = int(test_strings[2].split()[-1])

   def throw_to(self, item, target):
      self.monkeys[target].give(item)

   def inspect(self, item):
      self.inspected += 1
      
      return self.operation(item)

   def run(self):
      for an_item in self.holding:
         
         item = self.inspect(an_item)
         # FIXME:

         target_monkey = self.test(item)
         item %= self.lcm
         self.throw_to(item, target_monkey)

      self.holding = []


def init_monkeys(data):
   monkeys = []
   for i in range(0, len(data) - 1, 7):
      monkeys.append(Monkey(data[i+1:i+7]))
   for monkey in monkeys:
      monkey.monkeys = monkeys
      monkey.lcm = 3
   return monkeys

def get_input(path):
   data = None
   with open(path) as f:
      data = f.readlines()
   return data

def d11_1(monkeys):
   for i in range(20):
      for monkey in monkeys:
         monkey.run()

   monkey_biz = [monkey.inspected for monkey in monkeys]
   monkey_biz.sort()
   top_two = monkey_biz[-2:]
   for monkey in monkeys:
      monkey.inspected = 0
   return top_two[0] * top_two[1]


# ===

def setup2(monkeys):
   factors = []
   for monkey in monkeys:
      factors.append(monkey.divisor)

   lcm = 1
   for prime in factors:
      lcm *= prime
   print("LCM", lcm)

   for monkey in monkeys:
      monkey.lcm = lcm


def d11_2(monkeys):
   
   setup2(monkeys)
   for i in range(10000):
      for monkey in monkeys:
         monkey.run()

   monkey_biz = [monkey.inspected for monkey in monkeys]
   monkey_biz.sort()
   print(monkey_biz)
   top_two = monkey_biz[-2:]
   return top_two[0] * top_two[1]



if __name__ == '__main__':
   res1 = 'res.txt'
   res2 = 'sample.txt'

   data = get_input(res1)
   monkeys = init_monkeys(data)

   #pr1 = d11_1(monkeys)
   pr2 = d11_2(monkeys)

   #print("Result 1: ", pr1)
   print("Target: 2713310158")
   print("Result:", pr2)
