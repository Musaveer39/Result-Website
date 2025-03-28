from django.db import models
from student.models import studentData
class Subjects(models.Model):
    name = models.CharField(max_length=20)
    max_im = models.IntegerField()
    max_em = models.IntegerField()
    sem = models.IntegerField()

class Marks(models.Model):
    student = models.CharField(primary_key=True,max_length=10)
    sub1_im = models.IntegerField(null=True,blank=True)
    sub2_im = models.IntegerField(null=True,blank=True)
    sub3_im = models.IntegerField(null=True,blank=True)
    sub4_im = models.IntegerField(null=True,blank=True)
    sub5_im = models.IntegerField(null=True,blank=True)
    sub6_im = models.IntegerField(null=True,blank=True)
    sub1_em = models.IntegerField(null=True,blank=True)
    sub2_em = models.IntegerField(null=True,blank=True)
    sub3_em = models.IntegerField(null=True,blank=True)
    sub4_em = models.IntegerField(null=True,blank=True)
    sub5_em = models.IntegerField(null=True,blank=True)
    sub6_em = models.IntegerField(null=True,blank=True)
