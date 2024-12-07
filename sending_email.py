import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_signup_email_outlook(recipient_email: str, username: str):
    sender_email = "zhngyiyan@gmail.com"
    sender_password = "btzl rxxu opoe cwoh"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # 创建邮件内容
    subject = "Welcome to Our Service!"
    body = f"""
    Hi {username},

    Thank you for signing up for our service! We're excited to have you on board.

    Best regards,
    The Team
    """
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # 连接到 SMTP 服务器并发送邮件
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # 启用 TLS 加密
            server.login(sender_email, sender_password)  # 登录到 SMTP 服务器
            server.sendmail(sender_email, recipient_email, message.as_string())  # 发送邮件
        print(f"Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
send_signup_email_outlook("zhangyiyanwilson@outlook.com", "Yiyan")