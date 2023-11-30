import streamlit as st
import langchain as lch

st.title("Pets Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?",("Dog", "Cat", "Rabbit", "Parrot"))

if animal_type == "Dog":
  pet_color = st.sidebar.text_area(label = "What color is your Dog?", max_chars=20)

if animal_type == "Cat":
  pet_color = st.sidebar.text_area(label = "What color is your Cat?",max_chars=20)

if animal_type == "Rabbit":
  pet_color = st.sidebar.text_area(label = "What color is your Rabbit?",max_chars=20)

if animal_type == "Parrot":
  pet_color = st.sidebar.text_area(label = "What color is your Parrot?",max_chars=20)