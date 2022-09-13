#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_header = Paragraph(title, styles['h1'])
    report_txt = Paragraph(paragraph, styles['BodyText'])
    report.build([report_header, report_txt])
