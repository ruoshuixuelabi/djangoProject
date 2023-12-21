from pdf2docx import Converter

pdf_file = 'D:/物业服务方案.pdf'
docx_file = 'D:/物业服务方案.docx'
# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)  # all pages by default
cv.close()
