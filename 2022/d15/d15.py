
from collections import deque

def get_input(path):
   data = None
   with open(path) as f:
      data = f.readlines()
   
   data = [line.split() for line in data]
   data = [(line[2], line[3], line[-2], line[-1]) for line in data]

   processed_data = []
   for line in data:
      x1, y1, x2, y2 = line
      x1 = int(x1.split('=')[-1][0:-1])
      x2 = int(x2.split('=')[-1][0:-1])
      y1 = int(y1.split('=')[-1][0:-1])
      y2 = int(y2.split('=')[-1])
      processed_data.append((complex(x1, y1), complex(x2, y2)))
   return processed_data


def combine(seg1, seg2):
   res = []
   s1, s2 = seg1
   n1, n2 = seg2
   if s2 >= n1:
      if s2 >= n2:
         return [(s1, s2)]
      return [(s1, n2)]
   else:
      return [seg1, seg2]


def calc_y_slices(data, y_column, bound = False):
   starts = []
   ends = []
   for datum in data:
      sensor, beacon = datum
      distance = beacon - sensor

      s2b = int(abs(distance.real) + abs(distance.imag))
      s2y = abs(abs(y_column) - abs(int(sensor.imag)))
      x_cutoff = s2b - s2y
      y_span = x_cutoff * 2 + 1
      y_start = int(sensor.real) - x_cutoff

      if bound:
         if y_start < 0: 
            y_start = 0
         if (y_start + y_span) > bound:
            y_start = 20
      if y_span > 0:
         starts.append(y_start)
         ends.append(y_start + y_span)

   return starts, ends

def calc_segments(starts, ends):
   starts.sort()
   ends.sort()

   segments = deque()
   for start, end in zip(starts, ends):
      if len(segments) == 0:
         segments.append((start, end))
      else:
         last = segments.pop()
         results = combine(last, (start, end))
         for item in results:
            segments.append(item)
   segments = [x[1] - x[0] for x in list(segments)]
   return segments


def d15_1(data, y_column):
   starts, ends = calc_y_slices(data, y_column)
   segments = calc_segments(starts, ends)
   return sum(segments) - 1

if __name__ == '__main__':
   '''
   Not my finest work, doesn't appear to work for all y's
   '''

   p0 = "test.txt"
   p1 = "sample.txt"
   p2 = "res.txt"

   y0 = 0
   y2 = 2_000_000

   y1 = 10

   data = get_input(p0)

   pr1 = d15_1(data, y1)
   print(pr1)