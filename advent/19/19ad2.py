import copy

file = open("/Users/dannyyuan/Desktop/Code/Python/Paper-1/advent/19ad.txt", "r")
text = file.read()
[maps_inp, inp] = list(map(lambda x: x.split("\n"), text.split("\n\n")))
file.close()

maps = {}
for mapp in maps_inp:
  [name, text_rules] = mapp[:-1].split("{")
  list_text_rules = text_rules.split(",")
  def to_function(rule):
    result = []
    if ":" in rule:
      [operator, operands] = rule.split(":")
      if ">" in operator:
        [operator_1, operator_2] = operator.split(">")
        result.append([operator_1, ">", int(operator_2)])
        result.append(operands)
      else:
        [operator_1, operator_2] = operator.split("<")
        result.append([operator_1, "<", int(operator_2)])
        result.append(operands)
    else :
      result.append("final")
      result.append(rule)
    return result
        
  functions = list(map(to_function, list_text_rules))
  maps[name] = functions

def traverse(tree, current_node, max_vals, min_vals):
  functions = tree[current_node]
  total = 0
  prev_functions = []
  for func in functions:
    new_max_vals = copy.deepcopy(max_vals)
    new_min_vals = copy.deepcopy(min_vals)
    for prev_function in prev_functions:
      label = prev_function[0]
      operand = prev_function[2]
      if prev_function[1] == "<" :
       if new_min_vals[label] < operand - 1:
          new_min_vals[label] = operand - 1
      else: # >
        if new_max_vals[label] > operand + 1:
          new_max_vals[label] = operand + 1
    if func[0] != "final":
      label = func[0][0]
      operand = func[0][2]
      if func[0][1] == "<" :
        if new_max_vals[label] > operand:
          new_max_vals[label] = operand
      else: # >
        if new_min_vals[label] < operand:
          new_min_vals[label] = operand
    if func[1] != "A" and func[1] != "R": total += traverse(tree, func[1], new_max_vals, new_min_vals)
    elif func[1] == "A":
      xs = max(0, new_max_vals["x"] - new_min_vals["x"] - 1)
      ms = max(0, new_max_vals["m"] - new_min_vals["m"] - 1)
      As = max(0, new_max_vals["a"] - new_min_vals["a"] - 1)
      ss = max(0, new_max_vals["s"] - new_min_vals["s"] - 1)
      total += xs * ms * As * ss
    prev_functions.append(func[0])
  return total

max_vals = {
  "x": 4001,
  "m": 4001,
  "a": 4001,
  "s": 4001,
}

min_vals = {
  "x": 0,
  "m": 0,
  "a": 0,
  "s": 0,
}

#167409079868000
#167409079868000

total = traverse(maps, "in", max_vals, min_vals)
print(total)