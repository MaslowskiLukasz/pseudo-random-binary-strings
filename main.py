import test
import generator
import files


result_file_name = "results.txt"
n = 789
a = 5
r = 20000

result = generator.generate_BBS(n, a, r)
files.save_to_file(result_file_name, result)

print(test.single_bit_test(result))
print(test.series_test(result))