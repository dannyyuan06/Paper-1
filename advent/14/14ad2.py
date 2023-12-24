file = open("C:/Computer Science/Paper 1/advent/14ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(x), text.split("\n")))
file.close()

def up(inp):
  for i in range(len(inp)):
    line = inp[i]
    for j in range(len(line)):
      char = line[j]
      if char == "O":
        new_y = i - 1
        while new_y >= 0 and inp[new_y][j] == ".":
          new_y -= 1
        inp[i][j] = "."
        inp[new_y+1][j] = "O"
  return inp

def down(inp):
  for ii in range(len(inp)):
    i = len(inp) - ii - 1
    line = inp[i]
    for j in range(len(line)):
      char = line[j]
      if char == "O":
        new_y = i + 1
        while new_y < len(inp) and inp[new_y][j] == ".":
          new_y += 1
        inp[i][j] = "."
        inp[new_y-1][j] = "O"
  return inp

def right(inp):
  for ii in range(len(inp[0])):
    i = len(inp[0]) - ii - 1
    for j in range(len(inp)):
      char = inp[j][i]
      if char == "O":
        new_x = i + 1
        while new_x < len(inp[0]) and inp[j][new_x] == ".":
          new_x += 1
        inp[j][i] = "."
        inp[j][new_x-1] = "O"
  return inp

def left(inp):
  for i in range(len(inp[0])):
    for j in range(len(inp)):
      char = inp[j][i]
      if char == "O":
        new_x = i - 1
        while new_x >= 0 and inp[j][new_x] == ".":
          new_x -= 1
        inp[j][i] = "."
        inp[j][new_x+1] = "O"
  return inp

cycles = inp
before = 0
caches = {}
caches_array = []
billion = 1000000000
for i in range(billion):
  cycles = right(down(left(up(inp))))
  out = "\n".join(list(map(lambda x: "|".join(x), cycles)))
  if out in caches:
    difference = i - caches[out]
    repeats = billion - caches[out] - 1
    mod = repeats % difference
    inp = list(map(lambda x: x.split("|"), caches_array[mod + caches[out]].split("\n")))
    print(mod + caches[out])
    print(caches[out], i)
    break
  caches_array.append(out)
  caches[out] = i
  

out = "\n".join(list(map(lambda x: "".join(x), cycles)))

file = open("C:/Computer Science/Paper 1/advent/14adOut.txt", "w")
file.write(out)
file.close()

total = 0
total_length = len(inp)
for i in range(len(inp)):
  bottom_index = total_length - i
  total += bottom_index * inp[i].count("O")
print(total)