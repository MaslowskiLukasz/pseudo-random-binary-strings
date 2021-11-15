def save_to_file(file_name, data):
  with open(file_name, "w") as file:
    file.write(data)

def read_from_file(file_name):
  text = ""
  with open(file_name, "r") as file:
    text = file.read()
  return text

def validate_input(data):
  if len(data) != 20_000:
    print("Wrong input size")
    return False
  return True
