file = open("C:/Computer Science/Paper 1/advent/15ad.txt", "r")
text = file.read()
inp = list(map(lambda x: x, text.split(",")))
file.close()

def hash(inp):
  current_val = 0
  for char in inp:
    current_val += ord(char)
    current_val = current_val*17%256
  return current_val

boxes = []
for i in range(256):
  boxes.append([])
for lens in inp:
  if "-" in lens:
    label = lens[:-1]
    index = hash(label)
    box = boxes[index]
    labels = list(map(lambda x: x[0], box))
    if label in labels:
      boxes[index].pop(labels.index(label))
  elif "=" in lens:
    [label, focal] = lens.split("=")
    index = hash(label)
    box = boxes[index]
    labels = list(map(lambda x: x[0], box))
    if label in labels:
      boxes[index][labels.index(label)] = [label, int(focal)]
    else:
      boxes[index].append([label, int(focal)])
      
total = 0
for i in range(len(boxes)):
  box = boxes[i]
  for j in range(len(box)):
    lens = box[j]
    total += (i+1)*(j+1)*lens[1]
print(total)