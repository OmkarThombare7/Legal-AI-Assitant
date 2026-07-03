import pytesseract
from PIL import Image
import PyPDF2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def extract_text_from_image(file):

    image = Image.open(file)

    text = pytesseract.image_to_string(image)

    return text


def extract_text_from_txt(file):

    return file.read().decode("utf-8")