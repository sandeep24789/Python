from PyPDF2 import PdfFileWriter, PdfFileReader
infile = PdfFileReader('c:/test/PoetryWBP.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    p = infile.getPage(i)

    text=p.extractText()

    if len(text) > 10: # getContents is None if  page is blank
        print(i,len(text),text)
        output.addPage(p)

with open('c:/test/output.pdf', 'wb') as f:
   output.write(f)
