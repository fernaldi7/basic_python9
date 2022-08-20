# Referensi Utama dari Youtube: Corey Schafer dan Python Passive Income 

# Import Modul Email dan CSV (Digunakan CSV karena juga bisa membaca dari file txt)
import smtplib, ssl, csv
from email.message import EmailMessage
# Import tool image reader
import imghdr

# Input data-data email
sender = 'fernaldigradiyanto7@gmail.com'
password = 'rahasia'
subject = 'Ini Kucingku, Mana Kucingmu?'
body_message = 'Kenalin kucing saya yang SWAG, namanya Tobi dan Dono, berikut foto mereka'

# Mendefinisikan STMP khas GMAIL
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context)

# Input gambar yang akan dijadikan attachment
files = ('F:\\Coding\\Indonesia.AI\\Basic Python\\Kucing1.jpg', 'F:\\Coding\\Indonesia.AI\\Basic Python\\Kucing2.jpg')

# For loop lapis luar untuk mengirimkan berbagai alamat email sesuai file txt
with open('F:\\Coding\\Indonesia.AI\\Basic Python\\Mails.txt', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = row
        em['Subject'] = subject
        em.set_content(body_message)
        # for loop lapis dalam untuk mengupload lebih dari 1 attachment
        for file in files:
            with open(file, 'rb') as img:
                file_data = img.read()
                file_type = imghdr.what(img.name)
                file_name = img.name
            em.add_attachment(file_data,maintype='image', subtype=file_type, filename=file_name)   
        # login menggunakan email dan password lalu mengeksekusi pengiriman email
        server.login(sender, password)
        server.send_message(em)
        print("The message sent")

server.close()
print("done")