# Generated by Django 3.0 on 2020-12-04 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]
