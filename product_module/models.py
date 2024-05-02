from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان', db_index=True)
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در لینک')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_deleted = models.BooleanField(default=False, verbose_name='حذف شده / نشده')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return f"{self.title} - {self.url_title}"


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(ProductCategory, related_name="product_categories",
                                      verbose_name="دسته بندی ها")
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name="توضیحات اصلی", db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    slug = models.SlugField(default='', null=False, blank=True, verbose_name='عنوان در لینک', max_length=200, unique=True)
    is_deleted = models.BooleanField(default=False, verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        #self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.price})'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = "محصولات"


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name="عنوان")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_tags")

    class Meta:
        verbose_name = 'عنوان محصولات'
        verbose_name_plural = "عنوان های محصولات"
