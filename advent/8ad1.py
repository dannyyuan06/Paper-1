from math import gcd


file = open("C:/Computer Science/Paper 1/advent/8ad.txt", "r")
text = file.read()
inp = text.split("\n\n")
file.close()

instr = inp[0]

graph = inp[1].split("\n")
graph_dic = {}

current_nodes = []


for node in graph:
  split_1 = node.split(" = ")
  split_2 = split_1[1].split(", ")
  graph_dic[split_1[0]] = [split_2[0][1:], split_2[1][:-1]]
  
  if split_1[0][-1] == "A": current_nodes.append(split_1[0])


counter = 0

loop = [0] * len(current_nodes)



while 0 in loop:
  direction = 1 if instr[counter % len(instr)] == "R" else 0
  for i in range(len(current_nodes)):
    current_node = current_nodes[i]
    current_nodes[i] = graph_dic[current_node][direction]
    if current_node[-1] == "Z" and loop[i] == 0: loop[i] = counter
  counter += 1

lc = 1
for i in loop:
  lc = lc*i//gcd(lc, i)
  
print(lc)