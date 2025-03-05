import streamlit as st
import requests

# ✅ FastAPI Endpoint
API_URL = "http://127.0.0.1:8000/query"

# ✅ Streamlit UI
st.title("🩺 AI Healthcare Assistant (RAG)")

# User Input
user_query = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if user_query.strip():
        with st.spinner("Fetching response..."):
            response = requests.post(API_URL, json={"query": user_query})
            if response.status_code == 200:
                st.success("✅ AI Response:")
                st.write(response.json()["response"])
            else:
                st.error("❌ Error fetching response!")
    else:
        st.warning("⚠️ Please enter a valid question.")
