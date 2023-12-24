from itertools import combinations 
import re
file = open("C:/Computer Science/Paper 1/advent/12ad.txt", "r")
text = file.read()
inp = list(map(lambda x: [((str(x.split(" ")[0]) + "?")*5)[:-1], list(map(lambda y: int(y), x.split(" ")[1].split(","))) * 5], text.split("\n")))
file.close()

print(inp[0])
def all_permutaions(max, count) :
  perms = []
  for positions in combinations(range(max), count):
    print("hello")
    p = ["0"] * max
    for position in positions:
      p[position] = "1"
    perms.append(p)
  return perms


total = 0
counter = 0
for line in inp:
  print(counter)
  num_broken = str(line[0]).count("#")
  num_unknown = str(line[0]).count("?")
  total_num_comb = sum(line[1]) - num_broken
  for positions in combinations(range(num_unknown), total_num_comb):
    print(positions)
    p = ["0"] * num_unknown
    line_copy = line[0]
    for position in positions:
      p[position] = "1"
    comb = p
    for i in range(len(comb)):
      if comb[i] == "1": line_copy = line_copy.replace("?", "#", 1)
      else: line_copy = line_copy.replace("?", ".", 1)
    spli = re.split(r'\.+', line_copy)
    if spli[0] == "": spli = spli[1:]
    if spli[-1] == "": spli = spli[:-1]
    flag = False
    for i in range(len(line[1])):
      if i >= len(spli):
        flag = True
        break
      if len(spli[i]) != line[1][i]:
        flag = True
        break
    if not flag: total += 1
  counter += 1
print(total)