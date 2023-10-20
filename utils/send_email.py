import smtplib
import email.message
import os
from dotenv import load_dotenv

load_dotenv("credentials.env")
def send_email(json_data):
    
    display_name = os.getenv("DISPLAY_NAME") # Load Display Name from environment file
    my_email=os.getenv("EMAIL") # Load Email Address from environment file
    my_password = os.getenv("PASSWORD") # Load Password from environment file
    receiver_email = os.getenv("RECEIVER_EMAIL") # Load bot's email from environment file

    print(f"Sending as: {my_email}")

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email, my_password)

    # iterate through json and send it to the bot 
    for json in json_data:
        msg = email.message.EmailMessage()
        print(f"Sending Data of {json['file_name']}")
        msg['From'] = f'{display_name} <{my_email}>'
        msg['To'] = receiver_email
        msg['Subject'] = json['subject']

        # Encode the plain text content as UTF-8 and set charset
        msg.set_content(json['email_body'], subtype='plain', charset='utf-8')

        # Send the email
        server.sendmail(my_email, receiver_email, msg.as_string())
        
    # Close the connection to the SMTP server
    server.quit()
    print("Mail Sent")