import streamlit as st
import requests

# ✅ FastAPI Endpoint
API_URL = "http://127.0.0.1:8000/query"  # Ensure FastAPI is running on this URL

# ✅ Streamlit UI
st.set_page_config(page_title="AI Healthcare Assistant", page_icon="🩺", layout="centered")

st.title("🩺 AI Healthcare Assistant (RAG)")
st.markdown(
    "This AI assistant retrieves relevant healthcare information from multiple datasets "
    "using **Retrieval-Augmented Generation (RAG)**. Just type your question below!"
)

# User Input
user_query = st.text_area("💬 Enter your question:")

# Submit Button
if st.button("🔍 Ask AI"):
    if user_query.strip():
        with st.spinner("🤖 Thinking... Fetching response..."):
            try:
                response = requests.post(API_URL, json={"query": user_query})
                if response.status_code == 200:
                    ai_response = response.json().get("response", "⚠️ No response received.")
                    st.success("✅ AI Response:")
                    st.markdown(f"**💡 {ai_response}**")  # Display response in bold markdown
                else:
                    st.error(f"❌ Error {response.status_code}: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Connection Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid question.")
