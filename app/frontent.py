import streamlit as st
from backend import generated_post

st.set_page_config(page_title="Linkedin Post Generator",)

st.title("LinkedIn Post Generator")

st.divider()

topic = st.text_input("Enter Your Topic:", placeholder="Topic")

length = st.selectbox("Select Length:", ("Short", "Medium", "Long"),index=None, placeholder="Length")

tone = st.selectbox("Select Tone:", ("Thoughtful", "Relatable", "Motivational", "Instructional", "Direct"), index=None, placeholder="Tone")

language = st.selectbox("Select Language:", ("English", "Hinglish"), index=None, placeholder="Language")

if st.button("Generate"):
    post = generated_post(topic, length, tone, language)
    st.write(post)