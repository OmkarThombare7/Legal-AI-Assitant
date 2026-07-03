import pytesseract
from PIL import Image
import PyPDF2
import io

# ✅ Set Tesseract path (only once)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def load_file(uploaded_file):

    try:
        file_type = uploaded_file.name.split(".")[-1].lower()

        # 📄 PDF Handling
        if file_type == "pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:  # ✅ avoid None
                    text += page_text

            return text if text.strip() else "⚠️ No text found in PDF"

        # 🖼️ Image Handling (OCR)
        elif file_type in ["png", "jpg", "jpeg"]:
            image = Image.open(uploaded_file)
            text = pytesseract.image_to_string(image)
            return text if text.strip() else "⚠️ No text detected in image"

        # 📃 TXT Handling
        elif file_type == "txt":
            return uploaded_file.read().decode("utf-8")

        return "❌ Unsupported file type"

    except Exception as e:
        return f"❌ Error processing file: {e}"