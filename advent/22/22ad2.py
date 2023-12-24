import copy

file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/22/22ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(map(lambda y: list(map(int, y.split(","))), x.split("~"))), text.split("\n")))
file.close()

z_coords = list(map(lambda x: max(x[0][2], x[1][2]), inp))
z_max = max(z_coords)

space = [[[-1 for z in range(z_max+1)] for y in range(10)] for x in range(10)]

total = 0
class Cube:
  def __init__(self, position: list[int], name) -> None:
    [self.x, self.y, self.z] = position
    self.name = name
    space[self.x][self.y][self.z] = name
  
  def __str__(self) -> str:
    return f"{self.name}: {self.x}, {self.y}, {self.z}"
  
  def can_move_down(self):
    return (space[self.x][self.y][self.z - 1] == -1 or space[self.x][self.y][self.z - 1] == self.name) and self.z - 1 > 0
  
  def brick_below(self):
    return space[self.x][self.y][self.z - 1] if self.z - 1 > 0 else -2
  
  def move_down(self):
    space[self.x][self.y][self.z - 1] = self.name
    space[self.x][self.y][self.z] = -1
    self.z -= 1


class Brick:
  def __init__(self, array, name) -> None:
    [pos_1, pos_2] = array
    i_changed = -1
    for i in range(len(pos_1)):
      if pos_1[i] != pos_2[i]: i_changed = i
    i_max = max(pos_1[i_changed], pos_2[i_changed])
    i_min = min(pos_1[i_changed], pos_2[i_changed])
    range_coods = []
    for i in range(i_min, i_max + 1):
      new_cood = copy.deepcopy(pos_1)
      new_cood[i_changed] = i
      range_coods.append(Cube(new_cood, name))
    self.cubes: list[Cube] = range_coods
    self.touching_up_bricks: set[int] = set()
    self.touching_down_bricks: set[int] = set()
    self.name = name
    
  def __str__(self) -> str:
    return str(list(map(str, self.cubes)))
  
  def add_touching_up_brick(self, name):
    self.touching_up_bricks.add(name)
  
  def move_down(self, testing:bool):
    can_move = True
    is_tested = False
    while can_move:
      for cube in self.cubes:
        if not cube.can_move_down():
          can_move = False
          break
      if not can_move:
        for cube in self.cubes:
          brick_below = cube.brick_below()
          if brick_below > -1 and brick_below != self.name:
            bricks[brick_below].add_touching_up_brick(self.name)
            self.touching_down_bricks.add(brick_below)
      else:
        for cube in self.cubes:
          cube.move_down()
        if testing: is_tested = True
    return 1 if is_tested else 0
  
  def can_remove(self):
    bricks_above = self.touching_up_bricks
    for brick_above in bricks_above:
      brick_above_bricks_below = bricks[brick_above].touching_down_bricks
      if len(brick_above_bricks_below) == 1: return False
    return True
    

def move_all_bricks(testing):
  global total
  for z in range(len(space[0][0])):
    for x in range(len(space)):
      for y in range(len(space[x])):
        label = space[x][y][z]
        if label != -1:
          total += bricks[label].move_down(testing)

bricks: list[Brick] = []
for i in range(len(inp)):
  bricks.append(Brick(inp[i], i))

move_all_bricks(False)

space_fallen = copy.deepcopy(space)
bricks_fallen = copy.deepcopy(bricks)

for i in range(len(bricks)):
  brick = bricks[i]
  print(f"{i}/{len(bricks)}")
  if brick.can_remove(): continue
  else:
    space = copy.deepcopy(space_fallen)
    for cube in brick.cubes:
      x, y, z = cube.x, cube.y, cube.z
      space[x][y][z] = -1
    move_all_bricks(True)
  bricks = copy.deepcopy(bricks_fallen)
  
#71002
print(total)