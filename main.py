import test
import generator
import files
import stream_encoder
import streamlit as st

PROGRAM_MODE = ["...", "BBS generator", "encode message", "decode message", "test random string"]

mode = st.selectbox("Chose mode", PROGRAM_MODE)

def create_random_string():
  p = st.number_input("p", step=1)
  q = st.number_input("q", step=1)
  blum = p * q
  seed = st.number_input("seed", step=1)
  length = st.number_input("length", step=1)
  result_file_name = st.text_input("Save results to file")
  if st.button("Generate and save"):
    result = generator.generate_BBS(blum, seed, length)
    st.text(f"create_random: {result}")
    files.save_random(result_file_name, result)

def encode_msg():
  p = st.number_input("p", step=1)
  q = st.number_input("q", step=1)
  blum = p * q
  seed = st.number_input("seed", step=1)
  file_name = files.get_input_file_name(mode)
  input = files.read_from_file(file_name)
  output_file_name = st.text_input("Output file name")
  key_file_name = st.text_input("Key file name")
  if st.button("Encode message"):
    encoded, key = stream_encoder.stream_encode(input, blum, seed)
    st.text(f"input: {input}")
    st.text(f"encoded: {encoded}")
    files.save_msg(output_file_name, encoded)
    files.save_key(key_file_name, key)

def decode_msg():  
  input_file_name = files.get_input_file_name(mode)
  key_file_name = files.get_input_file_name("key")
  input = files.read_from_file(input_file_name)
  key = files.read_from_file(key_file_name)
  if st.button("Decode message"):
    decoded = stream_encoder.stream_decode(input, key)
    st.text("input: {input}")
    st.text("decoded: {decoded}")

def run_tests():
  file_name = files.get_input_file_name(mode)
  input = files.read_from_file(file_name)
  st.text(input)
  st.text(f"summary: {test.run_all_tests(input)}")

#p = 1619
#q = 1231
#a = 5
#r = 20_000

if mode == "BBS generator":
  create_random_string()
elif mode == "encode message":
  encode_msg()
elif mode == "decode message":
  decode_msg()
elif mode == "test random string":
  run_tests()
