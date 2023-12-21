file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/18ad.txt", "r")
text = file.read()
inp = list(map(lambda x: x.split(" "), text.split("\n")))
file.close()
width = 400

total = 0

current_cood = [0, 0]
total_matrix = []
for i in range(len(inp)):
  [_, _, hex] = inp[i]
  [_, _, prev_hex] = inp[i-1]
  hex = hex[2:-1]
  prev_hex = prev_hex[2:-1]
  hex_direction = hex[-1]
  prev_hex_direction = prev_hex[-1]
  direction_map = ["R", "D", "L", "U"]
  direction = direction_map[int(hex_direction)]
  prev_direction = direction_map[int(prev_hex_direction)]
  length = int(hex[:-1], 16)
  comb = prev_direction + direction
  dic = {
    "UL": [1, 0],
    "UR": [0, 0],
    "DL": [1, 1],
    "DR": [0, 1],
    "LU": [1, 0],
    "LD": [1, 1],
    "RU": [0, 0],
    "RD": [0, 1]
  }
  added_matrix = dic[comb]
  coord_matrix = [current_cood[0] + added_matrix[0], current_cood[1] + added_matrix[1]]
  total_matrix.append(coord_matrix)
  
  if direction == "U": current_cood[0] -= length
  elif direction == "D": current_cood[0] += length
  elif direction == "R": current_cood[1] += length
  elif direction == "L": current_cood[1] -= length

running_total = 0
for i in range(len(total_matrix)):
  current_cood = total_matrix[i-1]
  next_cood = total_matrix[i]
  running_total += current_cood[0] * next_cood[1] - current_cood[1] * next_cood[0]

print(abs(running_total)//2)
