from .models import Marks,Subjects
from rest_framework.serializers import ModelSerializer

class MarkSerializer(ModelSerializer):
    class Meta:
        model = Marks
        exclude =['student']
        
class SubjectSerializer(ModelSerializer):
    class Meta:
        model= Subjects
        fields = '__all__'
