file = open("C:/Computer Science/Paper 1/2adprop.txt", "r")

inp = []

for line in file:
  new_line = line.split(": ")[1].replace("\n", "")
  sets_read = new_line.split("; ")
  sets = []
  for set in sets_read:
    colours_read = set.split(", ")
    sets.append(colours_read)
  inp.append(sets)
  
file.close()

max_num = {
  "red": 12,
  "green": 13,
  "blue": 14
}
total = 0
game_no = 0
for game in inp:
  game_no += 1
  possible = True
  for set in game:
    for colours in set:
      data_split = colours.split(" ")
      num = int(data_split[0])
      colour = data_split[1]
      if max_num[colour] < num:
        possible = False
        break
    if not possible:
      break
  if possible:
    total += game_no

print(total)