file = open("C:/Computer Science/Paper 1/4ad.txt", "r")

inp = []

for line in file:
  two_lists = line[:-1].split(' | ')
  inp.append(list(map(lambda a: list(map(int, a.split(' '))), two_lists)))
  
file.close()


total = 0

for game in inp:
  num_correct = 0
  for num in game[0]:
    if num in game[1]: num_correct += 1
  if num_correct > 0: 
    total += 2 ** (num_correct - 1)
  print(num_correct, game)

print(total)