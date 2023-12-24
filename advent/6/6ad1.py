from functools import reduce
from math import ceil, floor, sqrt


file = open("C:/Computer Science/Paper 1/advent/6ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(map(lambda y: int(y), x.split(" ")[1:])),text.split("\n")))
file.close()

def quadratic(b, c):
  inside_root = b**2 - 4*c
  numerator_1 = b + sqrt(inside_root)
  numerator_2 = b - sqrt(inside_root)
  denominator = 2
  result_1 = numerator_1 / denominator
  result_2 = numerator_2 / denominator
  result_bottom = floor(result_1)
  result_top = ceil(result_2)
  if result_bottom == result_1: result_bottom -= 1
  if result_top == result_2: result_top += 1
  return result_bottom - result_top + 1

total = 1
for i in range(len(inp[0])):
  ans = quadratic(inp[0][i], inp[1][i])
  total *= ans
print(total)