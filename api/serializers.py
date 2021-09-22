from django.db.models import fields
from rest_framework import serializers
from .models import *

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields='__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class SubCategorySerializers(serializers.ModelSerializer):
    #category=CategorySerializers(many=True)
    class Meta:
        model=Subcategory
        fields='__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields='__all__'

class OrderTrackingSerializer(serializers.ModelSerializer):
    #properties=PropertiesSerializers(read_only=True,many=True)
    users=UsersSerializers(read_only=True,many=False)
    products=ProductsSerializers(read_only=True,many=False)
    category=CategorySerializers(read_only=True,many=False)
    subcategories=SubCategorySerializers(read_only=True,many=False)
    orders=OrdersSerializer(read_only=True,many=False)

   
    class Meta:
        model=OrderTracking
        fields='__all__'



        
