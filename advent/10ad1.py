import copy
import sys


file = open("C:/Computer Science/Paper 1/advent/10ad.txt", "r")
text = file.read()
inp = text.split("\n")
file.close()

inp_copy = []
for line in inp:
  buffer = []
  for char in line:
    buffer.append(char)
    buffer.append("#")
  inp_copy.append(buffer)
  inp_copy.append(["#"] * len(buffer))

inp = inp_copy
sys.setrecursionlimit(100000)
# find s

current_cood = []
for i in range(len(inp)):
  for j in range(len(inp[i])):
    if inp[i][j] == "S":
      current_cood = [i, j]
      inp[i][j] = "@"

prev_routes = []
routes = []

top = inp[current_cood[0]-2][current_cood[1]]
down = inp[current_cood[0]+2][current_cood[1]]
left = inp[current_cood[0]][current_cood[1]-2]
right = inp[current_cood[0]][current_cood[1]+2]

if top == "|" or top == "7" or top == "F":
  routes.append([current_cood[0]-1, current_cood[1], "up"])
  prev_routes.append([-1, -1, ""])
if down == "|" or down == "L" or down == "J":
  routes.append([current_cood[0]+1, current_cood[1], "down"])
  prev_routes.append([-1, -1, ""])
if left == "-" or left == "F" or left == "L":
  routes.append([current_cood[0], current_cood[1]-1, "left"])
  prev_routes.append([-1, -1, ""])
if right == "-" or right == "7" or right == "J":
  routes.append([current_cood[0], current_cood[1]+1, "right"])
  prev_routes.append([-1, -1, ""])

def find_routes(routes, prev_routes):
  dictionary = {}
  for route in routes:
    key = "_".join(list(map(lambda x: str(x), route[:-1])))
    if key in dictionary:
      dictionary[key] += 1
    else: dictionary[key] = 1
  for route in prev_routes:
    key = "_".join(list(map(lambda x: str(x), route[:-1])))
    if key in dictionary:
      dictionary[key] += 1
    else: dictionary[key] = 1
  for key in dictionary:
    if dictionary[key] == 2 and key != "-1_-1": return True
  return False

while not find_routes(routes, prev_routes):
  prev_routes = copy.deepcopy(routes)
  for i in range(len(routes)):
    route = routes[i]
    char = inp[route[0]][route[1]]
    inp[route[0]][route[1]] = "@"
    if route[2] == "up":
      if char == "7":
        routes[i][1] -= 1
        routes[i][2] = "left"
      elif char == "F":
        routes[i][1] += 1
        routes[i][2] = "right"
      else:
        routes[i][0] -= 1
    elif route[2] == "down":
      if char == "L":
        routes[i][1] += 1
        routes[i][2] = "right"
      elif char == "J":
        routes[i][1] -= 1
        routes[i][2] = "left"
      else: routes[i][0] += 1
    elif route[2] == "right":
      if char == "J":
        routes[i][0] -= 1
        routes[i][2] = "up"
      elif char == "7":
        routes[i][0] += 1
        routes[i][2] = "down"
      else: routes[i][1] += 1
    elif route[2] == "left":
      if char == "L":
        routes[i][0] -= 1
        routes[i][2] = "up"
      elif char == "F":
        routes[i][0] += 1
        routes[i][2] = "down"
      else: routes[i][1] -= 1
for i in range(len(routes)):
    route = routes[i]
    inp[route[0]][route[1]] = "@"

counter = {"counter": 0}
def recurse(point, inp, letter, counter):
  if point[0] < len(inp) and point[0] >= 0 and point[1] < len(inp[0]) and point[1] >= 0 and inp[point[0]][point[1]] != letter and inp[point[0]][point[1]] != "@":
    if inp[point[0]][point[1]] != "#": counter["counter"] += 1
    inp[point[0]][point[1]] = letter
    recurse([point[0], point[1]+1], inp, letter, counter)
    recurse([point[0]+1, point[1]], inp, letter, counter)
    recurse([point[0], point[1]-1], inp, letter, counter)
    recurse([point[0]-1, point[1]], inp, letter, counter)
    recurse([point[0]-1, point[1]-1], inp, letter, counter)
    recurse([point[0]+1, point[1]+1], inp, letter, counter)
    recurse([point[0]-1, point[1]+1], inp, letter, counter)
    recurse([point[0]+1, point[1]-1], inp, letter, counter)

recurse([140, 140], inp, "A", counter)

file = open("C:/Computer Science/Paper 1/advent/10adOut.txt", "w", encoding="utf-8")
file.write("\n".join(list(map(lambda x: "".join(x), inp))))
file.close()

print(counter["counter"])
    

  


