from django.shortcuts import render
from django.contrib.auth.models import User
#from rest_framework import permissions
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import permission_classes

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.http import HttpResponse


# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)


#     if not user:
#         return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key}, status=HTTP_200_OK)

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer =  LoginSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LoginAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset = Customers.objects.all()
   
    serializer_class = LoginSerializers
    permission_classes=[AllowAny]
    authentication_classes=[TokenAuthentication]
    
    
    # def post(self, request):

    #     serializer = LoginSerializers(data=request.data) 
    #     if serializer.is_valid(): 
    #         serializer.save() 
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
         return self.create(request)

        
    def login(request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
         return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)


        if not user:
         return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)

        

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        print(request)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })



# Create your views here.

class UsersAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Users.objects.all()
   
    serializer_class = UsersSerializers
    
    lookup_field = 'user_id'
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    #@permission_classes(IsAuthenticated)
    def get(sef, request, user_id = None):
        user=request.user
        print(user)
        # role=request.role
        # print(role)
        # if Users.role!=user:
        #     return Response({"response":"you don't have a permission to edit that"})
        
        if user_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
        
        




      
    def post(self, request ):
            return self.create(request)
        
          
    def put(self, request, user_id=None):
         return self.update(request, user_id)
    
    def delete(self, request, user_id):
             return self.destroy(request, user_id)


class ProductsAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Products.objects.all()
    serializer_class =ProductsSerializers

   
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
   
    

    lookup_field = 'product_id'
       
    def get(sef, request, product_id = None):
        if product_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
   # @permission_classes([AllowAny])      
    def post(self, request):
              return self.create(request)
    
    def put(self, request, product_id=None):
             return self.update(request, product_id)
    
    def delete(self, request, product_id):
             return self.destroy(request, product_id)

class CategoryAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class =CategorySerializers

    lookup_field = 'category_id'

    def get(sef, request, category_id = None):
        if category_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
    
    def post(self, request):
              return self.create(request)
    
    def put(self, request, category_id=None):
             return self.update(request, category_id)
    
    def delete(self, request, category_id):
             return self.destroy(request, category_id)

class SubCategoryAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Subcategory.objects.all()
    serializer_class =SubCategorySerializers

    lookup_field = 'subcat_id'

    def get(sef, request, subcat_id = None):
        if subcat_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
    
    def post(self, request):
              return self.create(request)
    
    def put(self, request, subcat_id=None):
             return self.update(request, subcat_id)
    
    def delete(self, request, subcat_id):
             return self.destroy(request, subcat_id)



class OrdersAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Orders.objects.all()
    serializer_class =OrdersSerializer

    lookup_field = 'order_id'
    #permission_classes=[AllowAny]


    def get(sef, request, order_id = None):
        if order_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
    
    def post(self, request):
              return self.create(request)
    
    def put(self, request, order_id=None):
             return self.update(request, order_id)
    
    def delete(self, request, order_id):
             return self.destroy(request, order_id)


class OrderTrackingAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = OrderTracking.objects.all()
    serializer_class =OrderTrackingSerializer

    lookup_field = 'tracking_id'

    def get(sef, request, tracking_id = None):
        if tracking_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
    
    def post(self, request):
              return self.create(request)
    
    def put(self, request, tracking_id=None):
             return self.update(request, tracking_id)
    
    def delete(self, request, tracking_id):
             return self.destroy(request, tracking_id)
