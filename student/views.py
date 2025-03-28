from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.views import APIView
from .models import studentData
from teacher.models import Marks,Subjects

class StudentView(APIView):
    def get(self,request):
        studData = studentData.objects.all()
        serial = StudentSerializer(studData, many=True)
        return Response({'status':'200','data':serial.data})
    def post(self,request):
        data=request.data.copy()
        data['usn']=data['usn'].upper()
        data['name']=data['name'].upper()
        serial = StudentSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return Response({'message':"Student registered"},status=200)
        else:
            return Response({"message": str(serial.errors)}, status=404)
        
def result(request,_usn):
    try:
        studData=studentData.objects.get(usn=_usn)
        sem=studData.sem
    except Exception:
        return render(request,'notregister.html',{})
    try:
        marks = Marks.objects.filter(student=_usn).values('sub1_im', 'sub1_em','sub2_im', 'sub2_em','sub3_im', 'sub3_em','sub4_im', 'sub4_em','sub5_im', 'sub5_em','sub6_im', 'sub6_em').get()
    except Exception:
        return render(request,'Invalid.html',{})
    sub_data = Subjects.objects.filter(sem=sem)  # Queryset of subjects
    subjects_list = list(sub_data.values())
    tot=0
    flag=False
    for index, subject in enumerate(subjects_list):
        subject['im'] = marks.get(f'sub{index+1}_im', 0)  # Default 0 if not found
        subject['em'] = marks.get(f'sub{index+1}_em', 0)
        if subject['im'] != None and subject['em']!=None:
            subject['total']=subject['im']+subject['em']
            tot+=subject['total']
            if subject['im']<18 or subject['em']<18:
                flag = True
                subject['status']='F'
            else:
                subject['status']='P'
        context1 = {
        'subject': subjects_list,  
        'student':studData,
        'tot':tot,
        'flag':flag
    }

    return render(request, 'result.html', context1)

def resultHome(request):
    return render(request,'resultHome.html',{})