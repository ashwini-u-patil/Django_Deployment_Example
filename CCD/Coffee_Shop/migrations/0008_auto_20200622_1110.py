# Generated by Django 3.0.7 on 2020-06-22 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coffee_Shop', '0007_auto_20200622_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
    ]
