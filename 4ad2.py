file = open("C:/Computer Science/Paper 1/4ad.txt", "r")

inp = []
totals = []

for line in file:
  two_lists = line[:-1].split(' | ')
  inp.append(list(map(lambda a: list(map(int, a.split(' '))), two_lists)))
  totals.append(1)
  
file.close()

for i in range(len(inp)):
  game = inp[i]
  num_correct = 0
  for num in game[0]:
    if num in game[1]: num_correct += 1
  for j in range(num_correct):
    totals[i+j+1] += totals[i]
  print(num_correct, game)

print(sum(totals))