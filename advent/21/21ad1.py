import copy


file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/21ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(x), text.split("\n")))
file.close()

inp_copy = copy.deepcopy(inp)

starting_cood = [0, 0]
for i in range(len(inp)):
  for j in range(len(inp[0])):
    if inp[i][j] == "S":
      starting_cood = [i, j]
starting_set = set()

queue = [{f"{starting_cood[0]}_{starting_cood[1]}"}]
counter = 0
for _ in range(130):
  step_possibilies_set = queue.pop(0)
  step_possibilies = list(map(lambda x: list(map(lambda y: int(y), x.split("_"))), step_possibilies_set))
  new_step:set[str] = set()
  for [y, x] in step_possibilies:
    new_possibilities = [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]
    for [yy, xx] in new_possibilities:
      if yy < 0 or yy >= len(inp) or xx < 0 or xx >= len(inp[0]) or inp[yy][xx] == "#": continue
      new_step.add(f"{yy}_{xx}")
  queue.append(new_step)
  counter += 1
  
for i in queue[0]:
  coods = list(map(lambda y: int(y), i.split("_")))
  inp_copy[coods[0]][coods[1]] = "A"
print(len(queue[0]))

out = "\n".join(list(map(lambda x: "".join(x), inp_copy)))

file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/21adOut.txt", "w")
file.write(out)
file.close()