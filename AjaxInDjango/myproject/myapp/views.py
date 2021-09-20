from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,HttpResponse
from .forms import UserRegistratation
from .models import User

# Create your views here.
def index(request):
    form = UserRegistratation()
    users = User.objects.all()
    return render(request,"myapp/index.html",{"form":form, "users":users})


def save_data(request):
    if request.method=="POST":
        form = UserRegistratation(request.POST)
        if form.is_valid():
            id = request.POST.get("id")
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if id :
                user=User(id=id,name=name,email=email,password=password)
            else:
                user=User(name=name,email=email,password=password)
            user.save()
            print("Data Saved *****************")
            users =User.objects.values()
            user_data = list(users)
            print(users) 
            return JsonResponse({'status':1,'user_data':user_data})
        else:
            return JsonResponse({'status':0})


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        user = User.objects.get(pk=id)
        user.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        user = User.objects.get(pk=id)
        user_data = {"id":user.id,"name":user.name,"email":user.email,"password":user.password}
        return JsonResponse(user_data)
    else:
        return JsonResponse({'status':0})