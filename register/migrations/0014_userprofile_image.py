# Generated by Django 3.0 on 2020-12-04 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_remove_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile_images'),
        ),
    ]
