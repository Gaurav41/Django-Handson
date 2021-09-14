from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail 


# >>> from django.core.mail import send_mail
# >>> send_mail("django test mail","hello world mail by django","gauravpingale19999@gmail.com",["gauravpingale4@gmail.com"])
# 1
# >>> send_mail("django test mail","hello world mail by django","gauravpingale4@gmail.com",["gauravpingale4@gmail.com"])     
# 1

def send_email(request):
    if request.method == "POST":
        to = request.POST['to']
        subject = request.POST['subject']
        message = request.POST['message']
        email_from = "gauravpingale19999@gmail.com"
        recipient_list = []
        recipient_list.append(to)
        send_mail(subject,message,email_from,recipient_list,fail_silently=False)
        return HttpResponse("Email sent successfully")
    else:
        return render(request,"myapp/sendmail.html")


def send_mass_emails(request):
    email1 = ("this is a email1 subject","this is message1","gauravpingale19999@gmail.com",["gauravpingale4@gmail.com"])
    email2 = ("this is a email2 subject","this is message2","gauravpingale19999@gmail.com",["gauravpingale4@gmail.com"])
    send_mass_mail((email1,email2),fail_silently=False)
    return HttpResponse("Mass Emails are sent successfully")