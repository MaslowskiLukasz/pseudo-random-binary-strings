import math


def generateBBS(blum_number, seed, length):
  arr = []
  last_number = (seed * seed) % blum_number
  arr.append(last_number % 2)

  for i in range(1, length):
    print(last_number)
    last_number = (last_number * last_number) % blum_number
    arr.append(last_number % 2)

  print(arr)
  print(len(arr))
  return arr


n = 121
a = 5
r = 1024

arr = generateBBS(n, a, r)


with open("results.txt", "w") as file:
  file.write(str(arr))
