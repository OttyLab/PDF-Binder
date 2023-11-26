import csv
import sys
import re
import os
import PyPDF2

args = sys.argv

def shift(page, n=-1):
    return page + n

pdf_writer = PyPDF2.PdfWriter()
page_num = r'^(\d+)$'
page_range = r'^(\d+)-(\d+)$'

with open(args[1]) as list:
    csv_reader = csv.reader(list)
    for row in csv_reader:
        file_name = row[0].encode('cp932').decode('utf-8') if os.name == 'nt' else row[0]
        del row[0]

        print(file_name)
        pdf_reader = PyPDF2.PdfReader(file_name)

        for pages in row:
            pages = pages.replace(' ', '')
            match_page_num = re.match(page_num, pages)
            match_page_range = re.match(page_range, pages)

            if (match_page_num):
                page = shift(int(match_page_num.group(1)))
                pdf_writer.add_page(pdf_reader.pages[page])
            elif (match_page_range):
                start = shift(int(match_page_range.group(1)))
                end = shift(int(match_page_range.group(2)))
                for page in range(start, end + 1):
                    pdf_writer.add_page(pdf_reader.pages[page])

with open(args[2], 'wb') as output:
    pdf_writer.write(output)
