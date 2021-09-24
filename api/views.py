from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly,SAFE_METHODS
from rest_framework.authentication import TokenAuthentication



# Create your views here.
# permission_classes= [permissions.AllowAny]
# class UserWritePermission(BasePermission):
#     message='Admin oly having a write permission'
#     print('ss')

   
    #def has_object_permission(self, request, view, obj):
#         print('kl')
#         print(request)
#         if request.method in SAFE_METHODS:
#             retdhanadhadhhanaurn True
#         return obj.role == request.user
#@csrf_exempt
class UsersAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Users.objects.all()
    #print(queryset)
    serializer_class = UsersSerializers
    
    lookup_field = 'user_id'
    permission_classes=[AllowAny]
    authentication_classes=[TokenAuthentication]
    

    def get(sef, request, user_id = None):
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

    # permission_classes=[UserWritePermission]
    # #print(UserWritePermission)

    permission_classes=[IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    

    lookup_field = 'product_id'

    def get(sef, request, product_id = None):
        if product_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
    
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
