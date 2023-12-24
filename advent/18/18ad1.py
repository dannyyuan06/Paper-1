import sys

file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/18ad.txt", "r")
text = file.read()
inp = list(map(lambda x: x.split(" "), text.split("\n")))
file.close()
width = 400

sys.setrecursionlimit(100000)

total = 0
grid = []
for i in range(width):
  row = []
  for j in range(width):
    row.append(".")
  grid.append(row)
start = [200, 100]
current_cood = start
for [direction, length, _] in inp:
  length = int(length)
  grid[current_cood[0]][current_cood[1]] = "#"
  for i in range(1, length+1):
    total += 1
    if direction == "U": current_cood[0] -= 1
    elif direction == "D": current_cood[0] += 1
    elif direction == "R": current_cood[1] += 1
    elif direction == "L": current_cood[1] -= 1
    grid[current_cood[0]][current_cood[1]] = "#"
    
# hz_in = [False] * width
# for i in range(len(grid)):
#   vt_in = False
#   prev_vt_in = False
#   for j in range(len(grid[i])):
#     char = grid[i][j]
#     if char == "#":
#       vt_in = not vt_in
q = [[201, 103]]
been = set()
def to_key(li):  return "_".join(list(map(str, li)))
while q:
  current_pos = q.pop(0)
  total += 1
  positions = [[current_pos[0]+1, current_pos[1]], [current_pos[0]-1, current_pos[1]], [current_pos[0], current_pos[1]+1], [current_pos[0], current_pos[1]-1]]
  for position in positions:
    if grid[position[0]][position[1]] != "#" :
      q.append(position)
      grid[position[0]][position[1]] = "#"
      
print(total-1)
  
  
  

file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/18adOut.txt", "w", encoding="utf-8")
file.write("\n".join(list(map(lambda x: "".join(x), grid))))
file.close()
