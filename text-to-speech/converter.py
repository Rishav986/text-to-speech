import pyttsx3
from PyPDF2 import PdfReader

path = open('sample.pdf', 'rb')

file = PdfReader(path)

text = ""
for page in file.pages:
    text += page.extract_text()
    
bot = pyttsx3.init()
bot.say(text)
bot.runAndWait()