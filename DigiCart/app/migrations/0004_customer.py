# Generated by Django 4.0.3 on 2022-08-06 04:59

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_addfootwear_addwatche'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(upload_to='Profile_pics')),
                ('dob', models.DateField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
