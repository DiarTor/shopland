# Generated by Django 5.0.1 on 2024-05-02 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان در لینک')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='اسم')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='اسلاگ')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='حذف شده / نشده')),
                ('category', models.ManyToManyField(related_name='product_categories', to='product_module.productcategory', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='product_module.product')),
            ],
            options={
                'verbose_name': 'عنوان محصولات',
                'verbose_name_plural': 'عنوان های محصولات',
            },
        ),
    ]
