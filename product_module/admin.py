from django.contrib import admin

from product_module.models import Product, ProductCategory, ProductInformation


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'price', 'short_description', 'rating', 'is_active', 'product_information', 'category']
    list_filter = ['is_active', 'rating']
    list_editable = ['is_active', 'price']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductInformation)