from django.contrib import admin

from product_module.models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'price', 'short_description', 'rating', 'is_active']
    list_filter = ['is_active', 'rating']
    list_editable = ['is_active', 'price']


admin.site.register(Product, ProductAdmin)
