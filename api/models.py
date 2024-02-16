from django.db import models
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=50)
    

class Item(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    stock_status = models.CharField(max_length=20)
    available_stock = models.IntegerField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

# Views

class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


