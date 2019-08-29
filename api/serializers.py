from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields = '__all__'
        #depth = 1

class ResponsableListSerializer(serializers.ModelSerializer):
    def to_representation(self,instance):
        if isinstance(instance,Persona):
            return PersonaSerializer(instance = instance).data
        else:
            return AreaSerializer(instance = instance).data
    class Meta:
        model= Responsable
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Estado
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Persona
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Area
        fields = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tipo_producto
        fields = '__all__'
