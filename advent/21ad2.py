file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/21ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(x), text.split("\n")))
file.close()


# starting_cood = [0, 0]
# for i in range(len(inp)):
#   for j in range(len(inp[0])):
#     if inp[i][j] == "S":
#       starting_cood = [i, j]
# starting_set = set()

# queue = [{f"{starting_cood[0]}_{starting_cood[1]}"}]
# evens = set()
# odds = set()
# counter = 0
# length = 64
# while queue:
#   step_possibilies_set = queue.pop(0)
#   step_possibilies = list(map(lambda x: list(map(lambda y: int(y), x.split("_"))), step_possibilies_set))
#   new_step:set[str] = set()
#   current_pol = evens if counter % 2 == 0 else odds
#   next_pol = evens if counter % 2 == 1 else odds
#   for [y, x] in step_possibilies:
#     new_possibilities = [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]
#     for [yy, xx] in new_possibilities:
#       string_cood = f"{yy}_{xx}"
#       if inp[yy%len(inp)][xx%len(inp[0])] == "#" or string_cood in next_pol: continue
#       new_step.add(string_cood)
#     current_pol.add(f"{y}_{x}")
#   queue.append(new_step)
#   # for key in next_pol:
#   #   [y, x] = list(map(lambda y: int(y), key.split("_")))
#   #   new_possibilities = [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]
#   #   chars = list(map(lambda x: inp[x[0]%len(inp)][x[1]%len(inp[0])], new_possibilities))
#   #   flag = False
#   #   for char in chars:
#   #     if char == ".":
#   #       flag = True
#   #       break
#   #   if not flag: next_pol.remove(key)
#   counter += 1
# print(len(queue[0]) + (len(evens) if length % 2 == 0 else len(odds)))
l = len(inp)
e = (((((26501365 - l//2)//l) * 2 + 1) ** 2) // 4) * (7421 + 7450)
o = (((((26501365 - l//2)//l) * 2 + 1) ** 2) // 2 + 1) * 3776
print(e+3776)

#608602995997076
#608152815581776