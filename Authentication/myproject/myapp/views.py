from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib import messages


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        print("***************************")
        # fm = UserCreationForm(request.POST)
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Account created successfully")
            print("Form Saved")
    else:
        # fm=UserCreationForm()
        fm=SignupForm()
    return render(request,'myapp/signup.html',{'form':fm})

def user_login(request):
    if request.method == 'POST':
        print("***************************")
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            print("***********Valid****************")
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            
            if user is not None :
                print("***********Login***********")
                login(request,user)
                messages.success(request,"Loggin successfull")
                print("Loggin successfull")

                # next = request.GET.get('next',None)
                next = request.POST .get('next',None)
                print('next:',next)
                if next :
                    return HttpResponseRedirect(next) 
                return HttpResponseRedirect("/profile/") 
    else:
        # fm=UserCreationForm()
        fm=AuthenticationForm()
    return render(request,'myapp/userlogin.html',{'form':fm})

# @login_required()
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,"myapp/profile.html",{'user':request.user})
    else:
        return HttpResponseRedirect("/login/")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")

@login_required(login_url="/login/")
def user_change_password(request):
    if request.method == "POST":
        ## requires old password to set new password
        fm = PasswordChangeForm(user=request.user,data=request.POST)

        ## Old password is not required to set new password
        # fm = SetPasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            # to keep user logged in
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect("/profile/")
        
    else:
        fm = PasswordChangeForm(request.user)
        # fm = SetPasswordForm(request.user)
    return render(request,"myapp/change_password.html",{'form':fm})