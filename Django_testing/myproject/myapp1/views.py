from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"myapp1/index.html")

def home(request):
    return render(request,"myapp1/home.html")
