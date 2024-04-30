from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در لینک')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = "دسته بندی ها"


class ProductInformation(models.Model):
    color = models.CharField(max_length=200, verbose_name="رنگ")
    size = models.CharField(max_length=200, verbose_name="اندازه")

    def __str__(self):
        return f"{self.color} - {self.size}"

    class Meta:
        verbose_name = 'اطلاعات تکمیلی'
        verbose_name_plural = "اطلاعات تکمیلی"


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='اسم')
    product_information = models.OneToOneField(ProductInformation, models.CASCADE, related_name="product_information",
                                               verbose_name="اطلاعات تکمیلی", null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, related_name="products",
                                 verbose_name="دسته بندی محصولات")
    price = models.IntegerField(verbose_name='قیمت')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0,
                                 verbose_name='امتیاز')
    short_description = models.CharField(max_length=360, null=True, verbose_name="توضیحات کوتاه")
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    slug = models.SlugField(default='', null=False, db_index=True, blank=True, verbose_name='اسلاگ')

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.price})'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = "محصولات"
