# Generated by Django 3.2 on 2021-10-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211012_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user_image',
            field=models.ImageField(default='', null=True, upload_to='userimages'),
        ),
    ]