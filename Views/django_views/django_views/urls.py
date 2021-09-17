"""django_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import Pattern
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    ## TemplateView
    path('', views.TemplateView.as_view(template_name="myapp/index.html"),name="index"),
    path('home1', views.HomeTemplateView1.as_view(),name="home1"),
    path('home2', views.HomeTemplateView2.as_view(),name="home2"),
    path('home3', views.HomeTemplateView2.as_view(extra_context={"course":'django'}),name="home3"),
    path('home4/<int:course_id>', views.HomeTemplateView2.as_view(),name="home4"),

    ## RedirectView
    path('index', views.TemplateView.as_view(template_name="myapp/index.html"),name="index"),
    path('home', views.RedirectView.as_view(url="index"),name="home"),
    path('youtube', views.RedirectView.as_view(url="https://www.youtube.com/"),name="youtube"),
    path('google', views.GoogleRedirectView.as_view(),name="google"),

    path('second', views.RedirectView.as_view(url="/something/"),name="second"),
    path('first', views.RedirectView.as_view(pattern_name='second'),name="first"),

    path('my/<int:pk>/', views.MyRedirectView.as_view(),name="my"),

    ## List View
    path('students/', views.StudentListView.as_view() ,name="students"),
    path('students1/', views.StudentListView1.as_view() ,name="students1"),

    ## Detail View
    path('students/<int:pk>', views.StudentDetailView.as_view() ,name="student_detail"),
    # path('students/<int:id>', views.StudentDetailView1.as_view() ,name="student_detail1"),


    ## Editing view
    # Form view
    path('contact/', views.ContactFormView.as_view() ,name="contact"),
    path('thankyou/', views.thankyou,name="thankyou"),

    # detail view
    path('create/', views.StudentCreateView.as_view(),name="create_student"),
    path('update/<int:pk>', views.StudentUpdateView.as_view(),name="update_student"),
    path('delete/<int:pk>', views.StudentDeleteView.as_view(),name="delete_student"),



]

