from django.db import models
from django.utils import timezone


class Sponsor(models.Model):
    CHOICES=[
        ('yangi','yangi'),
        ('moderatsiyada','moderatsiyada'),
        ('tasdiqlangan', 'tasdiqlangan'),
        ('bekor qilingan', 'bekor qilingan')
    ]
    username = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=14)
    summa = models.PositiveIntegerField()
    holati = models.CharField(max_length=120, choices=CHOICES, default='yanngi')
    created_at = models.DateTimeField(default=timezone.now)
    tashkilot_nomi = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username