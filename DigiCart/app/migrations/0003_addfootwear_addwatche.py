# Generated by Django 4.0.3 on 2022-08-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_addgrocery_addhomeitem_addkidsitem_addlaptop_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFootwear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='Footwear')),
            ],
        ),
        migrations.CreateModel(
            name='AddWatche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='Watche')),
            ],
        ),
    ]
