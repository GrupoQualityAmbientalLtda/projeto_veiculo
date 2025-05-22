from src.controller.controller_avaria import ControllerAvaria
from datetime import datetime
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import smtplib, ssl
from email.message import EmailMessage


# carregando as variáveis de ambiente
load_dotenv()
    
def send_mail_zepto():
    port = 465
    smtp_server = "smtp.zeptomail.com"
    username=os.getenv('username')
    password =os.getenv('password')
    print(username)
    print(password)
    corpo = "Segue a relação das avarias: "
    avarias = ControllerAvaria.listar_avarias_verdadeiras()
    for avaria_dict in avarias:
            for nome, valor in avaria_dict.items():
                if valor:  # só adiciona se for True
                    corpo += f"\n- {nome}"

    msg = EmailMessage()
    msg['Subject'] = "REGISTRO: Veículo avariado encontrado."
    msg['From'] = "noreply@grupoqualityambiental.com.br"
    msg['To'] = "ti@grupoqualityambiental.com.br","ti.grupoqualityamb@gmail.com"
    msg.set_content(corpo)
    try:
        if port == 465:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                print(f'Username: {username}')
                print(f'Password: {password}')
                server.login(username, password)
                server.send_message(msg)
        else:
            print ("use 465 / 587 as port value")
            exit()
        print ("successfully sent")
    except Exception as e:
        print (e)   

send_mail_zepto()

username=os.getenv('username')
password = os.getenv('password')
print(username)
print(password)