from PyPDF2 import PdfFileWriter, PdfFileReader
output = PdfFileWriter()

ipdf = PdfFileReader(open('c:/test/Acn.pdf', 'rb'))
wpdf = PdfFileReader(open('c:/test/Wm.pdf', 'rb'))
watermark = wpdf.getPage(0)

for i in range(ipdf.getNumPages()):
    page = ipdf.getPage(i)
    page.mergePage(watermark)
    output.addPage(page)

with open('c:/test/demopdflaye.pdf', 'wb') as f:
   output.write(f)
