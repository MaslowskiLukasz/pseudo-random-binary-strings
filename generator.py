def generate_BBS(blum_number, seed, length):
  result = ""
  last_number = (seed * seed) % blum_number
  result += str(last_number % 2)

  for i in range(1, length):
    last_number = (last_number * last_number) % blum_number
    result += str(last_number % 2)

  return result