file = open("C:/Computer Science/Paper 1/advent/3ad.txt", "r")

inp = []

for line in file:
  inp.append(line[:-1]+'.')
print(inp[2])
  
file.close()

def check_spot(pointer_x, pointer_y, length, inp):
  coods = [[pointer_x - 1, pointer_y - 1], [pointer_x - 1, pointer_y], [pointer_x - 1, pointer_y + 1]]
  for i in range(length):
    coods.append([pointer_x + i, pointer_y + 1])
    coods.append([pointer_x + i, pointer_y - 1])
  coods.append([pointer_x + length, pointer_y - 1])
  coods.append([pointer_x + length, pointer_y])
  coods.append([pointer_x + length, pointer_y + 1])
  gears = []
  for cood in coods:
    if cood[0] >= 0 and cood[1] >= 0 and cood[0] < len(inp[0]) and cood[1] < len(inp):
      char = inp[cood[1]][cood[0]]
      if char == '*':
        gears.append(cood)
  return gears

gears = {}
total = 0
for i in range(len(inp)):
  line = inp[i]
  num_start = -1
  num_buffer = ""
  for j in range(len(line)):
    char = line[j]
    if char.isdigit():
      if num_start == -1: num_start = j
      num_buffer += char
    elif num_buffer != "":
      coods = check_spot(num_start, i, len(num_buffer), inp)
      if len(coods) != 0:
        for cood in coods:
          if (str(cood[0]) + '_' + str(cood[1])) in gears.keys():
            gears[str(cood[0]) + '_' + str(cood[1])].append(int(num_buffer))
          else:
            gears[str(cood[0]) + '_' + str(cood[1])] = [int(num_buffer)]
      num_buffer = ""
      num_start = -1

for key in gears:
  if len(gears[key]) == 2:
    total += gears[key][0] * gears[key][1]

print(total)      

    