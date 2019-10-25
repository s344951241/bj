
import smtplib
from email.mime.text import MIMEText
from email.header import  Header

sender = '344951241@qq.com'
receivers = ['shileiyes@sina.com']

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg,'html','utf-8')
#message = MIMEText("test",'plain','utf-8')
message['From'] = Header("菜鸟教程",'utf-8')
message['To'] = Header("测试",'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject,'utf-8')

smtpServer = "smtp.qq.com"
smtpPassword = "mzrmquhshnfqcahj"

try:
    smtpObj = smtplib.SMTP(host=smtpServer)

    smtpObj.set_debuglevel(1)
    smtpObj.connect(host=smtpServer,port=587)
    smtpObj.starttls()
    smtpObj.login(sender,smtpPassword)

    smtpObj.sendmail(sender,receivers,message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
