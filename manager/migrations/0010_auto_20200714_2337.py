# Generated by Django 3.0.8 on 2020-07-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20200713_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, default='../media/profile_pictures/default_pic.jpg', null=True, upload_to='profile_pictures/'),
        ),
    ]
