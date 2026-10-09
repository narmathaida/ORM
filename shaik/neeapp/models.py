from django.db import models
from django.contrib import admin
class Product(models.Model):
    Product_Id=models.IntegerField(primary_key=True)
    Product_Name=models.CharField(max_length=10)
    Category=models.CharField(max_length=20)
    Brand=models.CharField(max_length=10)
    Rate=models.IntegerField()
    Gst=models.FloatField()
    Quantity=models.IntegerField()
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "Product_Id",
        "Product_Name",
        "Category",
        "Brand",
        "Rate",
        "Gst",
        "Quantity"
         ]
