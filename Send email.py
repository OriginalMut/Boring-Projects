import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "Jeffanicet45@gmail.com"
receiver_email = "Jeffanicet45@gmail.com"
password = "your_email_password"

# Email content
subject = "Test Email from Python"
body = "Hi there, this is a test email sent using Python!"

# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Login to your email account
        server.send_message(message)  # Send the email
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
