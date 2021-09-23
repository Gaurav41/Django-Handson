from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail 
from .tasks import test_func,send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule


# >>> from django.core.mail import send_mail
# >>> send_mail("django test mail","hello world mail by django","gauravpingale19999@gmail.com",["gauravpingale4@gmail.com"])
# 1
# >>> send_mail("django test mail","hello world mail by django","gauravpingale4@gmail.com",["gauravpingale4@gmail.com"])     
# 1

# def send_email(request):
#         to = 'gauravpingale4@gmail.com'
#         subject = "hi from Django"
#         message = "hi from Django"
#         email_from = "gauravpingale19999@gmail.com"
#         recipient_list = []
#         recipient_list.append(to)
#         send_mail(subject,message,email_from,recipient_list,fail_silently=False)
#         return HttpResponse("mail sent")
      


# def send_mass_emails(request):
#     email1 = ("this is a email1 subject","this is message1","gauravpingale19999@gmail.com",["gauravpingale4@gmail.com"])
#     email2 = ("this is a email2 subject","this is message2","gauravpingale19999@gmail.com",["gauravpingale4@gmail.com"])
#     send_mass_mail((email1,email2),fail_silently=False)
#     return HttpResponse("Mass Emails are sent successfully")



def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    # send_mail_func.delay()
    return HttpResponse("Sent")

def schedule_mail(request):
    if request.method == 'POST':
        day = request.POST['day'] 
        month = request.POST['month']
        hr = request.POST["hr"]
        min = request.POST['min'] 
        count = PeriodicTask.objects.all().count()
        # print("count ",count)
        name = "schedule_mail_task_"+ str(count) # so the every name will be unique
        schedule, created = CrontabSchedule.objects.get_or_create(hour = hr, minute = min,day_of_month=day,month_of_year=month)
        task = PeriodicTask.objects.create(crontab=schedule, name=name, task='myapp.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
        return HttpResponse("Done")
    else:
        return render(request,"myapp/schedule_mail.html")