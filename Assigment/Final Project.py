#Script bersumber dari Youtube: Python Passive Income
#Script untuk attachment file bersumber dari Youtube: Corey Schafer

from email.mime.base import MIMEBase
# Import modul pengiriman email dan CSV Reader (Proses yang akan dilakukan adalah membaca txt sebagai csv)
import smtplib, ssl, csv
# Import Modul Image reader
import imghdr
from email.message import EmailMessage

# Mengaitkan dengan GMAIL
sender = 'fernaldigradiyanto7@gmail.com' 
password = 'rahasia'

# Subject dan Body Email
subject = 'Email Automation with Python'
body_message = "Halo, Apabila anda menemukan kucing di bawah ini harap segera menghubungi saya. Terima kasih"

# Mendefinisikan SMTP Email yang digunakan yaitu GMAIL
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context)
server.login(sender, password)
em = EmailMessage()

# Memasukkan Attachment
files = ['G:\\python\\basic_python9\\Assigment\\Kucing1.jpg', 'G:\\python\\basic_python9\\Assigment\\Kucing2.jpg']

for file in files:
    with open(file, 'rb') as img:
        file_data = img.read()
        file_type = imghdr.what(img.name)
        file_name = img.name

# Mengaitkan dengan txt berisi list email yang akan dituju
with open('F:\\Coding\\Indonesia.AI\\Basic Python\\mails.txt', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        em['From'] = sender
        em['To'] = row
        em['Subject'] = subject
        em.set_content(body_message)
        # Mengirimkan Attachment
        em.add_attachment(file_data,maintype='image', subtype=file_type, filename=file_name)
        server.send_message(em)
        print("The message sent")

server.close()
print("Done")