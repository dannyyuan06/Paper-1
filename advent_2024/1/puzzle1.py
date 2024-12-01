file = open("input.txt", "r")
text = file.read()
inp = list(map(lambda x: x.split("   "),text.split("\n")))
file.close()

left = list(map(lambda x: int(x[0]),inp))
right = list(map(lambda x: int(x[1]),inp))

left.sort()
right.sort()

total = 0

for i, x in enumerate(left):
    total += abs(x-right[i])

print(total)