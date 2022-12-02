def get_strategy():
   lines = []
   with open('resources/res.txt') as f:
      lines = f.readlines()
      lines = [(line[0], line[2]) for line in lines]
   return lines

def get_score(strat):
   summary = 0
   scoring = {
      'X' : 0,
      'Y' : 3,
      'Z' : 6
   }
   summary += scoring[strat[1]]
   guess_score = {'A' : 1, 'B':2, 'C':3}

   def solve(letter, command):
      letters = ['A', 'B', 'C']
      if command == "X":
         pos = letters.index(letter) - 1
         if pos == -1:
            pos = 2
         return letters[pos]
      elif command == "Y":
         return letter
      else:
         pos = letters.index(letter) + 1
         if pos == 3:
            pos = 0
         return letters[pos]

   summary += guess_score[solve(strat[0], strat[1])]
   return summary


if __name__ == "__main__":
   strategy_guide = get_strategy()
   '''
   strategy_guide = [
      ('A', 'Y'),
      ('B', 'X'),
      ('C', 'Z')
   ]
   '''
   guess_score = {'X' : 1, 'Y':2, 'Z':3}
   result_score = {
      ('A', 'X') : 3, 
      ('A', 'Y') : 6,
      ('A', 'Z') : 0,
      ('B', 'X') : 0, 
      ('B', 'Y') : 3, 
      ('B', 'Z') : 6,
      ('C', 'X') : 6,
      ('C', 'Y') : 0,
      ('C', 'Z') : 3
      }
   result = [guess_score[x[1]] + result_score[x] for x in strategy_guide]
   print(sum(result))
   result2 = [get_score(strat) for strat in strategy_guide]
   print(sum(result2))