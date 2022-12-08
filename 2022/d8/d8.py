
def get_input(path):
   data = None
   with open(path) as file:
      data = file.read().split("\n")
   data = [list(map(int, list(letter))) for letter in data]
   return data

def process_row(row, row2):
   height = row[0] - 1
   for i in range(len(row)):
      if row[i] > height:
         row2[i] = 1
         height = row[i]

def process_rows(m1, m2):
   for _ in range(4):
      for k in range(len(m1)):
         process_row(m1[k], m2[k])
      m1 = [[m1[j][i] for j in range(len(m1))] for i in range(len(m1[0])-1,-1,-1)]
      m2 = [[m2[j][i] for j in range(len(m2))] for i in range(len(m2[0])-1,-1,-1)]

   return m1, m2

def d8_1(matrix):
   matrix2 = [[0 for h in range(len(matrix[0]))] for l in range(len(matrix))]
   m1, m2 = process_rows(matrix, matrix2) 
   return sum([sum(row) for row in m2])

'''
# --- --- ---
'''


def find_visible(row1, row2):
   prev = []
   for i, height in enumerate(row1):
      if not prev:
         prev.append([i, height])
      elif prev and height <= prev[-1][1]:
         prev.append([i, height])
      else:
         while prev and height > prev[-1][1]:
            prev.pop()
         if prev:
            row2[i] *= i - prev[-1][0]
         else:
            if i != 0:
               row2[i] *= i
         prev.append([i, height])

def d8_2(matrix):
   pr = 0
   m1 = matrix
   m2 = [[1 for cell in row] for row in m1]

   for _ in range(4):
      for k in range(len(m1)):
         find_visible(m1[k], m2[k])
      m1 = [[m1[j][i] for j in range(len(m1))] for i in range(len(m1[0])-1,-1,-1)]
      m2 = [[m2[j][i] for j in range(len(m2))] for i in range(len(m2[0])-1,-1,-1)]

   for i in range(len(m2)):
      for j in range(len(m2[0])):
         if i == 0 or j == 0 or i == len(m2) - 1 or j == len(m2[0]) - 1:
            m2[i][j] = 0
   return max([max(row) for row in m2])


if __name__ == '__main__':
   path1 = 'res.txt'
   path2 = 'sample.txt'
   data = get_input(path1)
   res1 = d8_1(data)
   res2 = d8_2(data)
   print(res2)
   print(res1)