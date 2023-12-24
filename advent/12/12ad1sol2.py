from itertools import combinations 
from functools import cache
import re
file = open("C:/Computer Science/Paper 1/advent/12ad.txt", "r")
text = file.read()
inp = list(map(lambda x: [((str(x.split(" ")[0])+ "?")*5)[:-1], list(map(lambda y: int(y), x.split(" ")[1].split(",")))*5], text.split("\n")))
file.close()

total = 0
counter = 0
for line in inp:
  counter += 1
  text = line[0]
  in_a_row = line[1]
  print(counter)
  @cache
  def recurse(start_string, last_string, total):
    global in_a_row
    correct_order = in_a_row
    def check(start_string, correct_order):
      first_patterns = re.split(r'\.+', start_string)
      first_patterns = first_patterns[1:] if first_patterns[0] == "" else first_patterns
      if len(first_patterns) != 0:
        first_patterns = first_patterns[:-1] if first_patterns[-1] == "" else first_patterns
      for i in range(len(first_patterns)-1):
        first_pattern = first_patterns[i]
        if i >= len(correct_order): return False
        correct_pattern = correct_order[i]
        if len(first_pattern) != correct_pattern: return False
      return True
    def ccheck(start_string, correct_order):
      first_patterns = re.split(r'\.+', start_string)
      first_patterns = first_patterns[1:] if first_patterns[0] == "" else first_patterns
      if len(first_patterns) != 0:
        first_patterns = first_patterns[:-1] if first_patterns[-1] == "" else first_patterns
      for i in range(len(correct_order)):
        if i >= len(first_patterns): return False
        first_pattern = first_patterns[i]
        correct_pattern = correct_order[i]
        if len(first_pattern) != correct_pattern or len(first_patterns) != len(correct_order): return False
      return True
    if not check(start_string, correct_order):
      return total
    added_total = total
    new_start_string = start_string
    new_last_string = last_string
    while len(new_last_string) != 0:
      char = new_last_string[0]
      if char != "?":
        new_start_string += char
        new_last_string = new_last_string[1:]
      else:
        added_total = recurse(new_start_string + "#", new_last_string[1:], added_total)
        added_total = recurse(new_start_string + ".", new_last_string[1:], added_total)
        break
    if len(new_last_string) == 0 and ccheck(new_start_string, correct_order): 
      return total + 1
    return added_total
  total += recurse("", text, 0)
print(total)