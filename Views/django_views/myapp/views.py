from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView 
from .forms import ContactForm

from .models import Student
## TemplateView

class HomeTemplateView1(TemplateView):
    template_name="myapp/home.html"

class HomeTemplateView2(TemplateView):
    template_name="myapp/home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']= 'Gaurav'
        context['id']= 100
        ## or 
        # context={'name':'Gaurav','id':100} ## but in this extra_context dose not work
        print(context)
        # {'course_id': 1, 'view': <myapp.views.HomeTemplateView2 object at 0x042CE2F8>, 'name': 'Gaurav', 'id': 100}

        print(kwargs)
        # {'course_id': 1}
        return context


## Redirect View

class GoogleRedirectView(RedirectView):
    url='https://www.google.com/'
    # pattern_name='/home/'
    # parmanant = True


class MyRedirectView(RedirectView):
    url="https://www.google.com/"

    # we can reconstruct url here
    def get_redirect_url(self, *args, **kwargs) :
        print(kwargs) #{'pk': 15}
        return super().get_redirect_url(*args, **kwargs)



# ************ Generic view ***********

# ListView
# class StudentListView(ListView):
#     model=Student

class StudentListView(ListView):
    model=Student
    ## This is same as below
    ## students = Student.objects.all()
    ## context = {"student_list":students}
    ## return render(request,'myapp/student_list.html',context)

    # template_name="myapp/stundet_get" ## default  appname/modelname_list.html ie student_list.html
    # template_name_suffix="_get" ## default -> "_list"
    # ordering=["name"] ## order by name -> default as inserted in db


class StudentListView1(ListView):
    model=Student
    template_name="myapp/students.html" ## default  appname/modelname_list.html ie student_list.html
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course="Java")

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context["freshers"]= Student.objects.all().order_by('name')
        return context


    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = "myapp/superuser.html"
        elif self.request.user.is_staff:
            template_name = "myapp/superuser.html"
        else:
            template_name = self.template_name
        return template_name
        
## Detail view 
     
class StudentDetailView(DetailView):
    model = Student


class StudentDetailView1(DetailView):
    model = Student
    pk_url_kwarg="id"
    template_name="myapp/student.html"
    context_object_name="student"


## Editing view
## form view

class ContactFormView(FormView):
    template_name = "myapp/contact.html" ## required to define
    form_class = ContactForm
    success_url = "/thankyou/"
    initial={'name':'Gaurav'}
    
    def form_valid(self, form) :
        name = form.cleaned_data['name']
        print(name)
        # return super().form_valid(form)
        return HttpResponse("Msg sent")


def thankyou(request):
    return HttpResponse("thank you")


class StudentCreateView(CreateView):
    model = Student
    fields = ['name','roll','course']
    success_url="/create/"


# Update View

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','roll','course']
    success_url = "/thankyou/"

# delete View
class StudentDeleteView(DeleteView):
    model = Student 
    success_url = "/thankyou/"
