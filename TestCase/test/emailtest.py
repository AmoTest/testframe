
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务
# 如果使用QQ邮箱，运行代码前请将mail_user与mail_pwd替换为自己的邮箱

# 设置邮箱服务器
mail_host = "smtp.qq.com"

# 设置邮箱账户
mail_user = "2715756433@qq.com"
mail_pwd = "pumpdifbyqhmdhdg"  # QQ邮箱的授权码，不是邮箱密码

# 发件箱
sender = "2715756433@qq.com"
# 收件箱
recvers = ["2715756433@qq.com", "1721210300@qq.com"]

subject = '测试报告邮件'

message = MIMEText('测试报告测试邮件', 'plain', 'utf-8')
message['From'] = Header("自动化测试组", 'utf-8')
message['To'] = Header("项目组成员", 'utf-8')
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pwd)
    smtpObj.sendmail(sender, recvers, message.as_string())
    print("发送成功")
except smtplib.SMTPException:
    print("Error:发送邮件失败")






















































