file = open("C:/Computer Science/Paper 1/advent/9ad.txt", "r")
text = file.read()
inp = list(map(lambda x: list(map(lambda y: int(y), x.split(" "))), text.split("\n")))
file.close()

total = 0

counter = 0

def check_all_zeros(arr) :
  flag = True
  for ele in arr:
    if ele != 0: flag = False
  return flag
    

for line in inp:
  last_elements = []
  dynamic_array = line
  while not check_all_zeros(dynamic_array):
    last_elements.append(dynamic_array[0])
    shifted = dynamic_array[1:]
    dynamic_array = dynamic_array[:-1]
    for i in range(len(dynamic_array)):
      dynamic_array[i] = shifted[i] - dynamic_array[i]
  last_elements.reverse()
  for i in range(len(last_elements)-1):
    last_elements[i+1] -= last_elements[i]
  total += last_elements[-1]
  counter += 1
print(total)

