from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=20, required = True)
    last_name = serializers.CharField(max_length=20, required = True)
    address = serializers.CharField(max_length=100, required = True)
    roll_no = serializers.IntegerField()
    mobile = serializers.CharField(max_length=10, required = True)

    class Meta:
        model = Students
        fields = ('__all__')
