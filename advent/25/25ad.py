import graphviz

file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/25/25ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(map(lambda y: y.split(" "), x.split(": "))), text.split("\n")))
file.close()

dot = graphviz.Digraph(comment='Wires', graph_attr={"ranksep": "30", "nodesep": ""})



graph = {}
for [[name], connections] in inp:
  dot.node(name)
  for connection in connections:
    dot.node(connection)
    dot.edge(name, connection)
dot.render('/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/25/graph.gv').replace('\\', '/')