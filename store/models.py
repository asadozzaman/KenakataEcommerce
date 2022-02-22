from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False,null=False)
    image = models.ImageField(upload_to='category',blank=True,null=True)
    parent = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name_plural= 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_des = models.CharField(max_length=255, verbose_name='Short Description')
    description = models.TextField(max_length=1000, verbose_name='Description')
    image = models.ImageField(upload_to='products',blank=False,null=False)
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    is_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]