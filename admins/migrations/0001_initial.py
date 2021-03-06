# Generated by Django 3.1.7 on 2021-03-29 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandName', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=300)),
                ('productDescription', models.TextField()),
                ('wholesalePrice', models.IntegerField()),
                ('salesPrice', models.IntegerField()),
                ('brand', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.brandmodel')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='SuplierModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suplierName', models.CharField(max_length=100)),
                ('suplierContact', models.BigIntegerField()),
                ('suplierAddress', models.TextField()),
            ],
            options={
                'db_table': 'supliers',
            },
        ),
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoryName', models.CharField(max_length=50)),
                ('subCategoryType', models.CharField(default=None, max_length=200)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.categorymodel')),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
        migrations.CreateModel(
            name='ProductModelImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImages', models.FileField(blank=True, default='', max_length=2000, null=True, upload_to='images/products/%Y%m')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.productmodel')),
            ],
            options={
                'db_table': 'productImages',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='subCategory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.subcategorymodel'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='suplier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.supliermodel'),
        ),
    ]
