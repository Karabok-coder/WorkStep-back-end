import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Data.config import PATH_HTML_CODE


class Sender():
    def __init__(self) -> None:
        self.sender = """WorkStepHelp@yandex.ru"""
        self.password = """pitjhgdkgmjtdyxz"""

    def sendCode(self, code: str, username: str, reciver: str):
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = reciver
        message['Subject'] = 'Код подтверждения'  # Указываем тему письма
        with open(PATH_HTML_CODE, 'r') as file: # Берем разметку для письма
            html = file.read().replace('"КОД"', str(code)).replace('"ИМЯ"', str(username))
        message.attach(MIMEText(html, 'html'))
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        smtpObj = smtplib.SMTP_SSL('smtp.yandex.ru', 465, context=context)
        smtpObj.login(self.sender, self.password)
        smtpObj.sendmail(self.sender, reciver, message.as_string())
        smtpObj.quit()


# sender = 'WorkStepHelp@yandex.ru'
# reciver = 'karabok122133@gmail.com'

# msg = MIMEMultipart()
# msg['From'] = sender
# msg['To'] = reciver
# msg['Subject'] = 'Тема письма'  # Указываем тему письма

# with open('mailll.html', 'r') as file:
#     html = file.read()

# msg.attach(MIMEText(html, 'html'))

# context = ssl.SSLContext(ssl.PROTOCOL_TLS)
# smtpObj = smtplib.SMTP_SSL('smtp.yandex.ru', 465, context=context)
# # msg = f'From: {sender}\r\nTo: {reciver}\r\n\r\nHello'
# smtpObj.login(sender, 'kqvkblszwxpblfjk')
# smtpObj.sendmail(sender, reciver, msg.as_string())
# smtpObj.quit()
# print('success')