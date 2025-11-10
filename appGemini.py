# gemini_streamlit_simple.py
# Run with: streamlit run gemini_streamlit_simple.py

import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# 1) Load .env file
load_dotenv()  # this reads .env and adds variables to os.environ

# 2) Get API key from environment
API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
MODEL = "gemini-2.5-flash"

# Debug helper (optional, remove later)
# st.write("API_KEY present:", API_KEY is not None)

# Create client (will fail early if no key)
if not API_KEY:
    st.error("Set GEMINI_API_KEY or GOOGLE_API_KEY in your .env or environment.")
    st.stop()

client = genai.Client(api_key=API_KEY)

# 3) Streamlit UI
st.set_page_config(page_title="Gemini + Streamlit (Simple)", layout="centered")

st.title("✨ Gemini + Streamlit (Simple)")
st.caption("Prompt in, text out.")

prompt = st.text_area(
    "Prompt",
    value="Explain how AI works in a few words.",
    height=150,
)

if st.button("Send to Gemini"):
    if not prompt.strip():
        st.error("Please write a prompt first.")
    else:
        with st.spinner("Calling Gemini..."):
            try:
                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt,
                )
                text = (response.text or "").strip()
            except Exception as e:
                text = f"❌ Error: {e}"

        st.subheader("Response")
        st.code(text or "(empty response)", language="markdown")
