from rest_framework import serializers
from rest_framework.reverse import reverse

from blog.models import Sponsor
from .models import Student, Metsenat


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'username', 'student_type', 'otm', 'kontrakt', 'created_at')

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'username')

class MetsenatSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer(read_only=True)
    sponsor_id = serializers.IntegerField(write_only=True)
    student_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Metsenat
        fields = ('summa', 'created_at', 'sponsor', 'sponsor_id', 'student_id')
