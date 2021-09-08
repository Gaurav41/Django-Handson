from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(timeout=60,)
def index(request):
    return render(request,"index.html")

@cache_page(timeout=20)
def contact(request):
    return render(request,"contact.html")
