import test
import generator
import files
import stream_encoder
import streamlit as st


result_file_name = "output1.txt"
p = 1619
q = 1231
n = p * q
a = 5
r = 20_000

#result = generator.generate_BBS(n, a, r)
#files.save_to_file(result_file_name, result)
result = files.read_from_file(result_file_name)

print(f"all tests result: {test.run_all_tests(result)}")

input = files.read_from_file("encoded.txt")
encoded = stream_encoder.stream_encode(input, n, a)

st.text(f"input: {input}")
st.text(f"encoded: {encoded}")