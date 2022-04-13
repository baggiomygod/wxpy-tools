from docx2pdf import convert


def coverPdf(docxFile, output):
    convert(docxFile, output)

