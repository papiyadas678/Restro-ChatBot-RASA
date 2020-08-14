# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:50:53 2020

@author: eroynab
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


### Method for sending the Email ####
def send_email(sender,reciever,sender_password,response):
    try:
        text = "These are the following search results."
        email_text = text + ("\n".join(response))
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = reciever
        msg['Subject'] = 'Results of Restaurant Search'
        msg.attach(MIMEText(email_text,'plain'))
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, sender_password)
        server.sendmail(sender, reciever, msg.as_string())
        server.close()
        return ("200")
    except Exception as e:  
        return("405",e)

