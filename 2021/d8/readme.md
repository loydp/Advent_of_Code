Very messy.

Sort by top for clever solutions if I want to redo:
https://www.reddit.com/r/adventofcode/comments/rbj87a/2021_day_8_solutions/

See this, and remember set operations: & - | < > >= <=

General approach seems to be, take 1 and 4, or 4 and 2 here, and find the number of numbers in common with them.

s = 0
for x,y in [x.split('|') for x in open(0)]:  # split signal and output
  l = {len(s): set(s) for s in x.split()}    # get number of segments

  n = ''
  for o in map(set, y.split()):              # loop over output digits
    match len(o), len(o&l[4]), len(o&l[2]):  # mask with known digits
      case 2,_,_: n += '1'
      case 3,_,_: n += '7'
      case 4,_,_: n += '4'
      case 7,_,_: n += '8'
      case 5,2,_: n += '2'
      case 5,3,1: n += '5'
      case 5,3,2: n += '3'
      case 6,4,_: n += '9'
      case 6,3,1: n += '6'
      case 6,3,2: n += '0'
  s += int(n)

print(s)