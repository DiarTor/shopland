from django.contrib import admin

from product_module.models import Product, ProductCategory, ProductTag


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'is_active', 'is_deleted']
    list_display = ['title', 'price', 'is_active', 'is_deleted']
    list_editable = ['price', 'is_active', 'is_deleted']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
