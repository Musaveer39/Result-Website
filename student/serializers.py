from rest_framework import serializers
from .models import studentData

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentData
        fields = '__all__'
    def validate(self, data):
        if len(data['usn'])<10:
            raise serializers.ValidationError({'error':'Usn must be ten digits'})
        return data
        