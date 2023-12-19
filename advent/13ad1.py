file = open("C:/Computer Science/Paper 1/advent/13ad.txt", "r")
text = file.read()
inp = list(map(lambda x: x.split("\n"), text.split("\n\n")))
file.close()

total = 0

for puzzle in inp:
  print(total)
  mirrors_vertical = [True] * (len(puzzle[0])-1)
  for line in puzzle:
    for i in range(len(line)-1):
      left_split = line[:i+1]
      right_split = line[i+1:]
      reverse_left_split = left_split[::-1]
      if i < len(line)//2:
        for j in range(len(left_split)):
          if reverse_left_split[j] != right_split[j]:
            mirrors_vertical[i] = False
            break
      else:
        for j in range(len(right_split)):
          if reverse_left_split[j] != right_split[j]:
            mirrors_vertical[i] = False
            break
  mirrors_horizontal = [True] * (len(puzzle)-1)
  for i in range(len(puzzle)-1):
      up_split = puzzle[:i+1]
      down_split = puzzle[i+1:]
      reverse_up_split = up_split[::-1]
      if i < len(puzzle)//2:
        for j in range(len(up_split)):
          if reverse_up_split[j] != down_split[j]:
            mirrors_horizontal[i] = False
            break
      else:
        for j in range(len(down_split)):
          if reverse_up_split[j] != down_split[j]:
            mirrors_horizontal[i] = False
            break
  print(mirrors_horizontal, mirrors_vertical)
  total += 100 * ((mirrors_horizontal.index(True)+1) if True in mirrors_horizontal else 0) + ((mirrors_vertical.index(True) + 1) if True in mirrors_vertical else 0)
print(total)