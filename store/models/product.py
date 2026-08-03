from django.db import models
from .category import Category
from django.db.models import Q

class Products(models.Model):
    name = models.CharField(max_length=255)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products()

    @staticmethod
    def search_products(query):
        if query:
            return Products.objects.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query) | 
                Q(category__name__icontains=query)
            )
        return Products.get_all_products()