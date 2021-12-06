import test
import generator
import os
import files
import stream_encoder
import streamlit as st


PROGRAM_MODE = ["...", "BBS generator", "encode message", "decode message", "test random string"]

mode = st.selectbox("Select mode", PROGRAM_MODE)

def create_random_string():
  p = st.number_input("p", step=1, value=36187)
  q = st.number_input("q", step=1, value=50591)
  blum = p * q
  seed = st.number_input("seed", step=1, value=52609)
  length = st.number_input("length", step=1, value=20_000)
  result_file_name = st.text_input("Save results to file")
  if st.button("Generate and save"):
    result = generator.generate_BBS(blum, seed, length)
    st.write("Random")
    st.text(result)
    files.save_random(result_file_name, result)

def encode_msg():
  p = st.number_input("p", step=1, value=36187)
  q = st.number_input("q", step=1, value=50591)
  seed = st.number_input("seed", step=1, value=52609)
  blum = p * q

  file_list = os.listdir(files.INPUT_MSG_DIR)
  name = st.selectbox("Pick file", file_list)
  input = files.read_from_file(f"{files.INPUT_MSG_DIR}/{name}")
  output_file_name = st.text_input("Output file name")

  if st.button("Encode message"):
    encoded, key = stream_encoder.stream_encode(input, blum, seed)
    st.write("input")
    st.markdown(f"`{input}`")
    st.write("key")
    st.markdown(f"`{key}`")
    st.write("output")
    st.markdown(f"`{encoded}`")
    files.save_msg(output_file_name, encoded)
    files.save_key(output_file_name, key)

def decode_msg():  
  file_list = os.listdir(files.OUTPUT_MSG_DIR)
  name = st.selectbox("Pick file", file_list)
  input_file_name = f"{files.OUTPUT_MSG_DIR}/{name}"
  key_file_name = f"{files.OUTPUT_KEY_DIR}/{name}"

  input = files.read_from_file(input_file_name)
  key = files.read_from_file(key_file_name)

  if st.button("Decode message"):
    decoded = stream_encoder.stream_decode(input, key)
    st.write("input")
    st.markdown(f"`{input}`")
    st.write("key")
    st.markdown(f"`{key}`")
    st.write("output")
    st.markdown(f"`{decoded}`")
    files.save_decoded_msg(name, decoded)

def run_tests():
  file_list = os.listdir(files.INPUT_RANDOM_DIR)
  name = st.selectbox("Pick file", file_list)
  input = files.read_from_file(f"{files.INPUT_RANDOM_DIR}/{name}")

  if st.button("Run all tests"):
    st.text(input)
    if(files.validate_input(input)):
      st.text(f"summary: {test.run_all_tests(input)}")

#p = 19319, 21379, 31307, 30047, 36187
#q = 21247, 43427, 41959, 43787, 50591
#a = 543213, 52609, 50441, 52561, 52609
#r = 20_000

if mode == "BBS generator":
  create_random_string()
elif mode == "encode message":
  encode_msg()
elif mode == "decode message":
  decode_msg()
elif mode == "test random string":
  run_tests()
