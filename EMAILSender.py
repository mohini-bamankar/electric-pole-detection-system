import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.base import MIMEBase
# from email import encoders

def send_mail(to,latitude,longitude ):

    sender_address = "jadhavanuja212@gmail.com"
    sender_pass = "iale igix hrsq hlml"
    mapurl = f"https://www.google.com/maps/dir/?api=1&destination={latitude},{longitude}"

    subject = "Unsafe Electric Pole Detected"
    body = (
        "⚠️ Alert: Unsafe Electric Pole Detected\n\n"
        "An electric pole has been identified as potentially unsafe at the location below. "
        "Immediate inspection and necessary action are requested to prevent any possible hazard.\n\n"
        f"Location (Google Maps): {mapurl}\n\n"
        "Please review the location and take appropriate safety measures at the earliest.\n\n"
        "Regards,\n"
        "Smart Electric Pole Monitoring System"
    )   
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = to
    message['Subject'] = subject

    # Email body
    message.attach(MIMEText(body, 'plain'))

    # # Attach Image
    # with open(image_path, 'rb') as img:
    #     mime = MIMEBase('application', 'octet-stream')
    #     mime.set_payload(img.read())
    #     encoders.encode_base64(mime)
    #     mime.add_header('Content-Disposition', f'attachment; filename={image_path}')
    #     message.attach(mime)

    # SMTP Session
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)

    text = message.as_string()
    session.sendmail(sender_address, to, text)
    session.quit()

    print("Mail Sent with Image")
    return 1