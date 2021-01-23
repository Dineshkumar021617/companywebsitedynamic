from django.db import models
from django.contrib import admin

# Create your models here.
class products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_img = models.ImageField()

class productsadmin(admin.ModelAdmin):
    list_display = ('product_name','product_price','product_img')

class people(models.Model):
    people_name = models.CharField(max_length=100)
    people_desig = models.CharField(max_length=50)
    people_img = models.ImageField()

class peopleadmin(admin.ModelAdmin):
    list_display = ('people_name','people_desig','people_img')