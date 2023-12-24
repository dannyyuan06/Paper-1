from multiprocessing import Process
file = open("C:/Computer Science/Paper 1/advent/5ad.txt", "r")

inp = []

text = file.read()


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        if mid + 1 == len(arr):
            return mid
        if arr[mid][1] <= x and arr[mid + 1][1] > x:
            return mid
        if arr[mid + 1][1] <= x:
            low = mid + 1
        if mid - 1 == 0:
            return 0
        if arr[mid][1] > x and arr[mid - 1][1] <= x:
            return mid - 1
        if arr[mid - 1][1] > x:
            high = mid - 1
    return -1

dictionary_text = text.split("\n\n")
split_rows = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z) if z.isdigit() else z, y.split(" "))), x.split("\n"))), dictionary_text))

mappings = []

seeds = split_rows[0][0][1:]
maps_raw = split_rows[1:]
for ma in maps_raw:
  mappings.append(sorted(ma[1:], key=lambda x: x[1]))
  
  
def process(i):
  lowest = 99999999999
  for j in range(seeds[i+1]):
    seed = seeds[i] + j
    value = seed
    for maps in mappings:
      index = binary_search(maps, value)
      if maps[index][1] + maps[index][2] >= value and index != -1:
        value = value - maps[index][1] + maps[index][0]
    if lowest > value:
      lowest = value
  print(lowest)


results = []

def p1(): process(0)
def p2(): process(2)
def p3(): process(4)
def p4(): process(6)
def p5(): process(8)
def p6(): process(10)
def p7(): process(12)
def p8(): process(14)
def p9(): process(16)
def p10(): process(18)

if __name__ == "__main__":
  pp1 = Process(target=p1)
  pp1.start()
  pp2 = Process(target=p2)
  pp2.start()
  pp3 = Process(target=p3)
  pp3.start()
  pp4 = Process(target=p4)
  pp4.start()
  pp5 = Process(target=p5)
  pp5.start()
  pp6 = Process(target=p6)
  pp6.start()
  pp7 = Process(target=p7)
  pp7.start()
  pp8 = Process(target=p8)
  pp8.start()
  pp9 = Process(target=p9)
  pp9.start()
  pp10 = Process(target=p10)
  pp10.start()