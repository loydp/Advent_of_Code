
def acquire_data(addr):
   with open(addr) as f:
      return list(map(int, f.read().split(',')))


def age(pop) -> list:
   temp = pop[0]
   for i in range(8):
      pop[i] = pop[i + 1]
   pop[6] += temp
   pop[8] = temp
   return pop


if __name__ == '__main__':
   '''
   Models lanternfish populations.
   Takes in a list of current stages of lanternfish. These are 7/day lanternfish
   Lanternfish, on being created:
   8 (before creation)
   count down to 0
   then move back to 6 (7 days left), creating new lanternfish at 8

   '''
   addr = 'data.txt'
   num_days = 256

   # get data
   data = acquire_data(addr)   

   # create a list, and in each bucket have that number.
   population = [0] * 9
   for i in data:
      population[i] += 1

   # x times, decrement the number, with the constraints defined
   for _ in range(num_days):
      population = age(population)
   total = sum(population)
   print(total)