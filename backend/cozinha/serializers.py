from rest_framework import serializers
from cozinha.models import Restaurante

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

        