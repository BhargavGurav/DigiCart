from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
        ('T', 'T')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField()
    profile_pic = models.ImageField(upload_to='Profile_pics', blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    address = models.TextField()
    gender = models.CharField(max_length=2, choices=GENDER)
    

    def __str__(self):
        return self.user.username
    
class Cart(models.Model):
    user = models.ForeignKey('Customer',  on_delete=models.CASCADE)
    item_image = models.ImageField(upload_to='cart')
    category = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    item_disc = models.TextField()
    quantity = models.IntegerField()

class History(models.Model):
    user = models.ForeignKey("Customer", on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    total_price = models.IntegerField()
    

class AddMobile(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='Mobile')

    def __str__(self):
        return self.name
    
class AddLaptop(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='Laptop')

    def __str__(self):
        return self.name
    
class AddMenItem(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='Men')

    def __str__(self):
        return self.name
    
class AddWomenItem(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='Women')

    def __str__(self):
        return self.name
    
class AddKidsItem(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='Kids')

    def __str__(self):
        return self.name
    
class AddHomeItem(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='Home')

    def __str__(self):
        return self.name
    
class AddGrocery(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='Grocery')

    def __str__(self):
        return self.name

class AddWatche(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='Watche')

    def __str__(self):
        return self.name

class AddFootwear(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    image = models.ImageField(upload_to='Footwear')

    def __str__(self):
        return self.name     
    