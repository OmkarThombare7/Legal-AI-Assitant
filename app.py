import streamlit as st
from utils.file_loader import load_file
from utils.summarizer import summarize_text
from utils.qa_engine import ask_question

# Page config
st.set_page_config(page_title="Legal AI Assistant", layout="wide")

# Sidebar
st.sidebar.title("⚙️ Options")
st.sidebar.markdown("Upload a document and interact with it.")
show_full_text = st.sidebar.checkbox("Show Full Extracted Text")

# Main Title
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>📜 Legal AI Assistant</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# File Upload Section
uploaded_file = st.file_uploader(
    "📂 Upload PDF, Image or Text",
    type=["pdf", "png", "jpg", "jpeg", "txt"]
)

if uploaded_file:
    with st.spinner("🔍 Extracting text..."):
        text = load_file(uploaded_file)

    st.success("✅ File processed successfully!")

    # Layout: Two columns
    col1, col2 = st.columns(2)

    # Left Column - Extracted Text
    with col1:
        st.subheader("📄 Extracted Text")

        if show_full_text:
            st.text_area("Full Text", text, height=400)
        else:
            with st.expander("Preview Text"):
                st.write(text[:1000] + "...")

    # Right Column - Actions
    with col2:
        st.subheader("⚡ Actions")

        # Summary Button
        if st.button("📝 Generate Summary"):
            with st.spinner("Generating summary..."):
                summary = summarize_text(text)
            st.success("Summary Generated!")
            st.write(summary)

        st.markdown("---")

        # Question Answer Section
        question = st.text_input("❓ Ask a question from the document")

        if question:
            with st.spinner("Finding answer..."):
                answer = ask_question(text, question)
            st.success("Answer Found!")
            st.write(answer)

else:
    st.info("👆 Upload a file to get started")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)