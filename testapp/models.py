from django.db import models

# Create your models here.
class Prodcuts(models.Model):
    product_name=models.CharField(max_length=100)
    product_type=models.CharField(max_length=100)
    description=models.TextField()
    picture=models.ImageField()
    discounted_price=models.FloatField()
    original_price = models.FloatField()


    def __str__(self):
        return self.product_name

class User_details(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=16)
    mobile_No = models.IntegerField()
    city=models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    pin_code = models.IntegerField()

    def __str__(self):
        return self.user_name