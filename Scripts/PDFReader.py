from pdf2image import convert_from_path
import pytesseract
from PIL import Image

def extract_text_from_pdf(file_path):
    # Set the tesseract executable path
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as per your installation
    images = convert_from_path(file_path, dpi=300)
    text = ''
    for i, image in enumerate(images):
        text += pytesseract.image_to_string(image)
    return text    

print(extract_text_from_pdf(r'C:\Users\sakpa\Projects\Upgrad\Gen AI\QTS\Data\unsettled_trade_email_final.pdf'))