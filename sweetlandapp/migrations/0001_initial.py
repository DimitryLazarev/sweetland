# Generated by Django 3.2 on 2021-04-19 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='static/sweetlandapp')),
                ('description', models.CharField(max_length=35)),
                ('full_description', models.CharField(max_length=255)),
                ('product_type', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='static/sweetlandapp')),
                ('description', models.CharField(max_length=35)),
                ('full_description', models.CharField(max_length=255)),
                ('product_type', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='sweetlandapp.products')),
            ],
        ),
    ]
