from email.message import EmailMessage
import smtplib
import getpass
import mimetypes
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


sender = 'me@example.com'
recipient = 'you@example.com'
body = "Hey there!\n\nI'm learning to send emails using Python!"

message = EmailMessage()
message['From'] = sender
message['To'] = recipient
message['Subject'] = f'Greetings from {sender} to {recipient}!'
message.set_content(body)
attachment_path = '/tmp/example.png'
mime_type, mime_subtype = mimetypes.guess_type(attachment_path)
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename='example.png')

mail_server = smtplib.SMTP_SSL('smtp.example.com')
mail_pass = getpass.getpass('Password: ')
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()

fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

report = SimpleDocTemplate('/tmp/report.pdf')
styles = getSampleStyleSheet()
report_title = Paragraph('A Complete Inventory of My Fruit', styles['h1'])

table_data = []
for k, v in fruit.items:
    table_data.append([k, v])

table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign='LEFT')
report_pie = Pie(width=3*inch, height=3*inch)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.labels.append(fruit_name)
    report_pie.data.append(fruit[fruit_name])
report_chart = Drawing()
report_chart.add(report_pie)
report.build([report_title, report_table, report_chart])
