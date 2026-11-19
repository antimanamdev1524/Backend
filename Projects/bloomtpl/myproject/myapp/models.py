from django.db import models

# Create your models here.

class BuyerProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    mobile_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    def __str__(self):
        return self.user.username
    
class SellerProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    mobile_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='subcategories')
    
    def __str__(self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to='products/')
    size = models.CharField(max_length=50, blank = True)
    color = models.CharField(max_length=50, blank = True)
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        null = True,
        blank = True
        )
    seller = models.ForeignKey(
        SellerProfile, 
        on_delete=models.CASCADE,
        null = True,
        blank = True
        ) 
    stock = models.BooleanField(null=True, default=True)

    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100, blank = True)
    street = models.CharField(max_length=100, blank = True)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.apartment}, {self.street}, {self.city}, {self.district}, {self.state}, {self.country} - {self.pincode}"


