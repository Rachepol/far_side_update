import smtplib, ssl

def send_message(address):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "hermes.message.bag@gmail.com"  # Enter your address
    receiver_email = "fcressotti@gmail.com"  # Enter receiver address
    #password = input("Type your password and press enter: ")
    password = "1TN{sS4QeF5r"
    message = """\
    Subject: New Far Side Comic!

    There's no new far side comic!"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
