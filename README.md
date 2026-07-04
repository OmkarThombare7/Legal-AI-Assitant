# ⚖️ Legal AI Assistant

An AI-powered web application that summarizes legal documents and answers user queries using Groq LLM and Streamlit.

## 🚀 Features

- 📄 Upload PDF, DOCX, and TXT files
- 📝 Generate AI-powered summaries
- ❓ Ask questions about uploaded documents
- ⚡ Fast and interactive Streamlit interface
- 🤖 Powered by Groq LLM

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API (Llama Models)
- pdfplumber
- PyPDF2
- python-docx
- pytesseract
- python-dotenv

## 📂 Project Structure

```
├── app.py
├── config/
├── utils/
├── requirements.txt
├── README.md
└── test_groq_hardcoded.py
```

## ▶️ Installation

```bash
git clone https://github.com/your-username/Legal-AI-Assistant.git

cd Legal-AI-Assistant

pip install -r requirements.txt

streamlit run app.py
```

## 🔑 Configuration

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key
```

## 📌 Future Enhancements

- OCR support
- Multi-document analysis
- RAG integration
- Chat history
- PDF summary export

## 👨‍💻 Author

**Omkar Thombare**
