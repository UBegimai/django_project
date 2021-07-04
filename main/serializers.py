
from rest_framework import serializers

from .models import *




class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'image')

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
