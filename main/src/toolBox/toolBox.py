from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import cv2
import pytesseract
import numpy as np
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
class ToolBox:
    @staticmethod
    def convert_pdf_to_string(path : str) -> str:
        print("Starting the conversion process...")
        text = ""
        print(path)
        if not os.path.exists(path):
            return "The file is absent form the repository!"
        print("The file exists")
        reader = PdfReader(path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text :
                page_text = " ".join(page_text.split())
                text += page_text + "\n"

        if not text.strip():
            images = convert_from_path(path,
                                       dpi=300,
                                       poppler_path=r"C:\Program Files\Poppler\Release-25.07.0-0\poppler-25.07.0\Library\bin")
            for image in images :
                #prepare the image for conversion
                img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                gray = cv2.cvtColor(img_cv,cv2.COLOR_BGR2GRAY)
                _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
                thresh = cv2.medianBlur(thresh,3)
            
                text += pytesseract.image_to_string(thresh,lang="fra") +"\n"
        print("Conversion succeded!")
        return text