from django.db import models

class studentData(models.Model):
    usn = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=20)
    sem = models.IntegerField()


