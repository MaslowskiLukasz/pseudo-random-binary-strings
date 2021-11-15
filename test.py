import pandas as pd
from pandas import Series

def run_all_tests(data):
  single_bit_result = single_bit_test(data)
  series_result = series_test(data)
  long_series_result = long_series_test(data)
  poker_result = poker_test(data)

  print(f"single bit: {single_bit_result}")
  print(f"series: {series_result}")
  print(f"long series: {long_series_result}")
  print(f"poker: {poker_result}")

  return single_bit_result and series_result and long_series_result and poker_result

def single_bit_test(data):
  counter = 0
  for i in range(0, len(data)):
    if data[i] == "1":
      counter += 1

  print(f"number of ones = {counter}")
  return 9725 < counter < 10275

def poker_test(data):
  counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  for i in range(0, len(data) - 3, 4):
    number = int(data[i : i+4], 2)
    counters[number] += 1

  sum = 0
  for x in counters:
    sum += x * x
  test_value = (16/5000) * sum - 5000
  return 2.16 < test_value < 46.17

def long_series_test(data):
  result = False
  ones_series_counter = 0
  zeros_series_counter = 0
  convert_data = pd.Series(data)
  ones_series_counter = convert_data.str.count("1{26,}")
  zeros_series_counter = convert_data.str.count("0{26,}")

  if ones_series_counter[0] == 0 & zeros_series_counter[0] == 0:
    result = True
  else:
    result = False
  return result

def series_test(data):
  ones_series_counters = [0, 0, 0, 0, 0, 0] #series: 1, 11, 111, 1111, 11111, six or more 1
  zeros_series_counters = [0, 0, 0, 0, 0, 0]
  current_ones_series_length = 0
  current_zeros_series_length = 0

  for i in range(0, len(data)):
    if i == len(data) - 1 and data[i] == "1":
      ones_series_counters[current_ones_series_length] += 1
    elif data[i] == "1" and data[i+1] == "0":
      if current_ones_series_length > 5:
        ones_series_counters[5] += 1
      else:
        ones_series_counters[current_ones_series_length] += 1
      current_ones_series_length = 0
    elif data[i] == "1" and data[i+1] == "1":
      current_ones_series_length += 1
    
    if i == len(data) - 1 and data[i] == "0":
      zeros_series_counters[current_zeros_series_length] += 1
    elif data[i] == "0" and data[i+1] == "1":
      if current_zeros_series_length > 5:
        zeros_series_counters[5] += 1
      else:
        zeros_series_counters[current_zeros_series_length] += 1
      current_zeros_series_length = 0
    elif data[i] == "0" and data[i+1] == "0":
      current_zeros_series_length += 1 
  
  #print(ones_series_counters)
  #print(zeros_series_counters)
  result = check_series_ranges(ones_series_counters, zeros_series_counters)
  return result

def check_series_ranges(ones, zeros):
  result = False
  if (2315 < ones[0] < 2685 and
    1114 < ones[1] < 1386 and
    527 < ones[2] < 723 and
    240 < ones[3] < 384 and
    103 < ones[4] < 209 and
    103 < ones[5] < 209 and
    2315 < zeros[0] < 2685 and
    1114 < zeros[1] < 1386 and
    527 < zeros[2] < 723 and
    240 < zeros[3] < 384 and
    103 < zeros[4] < 209 and
    103 < zeros[5] < 209):
    result = True
  else:
    result = False

  return result