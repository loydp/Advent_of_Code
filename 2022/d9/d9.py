def get_input(path):
   ret = None
   with open(path) as f:
      ret = f.readlines()
   ret = [line.split() for line in ret]
   ret = [[line[0], int(line[1])] for line in ret]
   return ret

def update_head(head_pos, direction):
   if direction == 'U':
      return (head_pos[0], head_pos[1] + 1)
   elif direction == 'D':
      return (head_pos[0], head_pos[1] - 1)
   elif direction == 'L':
      return (head_pos[0] - 1, head_pos[1])   
   elif direction == 'R':
      return (head_pos[0] + 1, head_pos[1])

def near(head, tail):
   if head[0] > tail[0] - 2 and head[0] < tail[0] + 2 and head[1] > tail[1] -2 and head[1] < tail[1] + 2:
      return True
   return False


def follow(head, tail):
   if head == tail or near(head, tail):
      return tail
   else:
      hx, hy = head
      tx, ty = tail
      dx, dy = hx - tx, hy - ty
      if abs(dx) == 2 and abs(dy) == 2:
         tx = tx + dx//2
         ty = ty + dy//2
      elif abs(dx) > 1:
         tx += dx//2
         ty = hy
      elif abs(dy) > 1:
         ty += dy//2
         tx = hx
      return (tx, ty)


def d9(data, num):
   visited = set([(0, 0)])
   knots = [(0,0) for x in range(num)]
   for command in data:
      for i in range(command[1]):
         for i in range(num):
            if i == 0:
               knots[0] = update_head(knots[0], command[0])
            else:
               knots[i] = follow(knots[i - 1], knots[i])
            visited.add(knots[-1])
   return len(visited)

if __name__ == "__main__":
   data1 = 'res.txt'
   data2 = 'sample.txt'
   data3 = 'custom.txt'
   data = get_input(data1)
   res1 = d9(data, 2)
   res2 = d9(data, 10)
   print(res1)
   print(res2)
