import smtplib
sender = 'sender@localhost.com'
receivers = 'receiver@localhost.com'
message = """

Subject: SMTP e-mail using python

Dear sir/mam,
       This the sample mail from python code
"""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
    print ("Successfully sent email")
except Exception:
    print( "Error: unable to send email") 
