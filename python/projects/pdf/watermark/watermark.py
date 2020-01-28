import PyPDF2
from sys import argv

watermark_file = argv[1]
list_of_files = argv[2:]


def watermarker(watermark_file, list_of_files):

    watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
    watermark_page = watermark_pdf.getPage(0)

    for file in list_of_files:

        watermarked_pdf = PyPDF2.PdfFileWriter()
        source_pdf = PyPDF2.PdfFileReader(file)
        page_count = source_pdf.getNumPages()

        for page_number in range(page_count):
            source_page = source_pdf.getPage(page_number)
            source_page.mergePage(watermark_page)
            watermarked_pdf.addPage(source_page)

        out_name = "watermarked/" + file.split('.')[0] + '-watermarked.pdf'
        with open(out_name, 'wb') as out_file:
            watermarked_pdf.write(out_file)


watermarker(watermark_file, list_of_files)
