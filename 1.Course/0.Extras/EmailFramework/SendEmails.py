import getpass
import smtplib

class SendMails:

    def __init__(self):

        self.from_mail = getpass.getpass('Your email: ')
        self.password = getpass.getpass('Your password: ')
        

    def gmailit(self,to_email, subject,body):
        email_obj = smtplib.SMTP(host='smtp.gmail.com', port=587)
        email_obj.ehlo()
        email_obj.starttls()
        email_obj.login(self.from_mail,self.password)
        msg = 'Subject:' +subject + '\n' + body
        print(f'msg is {msg}')
        #out = 'Success'
        out = email_obj.sendmail(self.from_mail, to_email, msg)
        #if out = '{}
        print(f'Output : {out}')
        print('email sent successfully!')
        email_obj.quit()





if __name__ == '__main__':
    mailer = SendMails()
    print(mailer.from_mail)
    print(mailer.password)
    sub = 'Test Subject'
    body = 'Test Test Test Test Test TEST'

    mailer.gmailit('rraghu21489@gmail.com',sub, body)