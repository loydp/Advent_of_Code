class Board:
   def __init__(self, dimension, board) -> None:
      '''takes in lists of numbers on the board. puts them in:
      1. A dictionary where the key is the number and the value is the coordinates
      2. An array'''
      self.num_dict = {}
      self.arr = board
      for i in range(len(board)):
         for j in range(len(board)):
            self.num_dict[board[i][j]] = (i, j)

   def __str__(self) -> str:
      ret = ''
      for line in self.arr:
         ret += ' '.join(str(x) for x in line) + '\n'
      return ret

   def check_for_win(self, row, col):
      perfect = True
      for i in range(len(self.arr)):
         if self.arr[row][i] != True:
            perfect = False
            break
      if perfect == True:
         return self
      perfect = True
      for i in range(len(self.arr)):
         if self.arr[i][col] != True:
            return False
      return self

   def guess(self, guess):
      result = False
      if guess in self.num_dict:
         row, col = self.num_dict[guess]
         self.arr[row][col] = True
         result = self.check_for_win(row, col)
      return result


   def get_result(self, guess):
      the_sum = 0
      for row in self.arr:
         the_sum += sum([x for x in row if x != True])
      return the_sum * guess

def load_data(addr):
   '''Takes in an address, returns a list of lines note that this contains empty lines
   '''
   with open(addr) as f:
      return f.read().splitlines()

def convert_to_lists(length, data):
   '''Takes in a list of strings with board and guess information,
   returns the same information as ints in lists within those larger categories'''
   guesses = [int(x) for x in data[0].split(',')]
   boards = []
   num_boards = ((len(data) - 1) // (length + 1))
   for i in range(num_boards):
      start = (i * (length + 1)) + 2
      board = [[int(y) for y in x.split()] for x in data[start:start + length]]
      boards.append(board)
   
   for i in range(len(boards)):
      if len(boards[i]) == 0:
         print(i)
         break
      

   return guesses, boards

def instantiate_boards(dimension, num_arrs):
   boards = []
   for num_arr in num_arrs:
      boards.append(Board(dimension, num_arr))
   return boards


def play_bingo(boards, guesses):
   result = False
   for guess in guesses:
      for board in boards:
         result = board.guess(guess)
         if result != False:
            return result, guess
   print("couldn't find a winner")
   return result, guess

def lose_bingo(boards, guesses):
   '''
   For each board
   check each guess against it, tracking how many guesses so far
   Once it is complete, check if it's the current most losing
   record if it is.'''
   max = 0
   current = 0
   nominee = None
   for board in boards:
      for guess in guesses:
         current += 1
         result = board.guess(guess)
         if result != False:
            if current > max:
               nominee = result
               max = current
            current = 0
            break
   return nominee, guesses[max - 1]


if __name__ == "__main__":
   # get data
   addr = 'data.txt'
   dimension = 5
   data = load_data(addr)

   # convert to guesses and boards
   guesses, raw_boards = convert_to_lists(dimension, data)
   boards = instantiate_boards(dimension, raw_boards)

   # apply each guess to the boards until a winner is found
   winner, guess = play_bingo(boards, guesses)
   printable = winner.get_result(guess)
   print(printable)

   loser, guess = lose_bingo(boards, guesses)
   printable = loser.get_result(guess)
   print(printable)