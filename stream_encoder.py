import generator

def stream_encode(input, blum_number, seed):
  output = ""
  key_length = len(input)
  key = generator.generate_BBS(blum_number, seed, key_length)
  print(f"key: {key}")
  for i in range(0, key_length):
    input_value = True if input[i] == "1" else False
    key_value = True if key[i] == "1" else False
    output += str(int(input_value ^ key_value))

  return output