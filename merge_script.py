from PyPDF2 import PdfFileMerger

pdfs = ['resume.pdf', 'english_resume.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("Chen Yangyang resume.pdf")
merger.close()
