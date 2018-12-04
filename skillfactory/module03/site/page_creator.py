# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt


def generate_page(head, body):
    # page = '<html>' + head + body + '</html>'

    page = f"<html>{head}{body}</html>"
    return page


def generate_head(title):
    # head = "<meta charset='utf-8'>" + '<title>' + title + '</title>'
    # return '<head>' + head + '</head'

    head = f"<meta charset='utf-8'><title>{title}</title>"
    return f"<head>{head}</head>"


def generate_footer(file_name='about.html', link_name='О реализации'):
    return f"<hr><a href={file_name}>{link_name}</a>"


def generate_body(header, paragraphs):
    # body = '<h1>' + header + '</h1>'
    # for i in paragraphs:
    #     body += '<p>' + i + '</p>'
    # return '<body>' + body + '</body>'

    body = f"<h1>{header}</h1>"
    for i in paragraphs:
        body += f"<p>{i}</p>"
    body += generate_footer()
    return f"<body>{body}</body>"


def save_page(title, header, paragraphs, output='index.html'):
    fp = open(output, 'w', encoding='utf-8')
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header, paragraphs),
    )
    print(page, file=fp)
    fp.close()


# my implementation


def insert_image(src, width, heigth):
    return f"<img src={src} width='{width}px' heigth='{heigth}px'>"


def insert_paragraph(text):
    return f"<p>{text}</p>"


def generate_list(data):
    text = ''
    for k in data.keys():
        text += f"<li>{k}</li><ul>"
        for v in data[k]:
            text += f"<li>{v}</li>"
        text += "</ul>"
    return "<ol>" + text + "</ol>"


def generate_body_about(header, data):
    body = f"<h1>{header}</h1>"
    body += insert_image('pic.png', 100, 100)
    body += insert_paragraph('Параметры генерации')
    body += generate_list(data)
    body += generate_footer(file_name='index.html', link_name='Главная')
    return f"<body>{body}</body>"


def save_page_about(title, header, data, output='about.html'):
    fp = open(output, 'w', encoding='utf-8')
    page = generate_page(
        head=generate_head(title),
        body=generate_body_about(header, data),
    )
    print(page, file=fp)
    fp.close()
