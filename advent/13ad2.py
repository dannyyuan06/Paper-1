file = open("C:/Computer Science/Paper 1/advent/13ad.txt", "r")
text = file.read()
inp = list(map(lambda x: x.split("\n"), text.split("\n\n")))
file.close()

total = 0

for puzzle in inp:
  print(total)
  mirrors_vertical = [0] * (len(puzzle[0])-1)
  for line in puzzle:
    for i in range(len(line)-1):
      left_split = line[:i+1]
      right_split = line[i+1:]
      reverse_left_split = left_split[::-1]
      if i < len(line)//2:
        for j in range(len(left_split)):
          if reverse_left_split[j] != right_split[j]:
            mirrors_vertical[i] += 1
      else:
        for j in range(len(right_split)):
          if reverse_left_split[j] != right_split[j]:
            mirrors_vertical[i] += 1
  mirrors_horizontal = [0] * (len(puzzle)-1)
  
  def check_row(row_1, row_2):
    incorrect = 0
    for i in range(len(row_1)):
      if row_1[i] != row_2[i]:
        incorrect += 1
    return incorrect
  for i in range(len(puzzle)-1):
      up_split = puzzle[:i+1]
      down_split = puzzle[i+1:]
      reverse_up_split = up_split[::-1]
      if i < len(puzzle)//2:
        for j in range(len(up_split)):
          mirrors_horizontal[i] += check_row(reverse_up_split[j], down_split[j])
      else:
        for j in range(len(down_split)):
          mirrors_horizontal[i] += check_row(reverse_up_split[j], down_split[j])
  print(mirrors_horizontal, mirrors_vertical)
  total += 100 * ((mirrors_horizontal.index(1)+1) if 1 in mirrors_horizontal else 0) + ((mirrors_vertical.index(1) + 1) if 1 in mirrors_vertical else 0)
print(total)