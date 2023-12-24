file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/23/23ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(x),text.split("\n")))
file.close()

queue = [[0, 1, 1]]
junctions = set()
directions = {">": 0, "v": 1, "<": 2, "^":3} 
for i in range(len(inp)):
  for j in range(len(inp[i])):
    char = inp[i][j]
    if char == "#": continue
    surrounds = [[i, j+1], [i+1, j], [i, j-1], [i-1, j]]
    pathways = 0
    for [y, x] in surrounds:
      if y < 0 or y >= len(inp) or x < 0 or y >= len(inp[0]): continue
      ad_char = inp[y][x]
      if ad_char in directions: pathways += 1
    if pathways > 2:
      junctions.add(str([i, j]))
      for k in range(len(surrounds)):
        [y, x] = surrounds[k]
        if y < 0 or y >= len(inp) or x < 0 or y >= len(inp[0]): continue
        ad_char = inp[y][x]
        if ad_char != "#" :
          queue.append([i, j, k])
          
start_junction = str([0, 1])
final_junction = str([len(inp)-1, len(inp[0])-2])
junctions.add(start_junction)
junctions.add(final_junction)
def find_distance(position, direction, junctions, inp):
  current_dir = direction
  current_pos = position
  walks = 1
  pot_paths = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  current_pos = [current_pos[0] + pot_paths[direction][0], current_pos[1] + pot_paths[direction][1]]
  while str(current_pos) not in junctions:
    back_direction = (current_dir - 2) % 4
    for i in range(len(pot_paths)):
      if i == back_direction: continue
      pot_path = pot_paths[i]
      new_path = [current_pos[0] + pot_path[0], current_pos[1] + pot_path[1]]
      [y, x] = new_path
      if y < 0 or y >= len(inp) or x < 0 or y >= len(inp[0]): continue
      ad_char = inp[y][x]
      if ad_char != "#":
        current_pos = new_path
        current_dir = i
        break
    walks += 1

  return walks, current_pos

ad_mat = {}
ad_mat[str([len(inp)-1, len(inp[0])-2])] = {}
for [y, x, d] in queue:
  label = str([y, x])
  if label not in ad_mat:
    ad_mat[label] = {}
  cost, des = find_distance([y, x], d, junctions, inp)
  ad_mat[label][str(des)] = cost


visited = set() # Set to keep track of visited nodes of graph.
def dfs(visited, graph, node, total, max_total):  #function for dfs
  if node == final_junction:
    return total
  if node not in visited:
    visited.add(node)
    for neighbour in graph[node]:
      max_total = max(max_total, dfs(visited, graph, neighbour, total + graph[node][neighbour], max_total))
    visited.remove(node)
  return max_total

print(dfs(visited, ad_mat, "[0, 1]", 0, 0))