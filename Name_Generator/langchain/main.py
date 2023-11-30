import streamlit as st
from langchain.langchain_helper import generate_name

st.title("Pets Name Generator")


# Sidebar UI
animal_type = st.sidebar.selectbox("What is your pet?",("Dog", "Cat", "Rabbit", "Parrot"))

if animal_type == "Dog":
  pet_color = st.sidebar.text_area(label = "What color is your Dog?", max_chars=20)

if animal_type == "Cat":
  pet_color = st.sidebar.text_area(label = "What color is your Cat?",max_chars=20)

if animal_type == "Rabbit":
  pet_color = st.sidebar.text_area(label = "What color is your Rabbit?",max_chars=20)

if animal_type == "Parrot":
  pet_color = st.sidebar.text_area(label = "What color is your Parrot?",max_chars=20)



# Use the user selection of type and color
if pet_color:
  response = generate_name(animal_type, pet_color)
  st.text(response)
