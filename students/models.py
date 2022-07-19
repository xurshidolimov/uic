from django.db import models
from django.utils import timezone
from blog.models import Sponsor


class Student(models.Model):
    CHOICES = [
        ('bakalavr', 'bakalavr'),
        ('magistr', 'magistr'),
    ]
    username = models.CharField(max_length=60)
    student_type = models.CharField(max_length=120, choices=CHOICES, default='bakalavr')
    otm = models.CharField(max_length=250)
    kontrakt = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class Metsenat(models.Model):
    summa = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.sponsor} {self.student}ga {self.summa} ajratdi'


