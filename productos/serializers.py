from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        # fields = ('id', 'nombre', 'descripcion', 'precio', 'stock')