from apps.campeon.models import CampeonM
from rest_framework import serializers

class CampeonSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CampeonM
        fields = ('__all__')