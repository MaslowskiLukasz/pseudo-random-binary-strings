import os
import streamlit as st
from random import random
from random import seed

OUTPUT_MSG_DIR = "output_msg"
OUTPUT_RANDOM_DIR = "output_random"
OUTPUT_KEY_DIR = "output_key"
OUTPUT_DECODED_MSG_DIR = "output_decoded"
INPUT_MSG_DIR = "input_msg"
INPUT_RANDOM_DIR = "input_random"

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
    st.write("Wrong input size")
    return False
  return True

def save_msg(file_name, data):
  with open(f"{OUTPUT_MSG_DIR}/{file_name}", "w") as file:
    file.write(data)

def save_random(file_name, data):
  with open(f"{OUTPUT_RANDOM_DIR}/{file_name}", "w") as file:
    file.write(data)

def save_key(file_name, data):
  with open(f"{OUTPUT_KEY_DIR}/{file_name}", "w") as file:
    file.write(data)

def save_decoded_msg(file_name, data):
  with open(f"{OUTPUT_DECODED_MSG_DIR}/{file_name}", "w") as file:
    file.write(data)