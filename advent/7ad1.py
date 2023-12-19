file = open("C:/Computer Science/Paper 1/advent/7ad.txt", "r")
text = file.read()
inp = list(map(lambda x: x.split(" "),text.split("\n")))
file.close()

def dictionary(a:str):
  dic = {}
  for char in a:
    if char not in dic:
      dic[char] = 1
    else: dic[char] += 1
  return dic

def five(a:str) -> bool:
  return a == len(a) * a[0]

def four(a:str) -> bool:
  dic = dictionary(a)
  values = list(dic.values())
  return len(dic) == 2 and (values[0] == 4 or values[1] == 4)

def house(a:str) -> bool:
  dic = dictionary(a)
  values = list(dic.values())
  return len(dic) == 2 and (values[0] == 3 or values[1] == 3)

def three(a:str) -> bool:
  dic = dictionary(a)
  values = list(dic.values())
  return len(dic) == 3 and (values[0] == 3 or values[1] == 3 or values[2] == 3)

def two(a:str) -> bool:
  dic = dictionary(a)
  values = list(dic.values())
  return len(dic) == 3 and (values[0] == 2 or values[1] == 2 or values[2] == 2)

def one(a:str) -> bool:
  dic = dictionary(a)
  return len(dic) == 4

def distinct(a:str) -> bool:
  dic = dictionary(a)
  return len(dic) == 5

def compare(a:str, b:str):
  types = [distinct, one, two, three, house, four, five]
  strengths = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
  a_type = 0
  b_type = 0
  for i in range(len(types)):
    type = types[i]
    if type(a) and a_type == 0: a_type = i
    if type(b) and b_type == 0: b_type = i
  if a_type == b_type:
    for i in range(len(a)):
      if a[i] == b[i]: continue
      a_type += strengths.index(a[i]) - strengths.index(b[i])
      break
  return a_type > b_type

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if compare(arr[j][0], arr[j+1][0]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
 
bubbleSort(inp)
print(inp[:20])
total = 0
for i in range(len(inp)):
  total += int(inp[i][1]) * (i+1)

print(total)