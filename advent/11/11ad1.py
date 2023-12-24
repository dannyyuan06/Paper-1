
import dis


file = open("C:/Computer Science/Paper 1/advent/11ad.txt", "r")
text = file.read()
inp = text.split("\n")
file.close()

spaces_x = [False] * len(inp[0])
spaces_y = [False] * len(inp)

new_inp = []

for i in range(len(inp)):
  line = inp[i]
  flag = False
  for j in range(len(line)):
    char = line[j]
    if char == "#":
      spaces_x[j] = True
      flag = True
  spaces_y[i] = flag
print(spaces_x, spaces_y)
#Initialize a queue
multiple = 1000000 - 1
total = 0
for i in range(len(inp)):
  for j in range(len(inp[i])):
    char = inp[i][j]
    if char == "#":
      for k in range(len(inp)):
        for l in range(len(inp[k])):
          second_char = inp[k][l]
          if second_char == "#":
            spaces_x_multiple = 0
            spaces_y_multiple = 0
            for m in range(len(spaces_x)):
              if not spaces_x[m] and (m < l and m > j or m < j and m > l): spaces_x_multiple += 1
            for m in range(len(spaces_y)):
              if not spaces_y[m] and (m < k and m > i or m < i and m > k): spaces_y_multiple += 1
            distance = abs(k-i) + abs(l-j) + spaces_x_multiple * multiple + spaces_y_multiple * multiple
            total += distance
          

print(total//2)

      
