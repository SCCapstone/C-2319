# Generated by Django 3.0 on 2020-12-05 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/profile_images/blank-profile-picture-png.png', null=True, upload_to=''),
        ),
    ]
