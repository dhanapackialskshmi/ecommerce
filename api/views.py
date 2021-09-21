from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics



# Create your views here.
class UsersAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers

    lookup_field = 'user_id'

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
