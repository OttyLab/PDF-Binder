import csv
import sys
import PyPDF2

args = sys.argv

pdf_writer = PyPDF2.PdfWriter()
with open(args[1]) as list:
    csv_reader = csv.reader(list)
    for row in csv_reader:
        print(row[0].encode('cp932').decode('utf-8'))
        pdf_reader = PyPDF2.PdfReader(row[0].encode('cp932').decode('utf-8'))
        del row[0]
        for page in row:
            pdf_writer.add_page(pdf_reader.pages[int(page)])

with open(args[2], 'wb') as output:
    pdf_writer.write(output)
