import PyPDF2
from sys import argv

files = argv[1:]


def pdf_merger(pdf_list):
    with open('merged.pdf', 'wb') as out_file:
        merger = PyPDF2.PdfFileMerger()
        for file in pdf_list:
            merger.merge(0, file)
        merger.write(out_file)


pdf_merger(files)
