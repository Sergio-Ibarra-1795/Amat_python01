import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import glob

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        author = info.author
        creator = info.creator
        producer = info.producer
        subject = info.subject
        title = info.title
        print(f'Autor: {author}')
        print(f'Creador: {creator}')
        print(f'Productor: {producer}')
        print(f'Tema: {subject}')
        print(f'Título: {title}')
        print(f'Páginas: {number_of_pages}')

def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(4)
        #page = pdf.pages
        text = page.extractText()
        print(text)

def pdf_splitter(path, output):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()

def pdf_splitter(path, output):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_page_{}.pdf'.format(output + fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))

def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    for path in input_paths:
        pdf_merger.append(path)
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

def rotator(path, output):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)
    page1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page1)
    page2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page2)
    with open(output + 'pdf_rotator.pdf', 'wb') as fh:
        pdf_writer.write(fh)

def watermark(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfFileReader(watermark_pdf)
    watermark_page = watermark.getPage(0)
    pdf = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)
        
def encrypt(input_pdf, output_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 
                       use_128bit=True)
    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    path = R'C:\Users\llell\Documents\SIR_Personal\Other_Courses\PythonAMAT\demo1.pdf'
    my_output = R'C:\Users\llell\Documents\SIR_Personal\Other_Courses\PythonAMAT'

get_info(path)
