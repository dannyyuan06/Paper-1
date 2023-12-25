file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/25/25ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(map(lambda y: y.split(" "), x.split(": "))), text.split("\n")))
file.close()

graph = {}
for [[name], connections] in inp:
  if name not in graph: graph[name] = []
  for connection in connections:
    if connection not in graph: graph[connection] = []
    graph[name].append(connection)
    graph[connection].append(name)
    

visited = set() # Set to keep track of visited nodes of graph.
total = 0
def dfs(visited, graph, node):  #function for dfs 
    global total
    if node not in visited:
        total += 1
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code

dfs(visited, graph, 'lqs')
print(total)