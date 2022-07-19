from .models import Sponsor
from rest_framework import serializers

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'username', 'phone_number', 'summa', 'holati', 'created_at', 'tashkilot_nomi')

