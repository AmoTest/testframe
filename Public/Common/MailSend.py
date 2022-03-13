
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class MailSend:

    def sendMail(self, hostname, mail_user, mail_pwd, file):

        mail_body = open(file, 'r').read()
        message = MIMEMultipart()
        message.attach(MIMEText(mail_body, "html", "utf-8"))
        message["To"] = Header('测试组', "utf-8")
        message["From"] = Header("项目组", "utf-8")

        subject = "测试报告标题"
        message["subject"] = Header(subject, "utf-8")

        att1 = MIMEText(mail_body, "html", "utf-8")
        att1['Content-Type'] = "application/octet-stream"
        att1['ContentDisposition'] = 'attachment, filename="report.html"'
        message.attach(att1)

        sender = "123@qq.com"
        recievers = ["123@qq.com", "abc@qq.com"]

        smtpObj = smtplib.SMTP()
        smtpObj.connect(hostname, '25')
        smtpObj.login(mail_user, mail_pwd)
        smtpObj.sendmail(sender, recievers, message.as_string())

if __name__ == "__main__":

    hostName = "smtp.qq.com"
    mail_User = "123@qq.com"
    mail_Pwd = ""

