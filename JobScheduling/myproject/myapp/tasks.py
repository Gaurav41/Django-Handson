
import datetime
from celery import shared_task
from django.core.mail import send_mail 

# @celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=1)) # here we assume we want it to be run every 5 mins
# def myTask():
#     print('This wasn\'t so difficult')

@shared_task(blind=True)
def test_func():
    #operations
    # for i in range(0,10):
    #     print(i)
    return "done test func"

@shared_task(blind=True)
def send_mail_func():
    print("send mail function")
    to = 'gauravpingale4@gmail.com'
    subject = "Celery Test"
    message = "Celery test mail"
    email_from = "gauravpingale19999@gmail.com"
    recipient_list = []
    recipient_list.append(to)
    send_mail(subject,message,email_from,recipient_list,fail_silently=False)
    return "Done"
      

