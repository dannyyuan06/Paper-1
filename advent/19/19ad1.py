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
        result.append(operator_1)
        result.append(lambda x: operands if x > int(operator_2) else "next")
      else:
        [operator_1, operator_2] = operator.split("<")
        result.append(operator_1)
        result.append(lambda x: operands if x < int(operator_2) else "next")
    else :
      result.append("final")
      result.append(lambda _: rule)
    return result
        
  functions = list(map(to_function, list_text_rules))
  maps[name] = functions


def to_dictionary(ip):
  dic = {}
  splits = ip[1:-1].split(",")
  for split in splits:
    [var, operand] = split.split("=")
    operand = int(operand)
    dic[var] = operand
  return dic
inputs = list(map(to_dictionary, inp))

total = 0
for input in inputs:
  is_accepted = False
  current_function_name = "in"
  while current_function_name != "final":
    counter = 0
    result = "next"
    while result == "next":
      [label, current_function] = maps[current_function_name][counter]
      num_sub = input[label] if label != "final" else ""
      result = current_function(num_sub)
      counter += 1
    if result == "R" or result == "A":
      current_function_name = "final"
      is_accepted = result == "A"
    else:
      current_function_name = result
  if is_accepted:
    for key in input:
      total += input[key]
print(total)