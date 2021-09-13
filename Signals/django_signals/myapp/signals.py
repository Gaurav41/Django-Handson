from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_init,pre_init, pre_save,post_save,pre_delete,post_delete
from django.core.signals import  got_request_exception, request_finished, request_started

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("-------------------------Login Successful-------------------------------")
    print("Sender: ",sender)
    print("Request: ",request)
    print("User: ",user)
    print("User Name: ",user.username)
    print("User password: ",user.password)
    print(f"kwargs {kwargs}")

# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("--------------------------Log Out------------------------------")
    print("Sender: ",sender)
    print("Request: ",request)
    print(f"user {user} logged out...")
    print(f"kwargs {kwargs}")

# user_logged_out.connect(log_out,sender=User)

@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("--------------------------Login Failed------------------------------")
    print("Sender: ",sender)
    print("credentials: ",credentials)
    print("request: ",request)
    print(f"kwargs {kwargs}")

# user_login_failed.connect(login_failed)


# models signals

@receiver(pre_save,sender=User)
def pre_save_call(sender,instance,**kwargs):
    print("--------------------------pre_save------------------------------")
    print("Sender: ",sender)
    print("instance: ",instance)
    print(f"kwargs {kwargs}")

@receiver(post_save,sender=User)
def post_save_call(sender,instance,created,**kwargs):
    print("--------------------------Post Save------------------------------")
    print("Sender: ",sender)
    print("instance: ",instance)
    print(f"kwargs {kwargs}")
    if created:
        print("new resource created")
    else:
        print("old resource updated")

@receiver(pre_delete,sender=User)
def pre_delete_call(sender,instance,**kwargs):
    print("--------------------------Pre delete Signal------------------------------")
    print("Sender: ",sender)
    print("instance: ",instance)
    print(f"kwargs {kwargs}")
    print("Resource is going to delete")

@receiver(post_delete,sender=User)
def post_delete_call(sender,instance,**kwargs):
    print("--------------------------Post delete Signal------------------------------")
    print("Sender: ",sender)
    print("instance: ",instance)
    print(f"kwargs {kwargs}")
    print("Resource deleted")

@receiver(pre_init,sender=User)
def pre_init_call(sender,*args,**kwargs):
    print("--------------------------Pre init Signal------------------------------")
    print("Sender: ",sender)
    print(f"args {args}")
    print(f"kwargs {kwargs}")

    
@receiver(post_init,sender=User)
def post_init_call(sender,*args,**kwargs):
    print("--------------------------Post init Signal------------------------------")
    print("Sender: ",sender)
    print(f"args {args}")
    print(f"kwargs {kwargs}")

@receiver(request_started)
def request_started_call(sender,environ,**kwargs):
    print("--------------------------Request started Signal------------------------------")
    print("Sender: ",sender)
    print("environ: ", environ)
    print(f"kwargs {kwargs}")

@receiver(request_finished)
def request_finished_call(sender,**kwargs):
    print("--------------------------Request finished Signal------------------------------")
    print("Sender: ",sender)
    print(f"kwargs {kwargs}")

@receiver(got_request_exception)
def got_request_exception_call(sender,request,**kwargs):
    print("--------------------------Got Request exception Signal------------------------------")
    print("Sender: ",sender)
    print("request: ", request)
    print(f"kwargs {kwargs}")