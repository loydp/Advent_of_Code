
file_path = "resources/res.txt"
def get_stores():
   stores = []
   with open(file_path) as f:
      lines = f.readlines()
      pack = []
      for item in lines:
         if item != "\n":
            pack.append(int(item))
         else:
            stores.append(pack)
            pack = []
      stores.append(pack)
   return stores

def d1_1(stores):
   return max(map(sum, stores))

def d1_2(stores):
   stores = list(map(sum, stores))
   one = max(stores)
   stores.remove(one)
   two = max(stores)
   stores.remove(two)
   three = max(stores)
   return sum([one, two, three])

stores = get_stores()

res = d1_1(stores)
res = d1_2(stores)
print(res)