import smtplib, ssl, csv
import imghdr
from email.message import EmailMessage

sender = 'fernaldigradiyanto7@gmail.com'
password = 'qzoxkiazzqnskzvn'

subject = 'Ini Kucingku, Mana Kucingmu?'
body_message = 'Kenalin kucing saya yang SWAG, namanya Tobi dan Dono, berikut foto mereka'

context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context)

em = EmailMessage()
em['From'] = sender
em['Subject'] = subject
em.set_content(body_message)

files = ('F:\\Coding\\Indonesia.AI\\Basic Python\\Kucing1.jpg', 'F:\\Coding\\Indonesia.AI\\Basic Python\\Kucing2.jpg')

with open('F:\\Coding\\Indonesia.AI\\Basic Python\\Mails.txt', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = row
        em['Subject'] = subject
        em.set_content(body_message)
        for file in files:
            with open(file, 'rb') as img:
                file_data = img.read()
                file_type = imghdr.what(img.name)
                file_name = img.name
            em.add_attachment(file_data,maintype='image', subtype=file_type, filename=file_name)   
        server.login(sender, password)
        server.send_message(em)
        print("The message sent")

server.close()
print("done")