from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('students/<int:pk>', views.student_details,name="Student Details"),
    path('students/', views.students_details,name="Students Details"),
    path('addstu/', views.create_student,name="addstu"),
    path('studentapi/', views.student_api,name="student_api"),
    path('studentapi_cls/', views.StudentApi.as_view(),name="StudentApi"),


    ##### Function based Api View
    # path('funviewapi/', views.hello_world,name="hello"),
    path('funviewapi/', views.hello,name="hello"),
    path('rest_api/', views.rest_api,name="rest_api"),
    path('rest_api/<int:pk>', views.rest_api,name="rest_api1"),

]