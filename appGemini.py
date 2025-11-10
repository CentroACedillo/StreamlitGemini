# gemini_streamlit_simple.py
# Run with: streamlit run gemini_streamlit_simple.py

import streamlit as st
from google import genai

# 1) Read API key from secrets
API_KEY = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
MODEL = "gemini-2.5-flash"

if not API_KEY:
    st.error("Add GEMINI_API_KEY or GOOGLE_API_KEY to your Streamlit secrets.")
    st.stop()

client = genai.Client(api_key=API_KEY)

# 2) UI
st.set_page_config(page_title="Gemini + Streamlit", layout="centered")

st.title("✨ Gemini + Streamlit")
prompt = st.text_area("Prompt", "Explain how AI works in a few words.")

if st.button("Send to Gemini"):
    if not prompt.strip():
        st.error("Write a prompt first.")
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
        st.write(text or "(empty response)")
