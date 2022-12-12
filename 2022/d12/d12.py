def get_input(path):
   data = None
   with open(path) as f:
      data = f.read().split()
   return data

def process_input(data):
   #print(data)
   for i in range(len(data)):
      data[i] = [ord(x) - 97 for x in data[i]]
   start = None
   end = None
   for i in range(len(data)):
      for j in range(len(data[0])):
         if data[i][j] == -14:
            start = (i, j)
            data[i][j] = 0
         elif data[i][j] == -28:
            end = (i, j)
            data[i][j] = 25
   
   return start, end, data

from collections import deque

def get_directions(point):
   return [(point[0], point[1] + 1), (point[0], point[1] - 1), (point[0] + 1, point[1]), (point[0] - 1, point[1])] 

def get_paths(terrain, prev, visited):
   prev = prev[0]
   directions = []
   height = len(terrain)
   width = len(terrain[0])
   previous_height = terrain[prev[0]][prev[1]]
   for possible in get_directions(prev):
      # if we've already been here, pass on this location
      if possible in visited:
         continue

      # if it's beyond the bounds of the board, pass on this location
      if -1 < possible[0] < height and -1 < possible[1] < width:
         possible_height = terrain[possible[0]][possible[1]]

         # if the height is too far above or below, pass on this location
         if possible_height > previous_height + 1: #or possible_height < previous_height - 1:
            continue
         directions.append((possible, prev))

   return directions


def get_end(end, visited):
   counter = 0
   current = end
   while current != "Start":
      counter += 1
      current = visited[current]

   return counter - 1


def bfs(start, end, terrain):
   visited = {}
   frontier = deque()
   frontier.append((start, "Start"))

   while frontier:
      #print(frontier)
      current = frontier.popleft()
      visited[current[0]] = current[1]
      #print("height:", terrain[current[0][0]][current[0][1]])
      #print("Len frontier:", len(frontier))

      # get all possible paths from the current position
      # this excludes height differences, out of bounds, things in visited
      neighbors = get_paths(terrain, current, visited)
      #print(f"neighbors of {current}: {neighbors}")
      for neighbor in neighbors:
         if neighbor[0] == end:
            visited[neighbor[0]] = neighbor[1]
            return get_end(end, visited)
         else:
            visited[neighbor[0]] = neighbor[1]
            frontier.append(neighbor)
      
   return -1

def d12_1(data):
   k = bfs(data[0], data[1], data[2])

   return k

def d12_2(data):
   _, end, terrain = data
   starts = []

   for i in range(len(terrain)):
      for j in range(len(terrain[0])):
         if terrain[i][j] == 0:
            starts.append((i, j))
   results = [bfs(start, end, terrain) for start in starts]
   min_path = min(list(filter(lambda x: x != -1, results)))
   return min_path

   

if __name__ == '__main__':
   input1 = 'res.txt'
   input2 = 'sample.txt'
   data = get_input(input1)
   data = process_input(data)
   #pr = d12_1(data)
   pr = d12_2(data)
   print(pr)