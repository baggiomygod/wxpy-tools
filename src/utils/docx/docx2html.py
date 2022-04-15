from pydocx import PyDocX


def read_word2html(docxUrl):
    # Pass in a path
    html = PyDocX.to_html(docxUrl)
    return html
    # return HttpResponse(html)
