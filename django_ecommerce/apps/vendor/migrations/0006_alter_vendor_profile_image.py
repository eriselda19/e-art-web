# Generated by Django 3.2.5 on 2021-08-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_vendor_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/artisan/'),
        ),
    ]
