
from datetime import datetime
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import smtplib, ssl
from email.message import EmailMessage


# carregando as variáveis de ambiente
load_dotenv()
    
def send_mail_zepto(corpo: str):
    port = 465
    smtp_server = "smtp.zeptomail.com"
    username=os.getenv('username')
    password =os.getenv('password')

    msg = EmailMessage()
    msg['Subject'] = "REGISTRO: Veículo avariado encontrado."
    msg['From'] = "noreply@grupoqualityambiental.com.br"
    msg['To'] = "ti@grupoqualityambiental.com.br","ti.grupoqualityamb@gmail.com"
    msg.set_content(corpo)
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(username, password)
            server.send_message(msg)
        print ("successfully sent")
    except Exception as e:
        print (e)   

