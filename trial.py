import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "wlstjd7056@gmail.com"
my_password = "aeadzyrrgsnbremx"
you = "wlstjd7056@naver.com"

## 여기서부터 코드를 작성하세요.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Alert"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)
## 여기에서 코드 작성이 끝납니다.

# Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)
s.sendmail(me, you, msg.as_string())
s.quit()