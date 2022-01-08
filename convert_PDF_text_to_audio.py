
#-------------------------------------------
#
# FILENAME:	convert_PDF_text_to_audio.py
# 		
# CREATED: 	01.07.2022 - dserke
#
# SOURCES:	https://www.geeksforgeeks.org/convert-pdf-file-text-to-audio-speech-using-python/
#
# NOTES: 	1.8.2022 Gave up on install.  Need espeak and/or  libespeak.so.1 but need sud0 .... command with root priv to get package
#-------------------------------------------

#-------------------------------------------
# IMPORT LIBRARIES
#-------------------------------------------
import PyPDF2
import pyttsx3 as

#-------------------------------------------
# DEFINE CONSTANTS
#-------------------------------------------
# path of the PDF file
path      = open('/d1/serke/projects/python_tutorial/data/HuckFinn.pdf', 'rb')

#-------------------------------------------
# DEFINE INPUT FILES
#-------------------------------------------
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)
  
# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(24)
  
# extracting the text from the PDF
text      = from_page.extractText()

#-------------------------------------------
# LOAD INPUT FILES
#-------------------------------------------


#-------------------------------------------
# OUTPUT
#-------------------------------------------
# reading the text
speak      = pyttsx3.init()
speak.say(text)
speak.runAndWait()

