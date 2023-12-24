from itertools import combinations 
from functools import cache
file = open("C:/Computer Science/Paper 1/advent/12ad.txt", "r")
text = file.read()
inp = list(map(lambda x: [((str(x.split(" ")[0])+ "?")*5)[:-1], list(map(lambda y: int(y), x.split(" ")[1].split(",")))*5], text.split("\n")))
file.close()
total = 0
counter = 0
for line in inp:
  @cache
  def recursion(cur_index, cur_group_index, cur_group_length):
    global line
    [text, in_a_row] = line
    if cur_index == len(text) and (cur_group_index == len(in_a_row) and cur_group_length == 0 or cur_group_index == len(in_a_row) - 1 and cur_group_length == in_a_row[-1]): return 1
    if cur_index == len(text): return 0
    current_char = text[cur_index]
    total = 0
    if current_char == "?" or current_char == ".":
      if cur_group_length == 0:
        total += recursion(cur_index + 1, cur_group_index, cur_group_length)
      elif cur_group_index < len(in_a_row) and cur_group_length == in_a_row[cur_group_index]:
        total += recursion(cur_index + 1, cur_group_index + 1, 0)
    if current_char == "?" or current_char == "#":
      total += recursion(cur_index + 1, cur_group_index, cur_group_length + 1)
    return total
  total += recursion(0, 0, 0)
  counter += 1
print(total)