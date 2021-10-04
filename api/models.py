from django.core import validators
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.core.validators import RegexValidator

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class Login(models.Model):

  id = models.AutoField(primary_key=True)
  username=models.CharField(max_length=255)
  password=models.CharField(max_length=255)
  token=models.CharField(max_length=250)

  class Meta:
      db_table="ec_login"

class UserManager(BaseUserManager):
 
    def get_by_natural_key(self, username,):
        return self.get(username=username)

class CustomAccountCustomer(BaseUserManager):

    def create_customeradmin(self, email, user, password, **other_fields):

        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        other_fields.setdefault('is_active', False)
        other_fields.setdefault('is_client_admin',True)
        other_fields.setdefault('is_student',False)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.user(email, user, password, **other_fields)

    def customeradmin(self, email,user, password, **other_fields):

        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        customeradmin = self.model(email=email, user=user,
                           **other_fields)
        customeradmin.set_password(password)
        customeradmin.save()
        return user


class Customers(AbstractBaseUser,PermissionsMixin):
        user_id = models.AutoField(primary_key=True)
        username = models.CharField(max_length=100,unique=True) 
        password = models.CharField(max_length=32)
        first_name=models.CharField(max_length=250) 
        last_name=models.CharField(max_length=250)
        email=models.EmailField(max_length=250,unique=True)
       # token=models.CharField(max_length=32)
        #is_active=models.BooleanField(default=True)
        #is_active= EnumChoiceField(enum_class=ChoiceTypes , default=ChoiceTypes.active)

        USERNAME_FIELD = 'username'
        REQUIRED_FIELDS = ['first_name','last_name',]

        objects = UserManager()
        class Meta:
             db_table="ec_customers"

        def __str__(self):
            return self.username

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255,null=False,blank=False,validators=[RegexValidator('^[a-zA-Z]*$',message='Firstname must be in Character')])
    last_name = models.CharField(max_length=255,null=False,blank=False,validators=[RegexValidator('^[a-zA-Z]*$',message='Lastname must be in Character')])
    #email     = models.CharField(max_length=32,null=True,blank=True)
    email=models.EmailField(null=False,blank=False)
    verified_email=models.BooleanField(default=False)
    
    mobile_no     =models.BigIntegerField(null=False,blank=False,validators=[RegexValidator(r'^([0-9]{10})$',message='mobile no must have 10 digit')])
    verified_mobile_no =models.BooleanField(default=False)
    password      =models.CharField(max_length=10,null=False,blank=False,validators=[RegexValidator('^(?=.*[!$?])(?=.*[a-z])(?=.*[A-Z]).{8}$',message='invalid password.Password must be 8 characters.and atleast 1 numeric and symbols')])
    role=         models.CharField(max_length=20,null=False,default='guest',validators=[RegexValidator(r'^[a-zA-Z -.\'\_]+$',message='Role must be in Character')])
    address=models.TextField(null=False,blank=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
   
    class Meta:
         db_table="ec_users"




class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(unique=True,max_length=255,null=False,blank=False,validators=[RegexValidator('^[a-zA-Z]*$',message='Category name must be in letters')])
    category_desc=models.CharField(max_length=255,default="")

    class Meta:
         db_table="ec_category"


class Subcategory(models.Model):
    subcat_id =models.AutoField(primary_key=True)
    parent_cat_id= models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=255,blank=False,null=False,validators=[RegexValidator('^[a-zA-Z]*$',message='SubCategory name must be in  letters')])
    subcategory_desc =models.CharField(max_length=255,default="")

    class Meta:
         db_table="ec_subcategory"

class Products(models.Model): 
    product_id =models.AutoField(primary_key=True)
    product_name =models.CharField(max_length=255,null=False,blank=False,unique=True,validators=[RegexValidator('^[a-zA-Z0-9]*$',message='Product name must be in Alpha numeric')])
    product_desc=models.CharField(max_length=255,null=False,blank=False,default="")
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category_id=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    specification=models.CharField(max_length=255,default="",blank=False)
    Image=models. FileField(upload_to = 'images/')
    #Image=models.JSONField
    stock=models.IntegerField()
    price=models.IntegerField()
    discount_price=models.IntegerField()
    brand=models.CharField(max_length=255,validators=[RegexValidator('^[a-zA-Z0-9]*$',message='Brand name must be in Alpha numeric')])

    class Meta:
         db_table="ec_products"



class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    product_id =models.ForeignKey(Products,on_delete=models.CASCADE)
    user_id =models.ForeignKey(Users,on_delete=CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField()
    invoice_no=models.CharField(max_length=256,null=False,blank=False)
    payment_address=models.TextField(null=False,blank=False)
    shipping_address=models.TextField(null=False,blank=False)

    class Meta:
         db_table="ec_order"



class OrderTracking(models.Model):
    tracking_id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Orders,on_delete=CASCADE)
    shipment_status=models.CharField(max_length=100,validators=[RegexValidator('^[a-zA-Z]*$',message='Status must be in Letters')])
    current_location=models.CharField(max_length=255,null=False,blank=False,validators=[RegexValidator('^[a-zA-Z]*$',message='Current Location must be in Letters')])
    destination=models.CharField(max_length=255,null=False,blank=False,validators=[RegexValidator('^[a-zA-Z]*$',message='Destination must be in Letters')])
    shipment_date=models.DateTimeField()

    class Meta:
         db_table="ec_order_tracking"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)