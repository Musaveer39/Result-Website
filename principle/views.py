from django.shortcuts import render, redirect
from teacher.models import Subjects

# Create your views here.
def principal(request):
    return render(request,'prin_login.html',{})

def sems(request):
    sem=[]
    for i in range(1,9):
        sem.append({'s':f'Semester {i}','id':i})
    return render(request,'psem.html',{'sem':sem})

def subjects(request, sem_id):
    subjects = Subjects.objects.filter(sem=sem_id)
    sem_name = {1: 'First Semester', 2: 'Second Semester', 3: 'Third Semester',
                4: 'Fourth Semester', 5: 'Fifth Semester', 6: 'Sixth Semester',
                7: 'Seventh Semester', 8: 'Eighth Semester'}
    return render(request, 'subjects.html', {'sem_id': sem_id, 'subjects': subjects, 'sem_name': sem_name.get(sem_id, 'Unknown Semester')})

def add_subjects(request, sem_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        max_im = request.POST.get('max_internal')
        max_em = request.POST.get('max_external')

        subject = Subjects(name=name, max_im=max_im, max_em=max_em, sem=sem_id)
        subject.save()

        return redirect('subjects', sem_id=sem_id)

    return render(request, 'add_subjects.html', {'sem_id': sem_id})

def delete_subject(request, subject_id):
    try:
        subject = Subjects.objects.get(id=subject_id)
        subject.delete()
        return redirect('subjects', sem_id=subject.sem)
    except Subjects.DoesNotExist:
        return render(request, 'subjects.html', {'error': 'Subject not found'})