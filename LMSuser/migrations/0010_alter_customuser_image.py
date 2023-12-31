# Generated by Django 4.2.5 on 2023-11-04 11:19

import LMSuser.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSuser', '0009_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default=LMSuser.models.get_default_profile_image, null=True, upload_to='profile_pic', verbose_name='Profil Resmi'),
        ),
    ]
