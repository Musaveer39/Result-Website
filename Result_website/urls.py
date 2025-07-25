"""
URL configuration for Result_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from student.views import StudentView,result,resultHome
from teacher.views import teacherView ,MarksEntry,teacher,teacherLogin,sem,home,register
from principle.views import principal,sems,subjects,add_subjects,delete_subject
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('', home),
    path('student/', StudentView.as_view()),
    path('teacher/<int:_id>/', teacherView),
    #path('teacher/', principal),
    path('principal/<int:sem_id>/', subjects, name='subjects'),
    path('principal-login/', principal),
    path('principal/add-subjects/<int:sem_id>/', add_subjects),
    path('principal/delete/<int:subject_id>/', delete_subject),
    path('principal/sem/', sems),
    path('login/', teacherLogin),
    path('teacher/sem/', sem),
    path('teacher/<int:sem>/<str:_usn>/' ,teacher),
    path('api/enter-marks/<str:_usn>/' ,MarksEntry.as_view()),
    path('result/<str:_usn>/' ,result),
    path('result/' ,resultHome),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
