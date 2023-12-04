import PyPDF2

#simple script to add a watermark to a pdf file.
template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb')) 
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page._merge_page(watermark.pages[0])
    output.add_page(page)


with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
        