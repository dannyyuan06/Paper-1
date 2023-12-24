
file = open("C:/Computer Science/Paper 1/advent/11ad.txt", "r")
text = file.read()
inp = text.split("\n")
file.close()

spaces = [False] * len(inp[0])

new_inp = []

for i in range(len(inp)):
  line = inp[i]
  flag = False
  for j in range(len(line)):
    char = line[j]
    if char == "#":
      spaces[j] = True
      flag = True
  if not flag:
    new_inp.append(line)
  new_inp.append(line)

new_new_inp = []
for i in range(len(new_inp)):
  line = new_inp[i]
  row = ""
  for j in range(len(line)):
    char = line[j]
    row += char
    if spaces[j]: row += "."
  new_new_inp.append(row)

     #Initialize a queue

def bfs(ognode, graph): #function for BFS
  visited = {}
  node = ognode
  queue = [node]
  node_key = "_".join(list(map(lambda x: str(x), node)))
  visited[node_key] = True
  found = []
  while queue:          # Creating loop to visit each node
    node = queue.pop(0)
    if graph[node[0]][node[1]] == "#" and node != ognode:
      found.append([node, abs(node[0] - ognode[0]) + abs(node[1] - ognode[1]) - 1])
    coordinates = [[node[0]+1, node[1]], [node[0], node[1]+1], [node[0]-1, node[1]], [node[0], node[1]-1]]
    for coordinate in coordinates:
      coordinates_key = "_".join(list(map(lambda x: str(x), coordinate)))
      if coordinates_key not in visited and coordinate[0] >= 0 and coordinate[0] < len(graph) and coordinate[1] >= 0 and coordinate[1] < len(graph[0]):
        visited[coordinates_key] = True
        queue.append(coordinate)
    print(queue)
  return found

shortest_paths = {}
for i in range(len(new_new_inp)):
  for j in range(len(new_new_inp[i])):
    char = new_new_inp[i][j]
    if char == "#":
      coordinate = [i, j]
      coordinate_key = f"{str(i)}_{str(j)}"
      founds = bfs(coordinate, new_new_inp)
      for found in founds:
        found_coordinate = found[0]
        found_coordinate_key = f"{str(found_coordinate[0])}_{str(found_coordinate[1])}"
        coordinate_pair = [coordinate_key, found_coordinate_key]
        coordinate_pair.sort()
        shortest_paths["__".join(coordinate_pair)] = found[1]

total = 0
for key in shortest_paths:
  total += shortest_paths[key]

print(total)

      
