file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/20ad.txt", "r")
text = file.read()
inp = list(map(lambda x: x.split(" -> "), text.split("\n")))
file.close()

graph = {}

class Signal:
  def __init__(self, source: str, destination: str, signal_type: bool) -> None:
    self.source = source
    self.destination = destination
    self.signal_type = signal_type

class Broadcaster:
  def __init__(self, connections: list[str], name:str) -> None:
    self.connections = connections
    self.name = name
  
  def relay(self, _: Signal):
    return list(map(lambda x: Signal("broadcaster", x, False), self.connections))

class Flip_flop:
  def __init__(self, connections: list[str], name:str) -> None:
    self.connections = connections
    self.state = False
    self.name = name

  def relay(self, signal: Signal):
    if not signal.signal_type:
      self.state = not self.state
      return list(map(lambda x: Signal(self.name, x, self.state), self.connections))
    return []

class Conjunction:
  def __init__(self, connections: list[str], name:str) -> None:
    self.connections = connections
    self.inverse_connections = {}
    self.name = name
    
  def add_inverse_connection(self, node: str):
    self.inverse_connections[node] = False

  def relay(self, signal: Signal):
    self.inverse_connections[signal.source] = signal.signal_type
    flag = True
    for value in self.inverse_connections.values():
      if not value: flag = False
    if flag: return list(map(lambda x: Signal(self.name, x, False), self.connections))
    return list(map(lambda x: Signal(self.name, x, True), self.connections))
    
    
for [label, connections] in inp:
  connections = connections.split(", ")
  if label == "broadcaster":
    graph[label] = Broadcaster(connections, label)
  else:
    type_of_node = label[0]
    label = label[1:]
    if type_of_node == "%": graph[label] = Flip_flop(connections, label)
    else: graph[label] = Conjunction(connections, label)

for key in graph:
  value = graph[key]
  for connection in value.connections:
    if connection not in graph: continue
    node = graph[connection]
    if type(node) == Conjunction: node.add_inverse_connection(key)

low_total = 0
high_total = 0
for _ in range(1000):
  queue: list[Signal] = [Signal("420", "broadcaster", False)]
  while queue:
    item = queue.pop(0)
    # print(item.source, item.signal_type, item.destination)
    if item.signal_type: high_total += 1
    else: low_total += 1
    if item.destination not in graph: continue
    destination = graph[item.destination]
    new_signals = destination.relay(item)
    queue.extend(new_signals)

print(low_total * high_total)