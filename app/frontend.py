import streamlit as st
from backend import generated_post

st.set_page_config(page_title="Linkedin Post Generator", layout="wide")

st.title("LinkedIn Post Generator")

st.divider()

col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("Enter Your Topic:", placeholder="Topic")

    length = st.selectbox("Select Length:", ("Short", "Medium", "Long"),index=None, placeholder="Length")

    tone = st.selectbox("Select Tone:", ("Thoughtful", "Relatable", "Motivational", "Instructional", "Direct"), index=None, placeholder="Tone")

    language = st.selectbox("Select Language:", ("English", "Hinglish"), index=None, placeholder="Language")

    generate_post = st.button("Generate")

with col2:
    with st.container(border=True, height=400):
        if generate_post:
            post = generated_post(topic, length, tone, language)
            st.markdown(post)