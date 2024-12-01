file = open("input.txt", "r")
text = file.read()
inp = list(map(lambda x: x.split("   "),text.split("\n")))
file.close()

left = list(map(lambda x: int(x[0]),inp))
right = list(map(lambda x: int(x[1]),inp))

total = 0

occurances = {}

for x in right:
    if x in occurances:
        occurances[x] += 1
    else: occurances[x] = 1

for x in left:
    if x in occurances:
        total += x*occurances[x]

print(total)