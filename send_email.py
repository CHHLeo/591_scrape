import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(title, msg):
    fromaddr = 'chhsieh.leo@gmail.com'
    toaddrs = 'chhsieh.leo@gmail.com'

    # Credentials (if needed)
    username = 'chhsieh.leo@gmail.com'
    password = '21070527crab'
    msg_out = MIMEMultipart('alternative')
    msg_out['Subject'] = title
    msg_out.attach(MIMEText(msg, 'plain'))

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    # msg = msg.split('\n')
    # for i in msg:
    #     msg_out.attach(MIMEText(u'<a href=' + i + '></a>', 'html'))
    # print msg_out.as_string()
    server.sendmail(fromaddr, toaddrs, msg_out.as_string())
    server.quit()

def send_mail_CN(title, msg):
    fromaddr = 'chhsieh.leo@gmail.com'
    toaddrs = 'pb791008@gmail.com'

    # Credentials (if needed)
    username = 'chhsieh.leo@gmail.com'
    password = '21070527crab'
    msg_out = MIMEMultipart('alternative')
    msg_out['Subject'] = title
    msg_out.attach(MIMEText(msg, 'plain'))

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    # msg = msg.split('\n')
    # for i in msg:
    #     msg_out.attach(MIMEText(u'<a href=' + i + '></a>', 'html'))
    # print msg_out.as_string()
    server.sendmail(fromaddr, toaddrs, msg_out.as_string())
    server.quit()
