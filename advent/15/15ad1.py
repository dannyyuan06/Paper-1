file = open("C:/Computer Science/Paper 1/advent/15ad.txt", "r")
text = file.read()
inp = list(map(lambda x: x, text.split(",")))
file.close()

def hash(inp):
  current_val = 0
  for char in inp:
    current_val += ord(char)
    current_val = current_val*17%256
  return current_val
  
total = 0
for ins in inp:
  total += hash(ins)
print(total)