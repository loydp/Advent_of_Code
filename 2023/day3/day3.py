def get_input(input_path:str):
   ret = []
   with open(input_path) as f:
      ret = f.readlines()
   return ret

input_path = "example.txt"
# input_path = "input.txt"

class Schematic:
   def __init__(self, schematic_data) -> None:
      self.schematics:list[str] = schematic_data
   

   def get_start_stops(line:str):
      ret_list = []
      temp = []

      in_digit = False
      for i, char in enumerate(line):
         if char.isdigit():
            if not in_digit:
               in_digit = True
               temp = i
         else:
            if char == ".":
               if char.in_digit()
               in_digit == False
               temp.append(i)


      return ret_list


   def sol1(self):
      
      for line in self.schematics:
         start_stops = self.get_start_stops(line)
         valid_nums = get_valid_nums(start_stops, self.schematics)
         


      return 0
      


raw_input = get_input(input_path)
schematic = Schematic(raw_input)
res1 = schematic.sol1()