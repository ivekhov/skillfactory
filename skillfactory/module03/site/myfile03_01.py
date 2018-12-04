def generate_body(header, paragraphs):
    body = '<h1>' + header + '</h1>'
    for i in paragraphs:
        body += '<p>' + i + '</p>'
    return '<body>' + body + '</body>'
