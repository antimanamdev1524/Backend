from django.utils import timezone
from django.db import models


# Create your models here.

class User(models.Model):
    usertype = models.CharField(max_length= 20, default="buyer")
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique= True)
    mobile = models.BigIntegerField(unique= True)
    password = models.CharField(max_length= 20)
    uprofile = models.ImageField(default="", upload_to= 'uprofile/')

    def __str__(self):
        return self.name

class Product(models.Model):
    Seller= models.ForeignKey(User,on_delete=models.CASCADE)
    Category= (
        ("Men","Men"),
        ("Women","Women"),
        ("Kids","Kids"),
        ("Jewellary","Jewellary"),
        ("Accessories","Accessories")
    )


    Brand= (
        ("Raymond","Raymond"),
        ("Polo","Polo"),
        ("Puma","Puma"),
        ("Peter England","Peter England"),
        ("Nike","Nike"),
        ("Other", "Other")
    )

    Size= (
        ("S","S"),
        ("M","M"),
        ("L","L"),
        ("XL","XL"),
        ("XXL","XXL"),
        ("XXXL","XXXL"),
        ("Free size","Free size"),
        ("0-3 Month","0-3 Month"),
        ("3-6 Month","3-6 Month"),
        ("1-2 year","1-2 year"),
        ("3-5 year","3-5 year"),
        ("5-7 year","5-7 year")
    )

    Scategory = models.CharField(max_length=40, choices= Category)
    Sbrand = models.CharField(max_length=40, choices= Brand)
    Ssize= models.CharField(max_length= 40, choices= Size)
    Price=models.IntegerField()
    Pname = models.CharField(max_length= 100)
    Description= models.TextField()
    Image= models.ImageField(upload_to= 'Profile/')
    
    def __str__(self):
        return self.Pname
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ttime =  models.DateTimeField(default=timezone.now)


class Cart(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    qty = models.IntegerField(default=1)
    price= models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return self.product
