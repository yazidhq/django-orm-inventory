# Generated by Django 4.2.7 on 2023-11-24 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute', to='inventory.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('is_active', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('is_default', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sku', models.CharField(max_length=20, unique=True)),
                ('attribute_value', models.ManyToManyField(to='inventory.attributevalue')),
            ],
            options={
                'verbose_name_plural': 'Inventory',
            },
        ),
        migrations.CreateModel(
            name='StockControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_checked', models.DateTimeField(editable=False)),
                ('units', models.IntegerField(default=0)),
                ('inventory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
            ],
            options={
                'verbose_name_plural': 'Stock Control',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('is_active', models.BooleanField()),
                ('category', models.ManyToManyField(to='inventory.category')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='inventory.product'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to=None)),
                ('alternative_text', models.CharField(max_length=50)),
                ('is_feature', models.BooleanField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
            ],
        ),
    ]
