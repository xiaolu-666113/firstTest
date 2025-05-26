from pdf2docx import Converter

pdf_file = 'a.pdf'
docx_file = 'output.docx'

cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()