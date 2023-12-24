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
  last_elements_total = 0
  dynamic_array = line
  while not check_all_zeros(dynamic_array):
    last_elements_total += dynamic_array[-1]
    shifted = dynamic_array[1:]
    dynamic_array = dynamic_array[:-1]
    for i in range(len(dynamic_array)):
      dynamic_array[i] = shifted[i] - dynamic_array[i]
  total += last_elements_total
  counter += 1
print(total)

