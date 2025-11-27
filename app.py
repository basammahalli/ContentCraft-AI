import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Social Media Agent", layout="wide")
st.title("📱 AI Social Media Agent")

st.sidebar.header("⚙️ Settings")
platform = st.sidebar.selectbox("Platform", ["Instagram", "Twitter", "LinkedIn"])
tone = st.sidebar.selectbox("Tone", ["Casual", "Professional", "Funny", "Aesthetic", "Bold"])
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

client = OpenAI(api_key=api_key)

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

option = st.selectbox("What do you want to generate?", [
    "Caption Generator",
    "Hashtag Generator",
    "Content Ideas",
    "Weekly Content Plan",
    "Caption Rewriter",
    "Product Marketing Post",
    "Trending Reel Ideas"
])

text_input = st.text_area("Enter topic / product / caption:")

if st.button("Generate"):
    if not api_key:
        st.error("Enter your OpenAI key!")
        st.stop()

    prompt = f"Generate {option} for {platform} about '{text_input}' in {tone} tone."
    output = ask_ai(prompt)

    st.subheader("✨ Output")
    st.write(output)
