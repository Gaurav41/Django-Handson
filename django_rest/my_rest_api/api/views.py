from functools import partial
import json
from django.contrib.auth.models import User, Group
import requests
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .serializers import StudentSerializer,StudentModelSerializer
from .models import Student

import io
from rest_framework.parsers import JSONParser
from django.views.decorators import csrf

# Create your views here.

def student_details(request,pk):
    student = Student.objects.get(id=pk) # complext data
    serializers = StudentSerializer(student) # to python dict  
    json_data = JSONRenderer().render(serializers.data) # JSON
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializers.data)

# Query set
def students_details(request):
    students = Student.objects.all() # complext data
    serializers = StudentSerializer(students,many=True) # to python object (non dict)  
    json_data = JSONRenderer().render(serializers.data) # JSON
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializers.data,safe=False)

@csrf.csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data=request.body
        stream = io.BytesIO(json_data)
        python_obj = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_obj)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data Inserted"}
            json_data = JSONRenderer().render(response)
        else:
            json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data,content_type="application/json") 
    else:
        return "None"

@csrf.csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        if id is not None:
            students = Student.objects.get(pk=id) 
            serializers = StudentSerializer(students)
        else:
            students = Student.objects.all() 
            serializers = StudentSerializer(students,many=True)
            
        json_data = JSONRenderer().render(serializers.data) 
        # return HttpResponse(json_data,content_type="application/json")
        return JsonResponse(serializers.data,safe=False)
    
    elif request.method == "POST":
        json_data=request.body
        stream = io.BytesIO(json_data)
        python_obj = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_obj)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data Inserted"}
            json_data = JSONRenderer().render(response)
        else:
            json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data,content_type="application/json")
    
    elif request.method == "PUT":
        json_data=request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')

        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student,data=python_data,partial=True)

        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data Update"}
            json_data = JSONRenderer().render(response)
        else:
            json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data,content_type="application/json") 

    elif request.method == "DELETE":
        json_data=request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(pk=id)
        student.delete()
        response = {"msg":"Data deleted"}
        # json_data = JSONRenderer().render(response)
        # return HttpResponse(json_data,content_type="application/json") 
        return JsonResponse(response,safe=False)


## Class based api

from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf.csrf_exempt,name='dispatch')
class StudentApi(View):

    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        if id is not None:
            students = Student.objects.get(pk=id) 
            # serializers = StudentSerializer(students)
            serializers = StudentModelSerializer(students)
        else:
            students = Student.objects.all() 
            # serializers = StudentSerializer(students,many=True)
            serializers = StudentModelSerializer(students,many=True)
            
        json_data = JSONRenderer().render(serializers.data) 
        # return HttpResponse(json_data,content_type="application/json")
        return JsonResponse(serializers.data,safe=False)

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream = io.BytesIO(json_data)
        python_obj = JSONParser().parse(stream)
        # serializer = StudentSerializer(data=python_obj)
        serializer = StudentModelSerializer(data=python_obj)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data Inserted"}
            json_data = JSONRenderer().render(response)
        else:
            json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data,content_type="application/json")
    
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')

        student = Student.objects.get(pk=id)
        # serializer = StudentSerializer(student,data=python_data,partial=True)
        serializer = StudentModelSerializer(student,data=python_data,partial=True)

        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data Update"}
            json_data = JSONRenderer().render(response)
        else:
            json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data,content_type="application/json") 

    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(pk=id)
        student.delete()
        response = {"msg":"Data deleted"}
        # json_data = JSONRenderer().render(response)
        # return HttpResponse(json_data,content_type="application/json") 
        return JsonResponse(response,safe=False)



################################## FUNCTION BASED API VIEW #####################################

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions,status

# @api_view()
# @permission_classes((permissions.AllowAny,))
# def hello_world(request):
#     return Response({'msg':'Hello World'})


# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def hello_p(request):
#     print(request.data)
#     return Response({'msg':'Post request'})


@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def hello(request):

    if request.method == 'GET':
        return Response({'msg':'Get method called'})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'Post method called','data':request.data})



@api_view(['GET','POST','PUT','PATCH','DELETE'])
@permission_classes((permissions.AllowAny,))
def rest_api(request,pk=None):
   
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            try:
                students = Student.objects.get(pk=id) 
                # serializers = StudentSerializer(students)
                serializers = StudentModelSerializer(students)
            except:
                response = {"error":"Not Found"}
                return Response(response,status=status.HTTP_404_NOT_FOUND)

        else:
            students = Student.objects.all() 
            # serializers = StudentSerializer(students,many=True)
            serializers = StudentModelSerializer(students,many=True)
        
        return Response(serializers.data,status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data Inserted"}
            return Response(response,status=status.HTTP_201_CREATED)
   
        else:
            response = serializer.errors
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        
        # id = request.data.get('id')
        id = pk
        try:
            student = Student.objects.get(pk=id)
            serializer = StudentModelSerializer(student,data=request.data)

            if serializer.is_valid():
                serializer.save()
                response = {"msg":"Data Update"}
                return Response(response,status=status.HTTP_200_OK)

            else:
                response = serializer.errors
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
                
        except:
                response = {"error":"Not Found"}
                return Response(response,status=status.HTTP_404_NOT_FOUND)


    if request.method == 'PATCH':
        
        # id = request.data.get('id')
        id=pk
        try:
            student = Student.objects.get(pk=id)
            serializer = StudentModelSerializer(student,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response = {"msg":"Data Update"}
                return Response(response,status=status.HTTP_200_OK) 
            else:
                response = serializer.errors
                return Response(response,status=status.HTTP_400_BAD_REQUEST)

        except:
                response = {"error":"Not Found"}
                return Response(response,status=status.HTTP_404_NOT_FOUND)

        


    if request.method == 'DELETE':
        
        # id = request.data.get('id')
        id = pk
        try:
            student = Student.objects.get(pk=id)
            student.delete()
            response = {"msg":"Data deleted"}
            return Response(response,status=status.HTTP_200_OK)

        except:
            response = {"error":"Some error occured while deleting data"}
            return Response(response,status=status.HTTP_404_NOT_FOUND)


