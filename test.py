from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
username = ""
password = ""
from_email = username

with open('emails.txt') as f:
    to_list = [email.strip() for email in f]

msg_root = MIMEMultipart('related')
msg_root['Subject'] = 'Travel Lab | Лаборатория Путешествий. Предложение по сотрудничеству'
msg_root['From'] = from_email
msg_root['To'] = ''
msg_root.preamble = 'multipart message in MIME format'

msg_alternative = MIMEMultipart('alternative')
msg_root.attach(msg_alternative)

msg_text = MIMEText('alternative plain text message')
msg_alternative.attach(msg_text)


html_txt = """\
<html>
</html>
    """
msg_text = MIMEText(html_txt, 'html')
msg_alternative.attach(msg_text)

with open('logo.jpg', 'rb') as img:
    msg_img_logo = MIMEImage(img.read())
msg_img_logo.add_header('Content-ID', '<logo>')
msg_root.attach(msg_img_logo)

with open('lvov.jpg', 'rb') as img:
    msg_img_lvov = MIMEImage(img.read())
msg_img_lvov.add_header('Content-ID', '<lvov>')
msg_root.attach(msg_img_lvov)

with open('karpati.jpg', 'rb') as img:
    msg_img_karpati = MIMEImage(img.read())
msg_img_karpati.add_header('Content-ID', '<karpati>')
msg_root.attach(msg_img_karpati)

with open('lvov_november.jpg', 'rb') as img:
    msg_img_lvov_november = MIMEImage(img.read())
msg_img_lvov_november.add_header('Content-ID', '<lvov_november>')
msg_root.attach(msg_img_lvov_november)

with open('lvov_new_year.jpg', 'rb') as img:
    msg_img_lvov_new_year = MIMEImage(img.read())
msg_img_lvov_new_year.add_header('Content-ID', '<lvov_new_year>')
msg_root.attach(msg_img_lvov_new_year)

with open('karpati_winter.jpg', 'rb') as img:
    msg_img_karpati_winter = MIMEImage(img.read())
msg_img_karpati_winter.add_header('Content-ID', '<karpati_winter>')
msg_root.attach(msg_img_karpati_winter)

with open('new-year-spb.jpg', 'rb') as img:
    msg_img_new_year_spb = MIMEImage(img.read())
msg_img_new_year_spb.add_header('Content-ID', '<new-year-spb>')
msg_root.attach(msg_img_new_year_spb)


try:
    email_conn = SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    email_conn.sendmail(from_email, to_list, msg_root.as_string()) 
    email_conn.quit()
    print("Message was sent")
except SMTPException: 
    print("Error occuer")
