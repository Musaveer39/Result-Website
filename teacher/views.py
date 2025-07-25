from django.shortcuts import render 
from rest_framework.views import APIView
from student.models import studentData
from teacher.models import Marks, Subjects
from rest_framework.response import Response
from django import forms
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


def teacherView(request,_id):
    data = studentData.objects.filter(sem=_id)
    context = {
        'data':data
    }
    return render(request,'teacher.html',context)


def teacher(request,sem,_usn):
    subs =Subjects.objects.filter(sem=sem)
    sub_list=list(subs.values())
    for ind, sub in enumerate(sub_list):
        sub['im'] = f'sub{ind+1}_im'
        sub['em'] = f'sub{ind+1}_em'
    
    return render(request,'marks_form.html',{'usn':_usn,'sub':sub_list})

def teacherLogin(request):
    return render(request,'login.html',{})

def sem(request):
    sem=[]
    for i in range(1,9):
        sem.append({'s':f'Semester {i}','id':i})
    return render(request,'sem.html',{'sem':sem})

class MarksEntry(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self, request, _usn):
        try:
            student = studentData.objects.get(usn=_usn)
            marks_instance, created = Marks.objects.update_or_create(
                student=student.usn, defaults=request.data
            )

            if created:
                return Response({"message": "Marks saved successfully"}, status=201)
            else:
                return Response({"message": "Marks updated successfully"}, status=200)

        except studentData.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)

        except Exception as e:
            return Response({"error": str(e)}, status=500)

def register(request):
    return render(request,'stud_register.html',{})

def principal(request):
    return render(request,'prin_login.html',{})

def home(request):
    return render(request,'home.html',{})