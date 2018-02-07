from PyPDF2 import PdfFileMerger, PdfFileReader
import os

merger = PdfFileMerger()
files = [x for x in os.listdir('c:/test') if x.endswith('.pdf')]
for fname in sorted(files):
    merger.append(PdfFileReader(open(os.path.join('c:/test', fname), 'rb')))

merger.write("c:/test/demopdfmerge.pdf")
