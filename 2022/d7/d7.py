def get_input(path):
   input = None
   with open(path) as f:
      input = f.readlines()
   return input

def process_input(input):
   ret = []
   for line in input:
      pline = line.split()
      ret.append(pline)
   return ret

class Node:
   def __init__(self, dic, name, parent):
      dic[name] = self
      self.name = name
      self.parent = parent
      self.size = 0
      self.children = []


def make_file_structure(commands):
   dic = {}

   root = Node(dic, '/', None)
   current = root

   for command in commands:
      if command[0] != '$':
         temp_node = Node(dic, command[1], current)
         size = 0
         if command[0] != 'dir':
            temp_node.size = int(command[0])
         current.children.append(temp_node)
      if command[1] == 'cd':
         if command[2] != '..':
            current = dic[command[2]]
         else:
            current = current.parent
      
      if command[1] == 'ls':
         continue

   return root, dic

def process_size(root):
   if not root.children:
      return root.size
   root.size = sum([process_size(child) for child in root.children])
   return root.size


def d7_1(root, amt, lst):
   if root.children:
      for child in root.children:
         d7_1(child, amt, lst)
      if root.size <= amt:
         lst.append(root.size)
   return lst

def d7_2(root, amt, lst):
   if root.children:
      for child in root.children:
         d7_2(child, amt, lst)
      if root.size >= amt:
         lst.append(root.size)
         #lst.append((root.size, root.name))
   return lst

def get_amt_needed(curr, total_mem, amt_needed):
   amt_used = curr.size
   amt_free = total_mem - amt_used
   delete_amt = amt_needed - amt_free
   return delete_amt

if __name__ == '__main__':
   input = get_input('res.txt')
   #input = get_input('sample.txt')
   commands = process_input(input)
   root, dic = make_file_structure(commands)
   process_size(root)
   res1 = d7_1(root, 100_000, [])
   print("p1:", sum(res1))
   total_mem = 70000000
   amt_needed = 30_000_000
   delete_amt = get_amt_needed(root, total_mem, amt_needed)
   res2 = d7_2(root, delete_amt, [])
   print("p2: ", min(res2))
   #print(min(res2, key=lambda x: x[0]))
