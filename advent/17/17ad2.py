from collections import defaultdict
import heapq as heap

file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/17ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(map(lambda y: int(y), list(x))), text.split("\n")))
file.close()

def dik(grid, starting_node):
  def to_key(cood, pre_pos): return "_".join(list(map(lambda x: str(x), cood))) + "__" + pre_pos
  def to_only_key(cood, pre_pos): return "_".join(list(map(lambda x: str(x), cood))) + "__" + (pre_pos[-10:] if len(pre_pos) > 9 else pre_pos)
  def to_cood(key): return list(map(lambda x: int(x), key.split("__")[0].split("_"))), key.split("__")[1]
  pq = []
  node_costs = defaultdict(lambda: float('inf'))
  starting_node_key = to_only_key(starting_node, "")
  starting_node_prev = to_key(starting_node, "")
  starting_weight = 0
  node_costs[starting_node_key] = starting_weight
  heap.heappush(pq, (starting_weight, starting_node_prev))
  
  while pq:
    _, node = heap.heappop(pq)
    coords, directions = to_cood(node)
    current_node_key = to_only_key(coords, directions)
    last_direction = directions[-1] if directions != "" else ""
    adjacent_coords = []
    for i in range(4, 11):
      if last_direction == "l" or last_direction == "r":
        adjacent_coords.append([[coords[0]+i, coords[1]], "d"*i])
        adjacent_coords.append([[coords[0]-i, coords[1]], "u"*i])
      elif last_direction == "u" or last_direction == "d":
        adjacent_coords.append([[coords[0], coords[1]+i], "r"*i])
        adjacent_coords.append([[coords[0], coords[1]-i], "l"*i])
      else:
        adjacent_coords.append([[coords[0]+i, coords[1]], "d"*i])
        adjacent_coords.append([[coords[0]-i, coords[1]], "u"*i])
        adjacent_coords.append([[coords[0], coords[1]+i], "r"*i])
        adjacent_coords.append([[coords[0], coords[1]-i], "l"*i])
    for [coord, new_direction] in adjacent_coords:
      new_directions = directions + new_direction
      coord_key = to_only_key(coord, new_directions)
      if (coord[0] < 0 or coord[0] >= len(grid) or coord[1] < 0 or coord[1] >= len(grid[0])): continue
      weight = 0
      for i in range(len(new_direction)):
        if new_direction[0] == "r": weight += grid[coord[0]][coord[1]-i]
        elif new_direction[0] == "l": weight += grid[coord[0]][coord[1]+i]
        elif new_direction[0] == "d": weight += grid[coord[0]-i][coord[1]]
        elif new_direction[0] == "u": weight += grid[coord[0]+i][coord[1]]
      new_cost = node_costs[current_node_key] + weight
      if node_costs[coord_key] > new_cost:
        node_costs[coord_key] = new_cost
        new_key = to_key(coord, new_directions)
        heap.heappush(pq, (new_cost, new_key))
  return node_costs

min = 99999
costs = dik(inp, [0,0])

for key in costs:
  str_coods = key.split("__")[0]
  if str_coods == f"{len(inp)-1}_{len(inp[0])-1}":
    weight = costs[key]
    if min > weight: min = weight

print(min)

