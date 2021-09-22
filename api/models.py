from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=False,blank=False)
    email     = models.CharField(max_length=32,null=True,blank=True)
    verified_email=models.BooleanField(default=False)
    mobile_no     =models.CharField(max_length=15,null=True,blank=True)
    verified_mobile_no =models.BooleanField(default=False)
    password      =models.CharField(max_length=10,default="",null=False)
    role=         models.CharField(max_length=20,null=True)
    address=models.TextField(null=True)

    class Meta:
         db_table="ec_users"




class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(unique=True,max_length=255,null=True,blank=True)
    category_desc=models.CharField(max_length=255)

    class Meta:
         db_table="ec_category"


class Subcategory(models.Model):
    subcat_id =models.AutoField(primary_key=True)
    parent_cat_id= models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=255,blank=False)
    subcategory_desc =models.CharField(max_length=255)

    class Meta:
         db_table="ec_subcategory"

class Products(models.Model):
    product_id =models.AutoField(primary_key=True)
    product_name =models.CharField(max_length=255,null=True,blank=False,unique=True)
    product_desc=models.CharField(max_length=255,null=False,blank=False)
    #models.ForeignKey(Products,on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category_id=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    specification=models.CharField(max_length=255,default="",blank=False)
    Image=models. FileField(upload_to = 'images/')
    #Image=models.JSONField
    stock=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    discount_price=models.IntegerField()
    brand=models.CharField(max_length=255)

    class Meta:
         db_table="ec_products"



class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    product_id =models.ForeignKey(Products,on_delete=models.CASCADE)
    user_id =models.ForeignKey(Users,on_delete=CASCADE)
    quantity=models.IntegerField(null=True)
    total_price=models.IntegerField(null=True)
    invoice_no=models.CharField(max_length=256,null=True,blank=True)
    payment_address=models.TextField(null=True,blank=True)
    shipping_address=models.TextField(null=True,blank=True)

    class Meta:
         db_table="ec_order"



class OrderTracking(models.Model):
    tracking_id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Orders,on_delete=CASCADE)
    shipment_status=models.CharField(max_length=100)
    current_location=models.CharField(max_length=255,null=True,blank=True)
    destination=models.CharField(max_length=255,null=True,blank=True)
    shipment_date=models.DateTimeField()

    class Meta:
         db_table="ec_order_tracking"
