#!/usr/bin/env python3
import reports
import emails
from datetime import date
import os


if __name__ == "__main__":
    pdf_path = "/tmp/processed.pdf"
    pdf_header = f'Processed Update on {date.today()}'
    pdf_txt = ''
    pdf_line_break = '<br/>'
    txt_source = 'supplier-data/descriptions/'
    files = os.listdir(txt_source)
    for filename in sorted(files):
        with open(txt_source + filename, 'r') as txt:
            fruit = txt.readlines()
            pdf_txt += pdf_line_break + 'name: ' + fruit[0] + pdf_line_break + 'weight: ' + fruit[1] + pdf_line_break
            reports.generate_report(pdf_path, pdf_header, pdf_txt)

    sender = 'automation@example.com'
    recipient = '<username>@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    msg = emails.generate_email(sender, recipient, subject, body, pdf_path)
    emails.send_email(msg)
