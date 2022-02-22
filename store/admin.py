from django.contrib import admin
from store.models import Category, Product,ProductImages
# Register your models here.


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)