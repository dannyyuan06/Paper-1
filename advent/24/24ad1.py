file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/24/24ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(map(lambda y: list(map(int, y.split(", "))), x.split(" @ "))), text.split("\n")))
file.close()

x_range = [200000000000000, 400000000000000]
y_range = [200000000000000, 400000000000000]

def get_equation(position: list[int], velocity:list[int]):
  coef = velocity[1]/velocity[0]
  cons = position[1]-(position[0]*velocity[1])/velocity[0]
  return coef, cons

def solve_for_x(coef_1, coef_2, cons_1, cons_2):
  return (cons_2 - cons_1)/(coef_1 - coef_2) if coef_1 - coef_2 != 0 else None

def get_y(x, coef, cons):
  return x * coef + cons

def is_t_neg(p, v, x):
  return (x-p)/v < 0

total = 0
for i in range(len(inp)):
  for j in range(i+1, len(inp)):
    e_1, c_1 = get_equation(inp[i][0], inp[i][1])
    e_2, c_2 = get_equation(inp[j][0], inp[j][1])
    x = solve_for_x(e_1, e_2, c_1, c_2)
    if x is None: continue
    if is_t_neg(inp[i][0][0], inp[i][1][0], x) or is_t_neg(inp[j][0][0], inp[j][1][0], x) :continue
    y = get_y(x, e_1, c_1)
    if x >= x_range[0] and x < x_range[1] and y >= y_range[0] and y < y_range[1]:
      total += 1
print(total)