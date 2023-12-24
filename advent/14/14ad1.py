file = open("C:/Computer Science/Paper 1/advent/14ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(x), text.split("\n")))
file.close()

for i in range(len(inp)):
  line = inp[i]
  for j in range(len(line)):
    char = line[j]
    if char == "O":
      new_y = i - 1
      while new_y >= 0 and inp[new_y][j] == ".":
        new_y -= 1
      inp[i][j] = "."
      inp[new_y+1][j] = "O"

total = 0
total_length = len(inp)
for i in range(len(inp)):
  bottom_index = total_length - i
  total += bottom_index * inp[i].count("O")
print(total)