file = open("C:/Computer Science/Paper 1/advent/16ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(map(lambda y: [y, []], x)), text.split("\n")))
file.close()

def run_check(text, y_coord,  x_coord, dir):
  inp = list(map(lambda x: list(map(lambda y: [y, []], x)), text.split("\n")))
  beams = [[y_coord, x_coord, dir]]
  while beams:
    i = 0
    while i < len(beams):
      beam = beams[i]
      [y, x, direction] = beam
      if direction == "r": x += 1
      elif direction == "l": x -= 1
      elif direction == "u": y -= 1
      elif direction == "d": y += 1
      if x < 0 or x >= len(inp[0]):
        beams.pop(i)
        continue
      if y < 0 or y >= len(inp):
        beams.pop(i)
        continue
      [char, prev] = inp[y][x]
      if direction in prev:
        beams.pop(i)
        continue
      else: inp[y][x][1].append(direction)
      if direction == "r":
        if char == "/": direction = "u"
        elif char == "\\": direction = "d"
        elif char == "|":
          direction = "u"
          beams.append([y, x, "d"])
      elif direction == "l":
        if char == "/": direction = "d"
        elif char == "\\": direction = "u"
        elif char == "|":
          direction = "d"
          beams.append([y, x, "u"])
      elif direction == "d":
        if char == "/": direction = "l"
        elif char == "\\": direction = "r"
        elif char == "-":
          direction = "r"
          beams.append([y, x, "l"])
      elif direction == "u":
        if char == "/": direction = "r"
        elif char == "\\": direction = "l"
        elif char == "-":
          direction = "l"
          beams.append([y, x, "r"])
      beams[i] = [y, x, direction]
      i += 1
  
  total = 0
  for line in inp:
    for char in line:
      if len(char[1]) != 0:
        total += 1
  return total

max = 0
for i in range(len(inp)):
  r1 = run_check(text, i, -1, "r")
  if r1 > max: max = r1
  r2 = run_check(text, i, len(inp[0]), "l")
  if r2 > max: max = r2

for i in range(len(inp[0])):
  r1 = run_check(text, -1, i, "d")
  if r1 > max: max = r1
  r2 = run_check(text, len(inp[0]), i, "u")
  if r2 > max: max = r2

print(max)