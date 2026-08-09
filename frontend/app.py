import streamlit as st
import requests

st.set_page_config(
    page_title="Code Review Assistant",
    page_icon="🔍",
    layout="wide"
)

st.title("Code Review Assistant")
st.markdown("*AI-powered code review using TinyLlama*")

# Sidebar
with st.sidebar:
    st.header("Settings")
    language = st.selectbox(
        "Programming Language",
        ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Rust", "TypeScript"]
    )

    st.header("Tips")
    st.write("""
    - Paste your code in the text area
    - Select the programming language
    - Click 'Review Code'
    - Get detailed feedback!
    """)

# Main content
code = st.text_area(
    "Paste your code here:",
    height=400,
    placeholder="def hello_world():\n    print('Hello, World!')"
)

if st.button("Review Code", type="primary"):
    if code:
        with st.spinner("Analyzing your code..."):
            try:
                response = requests.post(
                    "http://localhost:8000/review/",
                    data={"code": code, "language": language},
                    timeout=200
                )

                if response.status_code == 200:
                    review = response.json().get("review", "No review generated")

                    st.subheader("Review Results")
                    st.markdown("---")
                    st.markdown(review)

                    # Download button
                    st.download_button(
                        label="Download Review",
                        data=review,
                        file_name="code_review.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(f"Error: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to backend. Make sure FastAPI is running on port 8000.")
            except requests.exceptions.Timeout:
                st.error("Request timed out. The model may be taking longer than expected — try a shorter snippet.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please paste some code to review")

# Footer
st.markdown("---")
st.caption("Code Review Assistant | Powered by TinyLlama via Ollama")