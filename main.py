from speech import Speech
from PyPDF2 import PdfFileReader
import sys

def read_pages(pdf_reader):
    for page in range(pages):
        page_obj = pdf_reader.getPage(page)
        text = page_obj.extractText()
        print(text)
        voice.say(text)
    return

voice=Speech()

file = input('Enter the file you wish to hear: ').lower()
voice.say(f"Opening {file.split('.')[0]}")

try:
    with open(file, mode='rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        pages = pdf_reader.getNumPages()
        read_pages(pdf_reader)
except FileNotFoundError:
    voice.say('Unable to find your file, please try again')
    sys.exit()

pdf_file.close()

