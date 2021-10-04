
from django.db.models import fields
from rest_framework import serializers
from .models import *

class LoginSerializers(serializers.ModelSerializer):
   

    class Meta:
        model = Customers
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        

# class CustomersSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=



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
    users=UsersSerializers(read_only=True,many=False)
    products=ProductsSerializers(read_only=True,many=False)
    category=CategorySerializers(read_only=True,many=False)
    subcategories=SubCategorySerializers(read_only=True,many=False)
    orders=OrdersSerializer(read_only=True,many=False)


   
    class Meta:
        model=OrderTracking
        fields='__all__'



        
