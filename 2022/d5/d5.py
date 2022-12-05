
def get_diagram(input):
   input.reverse()
   input = [x[1::4] for x in input[:]]
   diagram = [[] for x in range(len(input[0]))]
   for row in input:
      for i in range(len(row)):
         if row[i] != ' ':
            diagram[i].append(row[i])
   return diagram

def clean_moves(input):
   input = [x.split() for x in input]
   input = [list(map(int, [x[1], x[3], x[5]])) for x in input]
   input = [(x, y - 1, z - 1) for x, y, z in input]
   return input

def solve_1(diagram, moves):
   for move in moves:
      for i in range(move[0]):
         diagram[move[2]].append(diagram[move[1]].pop())
   res = ""
   for i in range(len(diagram)):
      res += diagram[i][-1]
   return res

def solve_2(diagram, moves):
   for move in moves:
      end = diagram[move[1]][-move[0]:]
      diagram[move[2]].extend(end)
      diagram[move[1]] = diagram[move[1]][:-move[0]]
   res = ""
   for i in range(len(diagram)):
      res += diagram[i][-1]
   return res

input = None
with open('resources/res.txt') as f:
   input = f.read().split("\n")

height = 0
while input[height][1] != '1':
   height += 1

diagram = get_diagram(input[:height])
moves = clean_moves(input[height + 2:])

diagram2 = [[y for y in x] for x in diagram]
res1 = solve_1(diagram, moves)
res2 = solve_2(diagram2, moves)

print(res1)
print(res2)