from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = 'JDF1822.pdf'
pdf = PdfFileReader(file_path)

with open('child.txt', 'w') as f:
    for page_num in range(8, pdf.numPages):
        print('Page: {0}'.format(page_num))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()