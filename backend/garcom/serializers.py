from rest_framework import serializers
from garcom.models import Garcom


class GarcomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garcom
        fields = '__all__'