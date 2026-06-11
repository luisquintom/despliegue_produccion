from rest_framework import serializers
from .models import Agencia, Mision

class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        fields = '__all__'

class MisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mision
        fields = '__all__'

    # VALIDACIÓN no puede ser negativo
    def validate_coste_lanzamiento(self, value):
        if value < 0:
            raise serializers.ValidationError("El coste de lanzamiento no puede ser negativo.")
        return value