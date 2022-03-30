import PyPDF2
from io import BytesIO

tmp = BytesIO()
path = open('../../files/48.pdf', 'rb')
merger = PyPDF2.PdfFileMerger()
merger.append(fileobj=path)
merger.write(tmp)
PyPDF2.filters.compress(tmp.getvalue())
merger.write(open("../../files/out-min.pdf", 'wb'))